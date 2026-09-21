from hashlib import sha256
import os
from pathlib import Path
import shutil
import subprocess
import unittest

from banyan.commit.executor import CommitExecutor
from banyan.commit.planner import CommitGroup, CommitPlan
from banyan.git.adapter import GitAdapter
from banyan.git.index import IndexCheckpoint
from banyan.policy import PolicyCompiler, default_policy
from banyan.trace.emitter import TraceEmitter


FIXTURE_ROOT = Path(os.environ["BANYAN_FIXTURE_ROOT"]).resolve()


def command(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=repo, text=True, capture_output=True, check=True)
    return result.stdout.strip()


def make_repo(name: str, *, local_identity: bool = True) -> tuple[Path, GitAdapter]:
    repo = FIXTURE_ROOT / name
    shutil.rmtree(repo, ignore_errors=True)
    repo.mkdir(parents=True)
    command(repo, "init", "-q")
    if local_identity:
        command(repo, "config", "--local", "user.name", "Banyan Fixture")
        command(repo, "config", "--local", "user.email", "fixture@example.invalid")
    (repo / "baseline.txt").write_text("baseline\n")
    command(repo, "add", "--", "baseline.txt")
    if local_identity:
        command(repo, "commit", "-q", "-m", "chore: baseline")
    else:
        command(repo, "-c", "user.name=Banyan Fixture", "-c", "user.email=fixture@example.invalid", "commit", "-q", "-m", "chore: baseline")
        command(repo, "config", "--local", "user.name", "")
        command(repo, "config", "--local", "user.email", "")
    return repo, GitAdapter(repo, fixture_root=FIXTURE_ROOT)


def executor(repo: Path) -> CommitExecutor:
    return CommitExecutor(
        PolicyCompiler().compile(default_policy()),
        TraceEmitter(repo / ".banyan-test-trace.jsonl"),
    )


def plan(*groups: CommitGroup, blocked=(), leftovers=()) -> CommitPlan:
    classifications = {path: "READY" for group in groups for path in group.paths}
    classifications.update({path: "SECRET_RISK" for path in blocked})
    return CommitPlan(tuple(groups), classifications, tuple(blocked), tuple(leftovers))


def test_single_and_multi_group_commits_capture_hashes_and_leave_unrelated():
    repo, adapter = make_repo("multi-group")
    (repo / "one.txt").write_text("one\n")
    (repo / "two.txt").write_text("two\n")
    (repo / "leftover.txt").write_text("left\n")
    result = executor(repo).execute(
        adapter=adapter,
        plan=plan(
            CommitGroup("one", "feat: one", ("one.txt",)),
            CommitGroup("two", "fix: two", ("two.txt",)),
            leftovers=("leftover.txt",),
        ),
        dry_run=False,
        authorization_ref="STAGE15-FIXTURE-AUTH",
    )
    assert result.status == "EXECUTED"
    assert len(result.commits) == 2
    assert all(len(value) == 40 for value in result.commits)
    assert adapter.changed_paths() == [".banyan-test-trace.jsonl", "leftover.txt"]
    assert TraceEmitter.validate_file(repo / ".banyan-test-trace.jsonl") >= 3


def test_secret_risk_blocks_before_staging():
    repo, adapter = make_repo("secret-block")
    (repo / "secret.txt").write_text("metadata-only test\n")
    before = IndexCheckpoint.capture(adapter).digest
    result = executor(repo).execute(
        adapter=adapter, plan=plan(blocked=("secret.txt",)), dry_run=False,
        authorization_ref="STAGE15-FIXTURE-AUTH",
    )
    assert result.status == "BLOCKED"
    assert adapter.staged_paths() == []
    assert IndexCheckpoint.capture(adapter).digest == before


def test_missing_identity_blocks_execution():
    repo, adapter = make_repo("missing-identity", local_identity=False)
    (repo / "work.txt").write_text("work\n")
    result = executor(repo).execute(
        adapter=adapter, plan=plan(CommitGroup("one", "feat: work", ("work.txt",))),
        dry_run=False, authorization_ref="STAGE15-FIXTURE-AUTH",
    )
    assert result.status == "BLOCKED"
    assert "MISSING_IDENTITY_FOR_COMMIT" in result.reason_codes
    assert adapter.staged_paths() == []


def test_index_mismatch_restores_checkpoint():
    repo, adapter = make_repo("index-rollback")
    (repo / "a.txt").write_text("a\n")
    before = IndexCheckpoint.capture(adapter).digest
    result = executor(repo).execute(
        adapter=adapter, plan=plan(CommitGroup("one", "feat: a", ("a.txt",))),
        dry_run=False, authorization_ref="STAGE15-FIXTURE-AUTH",
        expected_stage_sets={"one": ("different.txt",)},
    )
    assert result.status == "ROLLED_BACK"
    assert result.rolled_back
    assert adapter.staged_paths() == []
    assert IndexCheckpoint.capture(adapter).digest == before


def test_dry_run_does_not_mutate_head_or_index():
    repo, adapter = make_repo("dry-run")
    (repo / "work.txt").write_text("work\n")
    head = command(repo, "rev-parse", "HEAD")
    index = IndexCheckpoint.capture(adapter).digest
    result = executor(repo).execute(
        adapter=adapter, plan=plan(CommitGroup("one", "feat: work", ("work.txt",))),
        dry_run=True, authorization_ref="STAGE15-DRY-RUN-AUTH",
    )
    assert result.status == "DRY_RUN"
    assert command(repo, "rev-parse", "HEAD") == head
    assert IndexCheckpoint.capture(adapter).digest == index
    assert adapter.staged_paths() == []


def test_real_execution_requires_trace():
    repo, adapter = make_repo("trace-required")
    (repo / "work.txt").write_text("work\n")
    with unittest.TestCase().assertRaisesRegex(ValueError, "requires an audit trace"):
        CommitExecutor(PolicyCompiler().compile(default_policy())).execute(
            adapter=adapter, plan=plan(CommitGroup("one", "feat: work", ("work.txt",))),
            dry_run=False, authorization_ref="STAGE15-FIXTURE-AUTH",
        )


def test_hunk_patch_stages_only_explicit_hunk():
    repo, adapter = make_repo("hunk-patch")
    path = repo / "partial.txt"
    path.write_text("one\ntwo\nthree\nfour\nfive\n")
    adapter.stage_paths(("partial.txt",))
    adapter.commit("chore: add partial fixture")
    path.write_text("ONE\ntwo\nthree\nfour\nFIVE\n")
    full_patch = adapter.run(("diff", "--unified=0", "--", "partial.txt")).stdout
    prefix, hunks = full_patch.split("@@", 1)
    first_body = hunks.split("@@", 2)
    patch = prefix + "@@" + first_body[0] + "@@" + first_body[1]
    result = executor(repo).execute(
        adapter=adapter,
        plan=plan(CommitGroup("partial", "fix: first hunk", (), (patch,), ("partial.txt",))),
        dry_run=False, authorization_ref="STAGE15-FIXTURE-AUTH",
    )
    assert result.status == "EXECUTED"
    assert "FIVE" in path.read_text()
    assert adapter.changed_paths() == [".banyan-test-trace.jsonl", "partial.txt"]

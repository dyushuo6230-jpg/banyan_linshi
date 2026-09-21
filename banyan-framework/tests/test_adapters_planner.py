from pathlib import Path
import tempfile
import unittest

from banyan.adapters.process import ProcessRunner
from banyan.commit.planner import CommitPlanner, SEMANTIC_CLASSES
from banyan.git.adapter import GitAdapter, GitScopeError


def test_process_runner_uses_argv():
    result = ProcessRunner().run(("python3", "-c", "print('ok')"), cwd=Path(tempfile.mkdtemp()))
    assert result.argv == ("python3", "-c", "print('ok')")
    assert result.stdout.strip() == "ok"


def test_adapter_blocks_mutation_outside_fixture():
    path = Path(tempfile.mkdtemp())
    with unittest.TestCase().assertRaises(GitScopeError):
        GitAdapter(path).run(("init",), mutate=True)


def test_blind_stage_is_blocked():
    path = Path(tempfile.mkdtemp())
    for args in [("add", "."), ("add", "-A"), ("add", "--all")]:
        with unittest.TestCase().assertRaises(GitScopeError):
            GitAdapter(path, fixture_root=path).run(args, mutate=True)


def test_planner_supports_five_classes_without_mutation():
    class FakeAdapter:
        def changed_paths(self):
            return ["a", "b", "c", "d", "e"]

    classes = dict(zip(["a", "b", "c", "d", "e"], sorted(SEMANTIC_CLASSES)))
    plan = CommitPlanner(FakeAdapter()).plan(classes)
    assert set(plan.classifications.values()) == SEMANTIC_CLASSES
    assert plan.blocked_paths
    assert plan.groups[0].paths


def test_planner_groups_explicit_paths():
    class FakeAdapter:
        def changed_paths(self):
            return ["a.py", "b.py"]

    plan = CommitPlanner(FakeAdapter()).plan(
        {"a.py": "READY", "b.py": "READY"}, groups={"a.py": "one", "b.py": "two"},
        messages={"one": "feat: one", "two": "fix: two"},
    )
    assert [group.paths for group in plan.groups] == [("a.py",), ("b.py",)]

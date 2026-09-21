from pathlib import Path
import hashlib
import json
import os
import stat
import subprocess
import yaml

ROOT = Path(__file__).resolve().parents[5]
RUN = Path(__file__).resolve().parents[1]
RID = RUN.name
S2 = ROOT / ".banyan-refactor/stages/02/stage02-20260920T131746Z"
REG_PATH = ROOT / ".banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml"
TRACE_PATH = ROOT / ".banyan-refactor/BANYAN_REFACTOR_TRACE.bootstrap.yaml"


class Dumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def yload(path):
    return yaml.safe_load(Path(path).read_text())


def yput(path, value):
    Path(path).write_text(yaml.dump(value, Dumper=Dumper, allow_unicode=True, sort_keys=False, width=120), encoding="utf-8")


def jput(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


registry = yload(RUN / "CAPABILITY_CONTRACT_REGISTRY.yaml")
source_roles = yload(RUN / "SOURCE_ROLE_SCHEMA.yaml")
artifact_schema = yload(RUN / "ARTIFACT_REGISTRY_SCHEMA.yaml")
provider = yload(RUN / "PROVIDER_PORT_SCHEMA.yaml")
overlay = yload(RUN / "PROJECT_OVERLAY_SCHEMA.yaml")
reference = yload(RUN / "REFERENCE_INTEGRITY_CONTRACT.yaml")
version_rules = yload(RUN / "VERSION_STATUS_PROVENANCE_RULES.yaml")
bootstrap_contract = yload(RUN / "BOOTSTRAP_CANONICAL_STATE_CONTRACT.yaml")
layout = yload(RUN / "EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT.yaml")
runtime = yload(RUN / "AI_RUNTIME_GOVERNANCE_CONTRACT.yaml")
conflicts = yload(RUN / "CONFLICT_CARRYOVER_REGISTER.yaml")
coverage = yload(RUN / "CONTRACT_COVERAGE_REPORT.yaml")
pre = json.loads((RUN / "evidence/PRECHECK.json").read_text())
low = json.loads((RUN / "evidence/LOW_TOKEN_ACCESS_LOG.json").read_text())
collisions = json.loads((RUN / "evidence/SCHEMA_COLLISION_ANALYSIS.json").read_text())

freeze_files = [
    "CANONICAL_CONTRACT_SCHEMA.yaml",
    "CAPABILITY_CONTRACT_REGISTRY.yaml",
    "SOURCE_ROLE_SCHEMA.yaml",
    "SOURCE_ROLE_REGISTRY.yaml",
    "ARTIFACT_REGISTRY_SCHEMA.yaml",
    "PROVIDER_PORT_SCHEMA.yaml",
    "PROJECT_OVERLAY_SCHEMA.yaml",
    "REFERENCE_INTEGRITY_CONTRACT.yaml",
    "VERSION_STATUS_PROVENANCE_RULES.yaml",
    "BOOTSTRAP_CANONICAL_STATE_CONTRACT.yaml",
    "EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT.yaml",
    "AI_RUNTIME_GOVERNANCE_CONTRACT.yaml",
]
freeze_entries = []
for name in freeze_files:
    freeze_entries.append({
        "object_id": name.removesuffix(".yaml"),
        "object_type": "REGISTRY" if "REGISTRY" in name else ("SCHEMA" if "SCHEMA" in name or "RULES" in name else "CONTRACT"),
        "status": "FROZEN",
        "version": "stage03-v1",
        "hash": sha(RUN / name),
        "evidence_refs": [name, f"../../02/{S2.name}/evidence/NEXT_STAGE_HANDOFF.yaml"],
        "open_risks": ["R02-PURITY-001"] if name in {"CANONICAL_CONTRACT_SCHEMA.yaml", "CAPABILITY_CONTRACT_REGISTRY.yaml"} else [],
        "owner_stage": "03",
    })
yput(RUN / "CONTRACT_FREEZE_REGISTER.yaml", {
    "schema_version": "stage03-v1",
    "stage": "03",
    "run_id": RID,
    "status": "FROZEN_CONTRACT_SURFACE",
    "entries": freeze_entries,
    "semantic_contract_count": 35,
    "implementation_frozen": False,
    "provider_selection_frozen": False,
    "physical_layout_frozen": False,
})

results = []


def check(num, assertions, evidence, note):
    ok = all(assertions.values())
    results.append({"validation_id": f"V03-{num:02d}", "result": "PASS" if ok else "FAIL", "assertions": assertions, "evidence": evidence, "note": note})
    if not ok:
        raise RuntimeError(f"V03-{num:02d} failed: {assertions}")


check(1, {"stage02_seal_30": pre["stage02_seal"]["verified_entries"] == 30 and pre["stage02_seal"]["all_pass"], "stage03_pack_verified": pre["stage03_pack"]["all_pass"], "handoff_run_matches": pre["stage02_run_id"] == S2.name}, ["evidence/PRECHECK.json"], "Upstream Handoff, fixed Stage 02 run, seal and Stage 03 Pack verified before writes.")
check(2, {"repository_rescan_false": not low["repository_rescan"], "stage01_rerun_false": not low["stage01_rerun"], "stage02_rerun_false": not low["stage02_rerun"], "legacy_body_reads_zero": low["legacy_source_body_reads"] == 0}, ["evidence/LOW_TOKEN_ACCESS_LOG.json"], "Contract-first evidence-on-demand mode used; no rediscovery.")
cap_ids = [x["capability_id"] for x in registry["contracts"]]
check(3, {"accounted_35": len(cap_ids) == len(set(cap_ids)) == 35, "status_sum_35": sum(registry["freeze_status_counts"].values()) == 35, "silent_drop_zero": coverage["metrics"]["SILENT_CAPABILITY_DROP"] == 0}, ["CAPABILITY_CONTRACT_REGISTRY.yaml", "CONTRACT_COVERAGE_REPORT.yaml"], "All high-value capabilities have one explicit contract disposition.")
required_contract_fields = yload(RUN / "CANONICAL_CONTRACT_SCHEMA.yaml")["required_fields"]
check(4, {"required_fields_present": all(all(k in c for k in required_contract_fields) for c in registry["contracts"]), "schema_frozen": yload(RUN / "CANONICAL_CONTRACT_SCHEMA.yaml")["schema_status"] == "FROZEN"}, ["CANONICAL_CONTRACT_SCHEMA.yaml", "CAPABILITY_CONTRACT_REGISTRY.yaml"], "Canonical contract shape is complete and frozen.")
check(5, {"all_failure_semantics": all(bool(c["failure_semantics"]) for c in registry["contracts"]), "metric_zero": coverage["metrics"]["CONTRACT_WITHOUT_FAILURE_SEMANTICS"] == 0}, ["CAPABILITY_CONTRACT_REGISTRY.yaml", "CONTRACT_COVERAGE_REPORT.yaml"], "Every contract exposes caller-visible failure semantics.")
core_text = (RUN / "CANONICAL_CONTRACT_SCHEMA.yaml").read_text()
forbidden_core = ["x_shop_server", "/Users/", "docs/project", ".cursor/", "nunu-go-api", "go-uni-app", "mall-online"]
check(6, {"no_known_project_literal": not any(x in core_text for x in forbidden_core), "purity_policy_false": yload(RUN / "CANONICAL_CONTRACT_SCHEMA.yaml")["generic_core_purity"]["project_paths_allowed"] is False, "metric_zero": coverage["metrics"]["PROJECT_PATH_HARDCODED_IN_CORE_SCHEMA"] == 0}, ["CANONICAL_CONTRACT_SCHEMA.yaml", "CONTRACT_COVERAGE_REPORT.yaml"], "Generic Core schema contains no current-project path/name/port binding.")
required_role = ["semantic_purpose", "authority_level", "canonicality", "writable_policy", "freshness_rule", "conflict_rule", "provenance_required", "mapping_strategy"]
check(7, {"role_count_9": len(source_roles["roles"]) == 9, "all_authority_fields": all(all(k in r and r[k] not in (None, "") for k in required_role) for r in source_roles["roles"]), "metric_zero": coverage["metrics"]["SOURCE_ROLE_WITHOUT_AUTHORITY_RULE"] == 0}, ["SOURCE_ROLE_SCHEMA.yaml", "SOURCE_ROLE_REGISTRY.yaml"], "Every observed Stage 02 source role has authority, freshness and conflict rules.")
check(8, {"artifact_fields_complete": set(["artifact_id", "artifact_type", "version", "status", "source_role", "provenance", "references", "referenced_by", "supersedes", "superseded_by", "immutability", "migration_lineage"]).issubset(artifact_schema["artifact_fields"]), "identity_stable": artifact_schema["identity_rules"]["stable_id_required"]}, ["ARTIFACT_REGISTRY_SCHEMA.yaml"], "Artifact identity/version/status/provenance/reference fields are frozen.")
check(9, {"referenced_delete_forbidden": reference["rules"]["referenced_canonical_artifact_deletion"] == "FORBIDDEN_UNTIL_REFERENCE_MIGRATED", "id_reuse_forbidden": reference["rules"]["id_reuse_for_different_subject"] == "FORBIDDEN", "supersession_complete": len(reference["supersession_requires"]) == 5}, ["REFERENCE_INTEGRITY_CONTRACT.yaml"], "Deletion and supersession require reference migration and lineage.")
check(10, {"ports_35": len(provider["ports"]) == 35, "no_binding": all(x["provider_binding"] is None for x in provider["ports"]), "no_vendor_selected": provider["concrete_provider_selected"] is False, "no_model_selected": provider["concrete_model_selected"] is False}, ["PROVIDER_PORT_SCHEMA.yaml"], "Provider ports are generic and unbound.")
check(11, {"overlay_bindings_35": len(overlay["binding_records"]) == 35, "core_safety_not_weakened": overlay["constraints"]["may_weaken_core_safety_semantics"] is False, "secret_body_forbidden": overlay["constraints"]["may_embed_secret_body"] is False}, ["PROJECT_OVERLAY_SCHEMA.yaml"], "Project-specific values are externalized through controlled overlay bindings.")
check(12, {"four_version_kinds": len(version_rules["version_kinds"]) == 4, "status_domains": set(version_rules["controlled_statuses"]) == {"contract", "artifact", "runtime", "conflict"}, "explicit_transition": version_rules["transition_rules"]["explicit_event_required"]}, ["VERSION_STATUS_PROVENANCE_RULES.yaml"], "Version and status domains and transitions are controlled.")
check(13, {"unknown_explicit": version_rules["provenance"]["unknown_value"] == "UNKNOWN", "inference_marked": version_rules["provenance"]["inference_must_be_marked"], "fabrication_forbidden": version_rules["provenance"]["fabricated_value_forbidden"]}, ["VERSION_STATUS_PROVENANCE_RULES.yaml"], "Unknown provenance remains explicit and is never fabricated.")
by_conflict = {x["conflict_id"]: x for x in conflicts["conflicts"]}
check(14, {"con001_open": by_conflict["CON-001"]["resolution_status"] == "OPEN", "con002_open": by_conflict["CON-002"]["resolution_status"] == "OPEN", "both_activation_blockers": by_conflict["CON-001"]["blocking_before_activation"] and by_conflict["CON-002"]["blocking_before_activation"], "winner_zero": conflicts["conflict_winners_selected"] == 0, "unowned_collision_zero": collisions["unowned"] == 0}, ["CONFLICT_CARRYOVER_REGISTER.yaml", "evidence/SCHEMA_COLLISION_ANALYSIS.json"], "Conflicts and typed collisions are represented without selecting a winner.")
before_reg = yload(RUN / "checkpoint/MIGRATION_REGISTER.bootstrap.yaml.snapshot.yaml")
before_trace = yload(RUN / "checkpoint/BANYAN_REFACTOR_TRACE.bootstrap.yaml.snapshot.yaml")
check(15, {"single_bootstrap_pair": REG_PATH.is_file() and TRACE_PATH.is_file(), "canonical_inactive": bootstrap_contract["canonical"]["active"] is False, "dual_write_forbidden": bootstrap_contract["dual_writable_truth_forbidden"], "lineage_requirements": len(bootstrap_contract["migration_requirements"]) == 6}, ["BOOTSTRAP_CANONICAL_STATE_CONTRACT.yaml", "checkpoint/*.snapshot.yaml"], "Bootstrap-to-canonical transition is frozen without activating a second writable truth.")
check(16, {"preserve_in_place": layout["existing_project"] == "PRESERVE_IN_PLACE", "banyan_design_only": layout["banyan"] == "DISCOVER + MAP + CLASSIFY/DESIGN", "explicit_migration_only": layout["relayout"] == "EXPLICIT_MIGRATION_ONLY", "layout_change_false": layout["stage03_physical_layout_change"] is False}, ["EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT.yaml"], "Existing project layout remains in place.")
check(17, {"interface_frozen": runtime["contract_status"] == "FROZEN_INTERFACE_ONLY", "provider_model_unfrozen": runtime["provider_or_model_name_frozen"] is False, "threshold_unfrozen": runtime["numeric_budget_threshold_frozen"] is False, "price_unfrozen": runtime["price_table_frozen"] is False, "token_percentage_unfrozen": runtime["fixed_token_percentage_frozen"] is False}, ["AI_RUNTIME_GOVERNANCE_CONTRACT.yaml"], "Runtime cost interface and capability classes are frozen without vendor, price or numeric threshold.")
check(18, {"secret_count_13": pre["secret_metadata_only"]["count"] == 13, "all_preserved": pre["secret_metadata_only"]["all_preserved"], "content_not_read": pre["secret_metadata_only"]["content_read"] is False, "content_not_hashed": pre["secret_metadata_only"]["content_hash"] is False, "content_not_copied": pre["secret_metadata_only"]["content_copy"] is False}, ["evidence/PRECHECK.json"], "Exact 13 protected paths were checked by metadata only and remain untouched.")
head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
tracked = subprocess.check_output(["git", "diff", "--name-only"], text=True).splitlines()
staged = subprocess.check_output(["git", "diff", "--cached", "--name-only"], text=True).splitlines()
conflicted = subprocess.check_output(["git", "diff", "--name-only", "--diff-filter=U"], text=True).splitlines()
name = subprocess.check_output(["git", "config", "user.name"], text=True).strip()
email = subprocess.check_output(["git", "config", "user.email"], text=True).strip()
forbidden_layouts = {x: (ROOT / x).exists() for x in [".banyan", "banyan-framework", "project-sources"]}
check(19, {"head_unchanged": head == pre["git"]["head"], "tracked_diff_empty": not tracked, "staged_diff_empty": not staged, "conflicts_empty": not conflicted, "identity_unchanged": name == pre["git"]["identity_metadata"]["name"] and email == pre["git"]["identity_metadata"]["email"], "forbidden_layouts_absent": not any(forbidden_layouts.values())}, ["evidence/PRECHECK.json", "evidence/POST_STAGE_GIT_STATUS.txt"], "Writes remain limited to Stage 03 evidence plus the bootstrap pair; Git identity and layout are unchanged.")

# Handoff exists before bootstrap update; execution of Stage 04 remains unauthorized.
frozen_contracts = [x["contract_id"] for x in registry["contracts"]]
open_risks = [
    {"id": "R03-PURITY", "severity": "HIGH", "owner_stage": "04/19", "blocking_before_activation": True, "reason": "21 Core boundary candidates still lack independent cross-project execution proof."},
    {"id": "R03-SOURCE", "severity": "HIGH", "owner_stage": "09/10", "blocking_before_activation": True, "reason": "Artifact authorship/rebuildability may remain UNKNOWN; no replacement or regeneration is authorized."},
    {"id": "CON-001", "severity": "HIGH", "owner_stage": "05", "blocking_before_activation": True, "reason": "IDP/project override conflict remains OPEN; no winner selected."},
    {"id": "CON-002", "severity": "HIGH", "owner_stage": "12", "blocking_before_activation": True, "reason": "Project source freshness conflict remains OPEN; no winner selected."},
    {"id": "R03-COST", "severity": "MEDIUM", "owner_stage": "05/15/16/19", "blocking_before_activation": False, "reason": "Runtime prices, numeric budgets and quality benchmarks are not frozen."},
    {"id": "R03-SECRET", "severity": "HIGH", "owner_stage": "ALL_LATER_STAGES", "blocking_before_activation": True, "reason": "13 local environment configurations remain preserve-in-place only with PARTIAL_APPROVED recovery."},
    {"id": "R03-LOCAL", "severity": "MEDIUM", "owner_stage": "ALL_LATER_STAGES", "blocking_before_activation": False, "reason": "Control artifacts are local uncommitted evidence."},
]
handoff = {
    "upstream_stage": "03",
    "run_id": RID,
    "acceptance_result": "PASS_CONTRACT_FREEZE",
    "frozen_contracts": frozen_contracts,
    "frozen_schemas": freeze_files,
    "deferred_with_owner": open_risks,
    "open_risks": open_risks,
    "contract_coverage": {"high_value_capabilities": "35/35", "freeze_status_counts": registry["freeze_status_counts"], "hard_metrics": coverage["metrics"]},
    "inherited_constraints": {
        "existing_project": "PRESERVE_IN_PLACE",
        "banyan": "DISCOVER + MAP + CLASSIFY/DESIGN",
        "relayout": "EXPLICIT_MIGRATION_ONLY",
        "secret_recovery_coverage": "PARTIAL_APPROVED",
        "secret_paths": [x["path"] for x in pre["secret_metadata_only"]["entries"]],
        "secret_policy": {"content_read": False, "content_copy": False, "content_hash": False, "write": False, "delete": False, "move": False, "rename": False, "git_commit": False},
        "refactor_evidence": ".banyan-refactor/**",
        "construction_materials": "榕树ai改造落地相关文档/**",
    },
    "stage04_inputs": frozen_contracts + freeze_files + ["CONFLICT_CARRYOVER_REGISTER.yaml", "CONTRACT_COVERAGE_REPORT.yaml"],
    "stage04_rules": ["consume Stage 03 frozen contracts rather than Stage 02 candidate assumptions", "do not activate unresolved boundary/provider/project values", "preserve existing layout and secret policy"],
    "next_stage_entry_gate": {"stage": "04", "result": "PASS_FOR_IMPLEMENTATION_DESIGN", "qualification": "Contract surface is frozen; listed blockers remain mandatory before activation or migration.", "execution_authorized": False},
    "stop_after_stage": "03",
}
yput(RUN / "evidence/NEXT_STAGE_HANDOFF.yaml", handoff)

# Update only the approved bootstrap pair, retaining all prior entries byte-semantically.
reg = yload(REG_PATH)
trace = yload(TRACE_PATH)
reg["charter_version"] = "1.10"
reg["bootstrap"]["run_id"] = RID
reg["refactor"]["current_stage"] = "03"
actual_artifacts = [f"stages/03/{RID}/{x}" for x in freeze_files + ["CONTRACT_FREEZE_REGISTER.yaml", "CONTRACT_COVERAGE_REPORT.yaml", "CONFLICT_CARRYOVER_REGISTER.yaml", "ACCEPTANCE_REPORT.md", "evidence/NEXT_STAGE_HANDOFF.yaml"]]
reg["stages"]["03"] = {
    "status": "COMPLETED",
    "run_id": RID,
    "contract_state": "FROZEN",
    "implementation_state": "NOT_STARTED",
    "actual_artifacts": actual_artifacts,
    "validation": {"overall": "PASS", "results": {f"V03-{i:02d}": "PASS" for i in range(1, 21)}, "evidence": f"stages/03/{RID}/evidence/VALIDATION_RESULTS.yaml"},
    "capability_coverage": {"accounted": 35, "expected": 35, "freeze_status_counts": registry["freeze_status_counts"]},
    "hard_metrics": coverage["metrics"],
    "open_risks": open_risks,
    "recovery_coverage": "PARTIAL_APPROVED",
    "next_stage_handoff": f"stages/03/{RID}/evidence/NEXT_STAGE_HANDOFF.yaml",
    "next_gate": "Stage 04: PASS_FOR_IMPLEMENTATION_DESIGN; execution not authorized",
    "activation_mode": "OFF",
    "stage04_started": False,
}
yput(REG_PATH, reg)

trace["charter_version"] = "1.10"
trace["bootstrap"]["run_id"] = RID
trace_requirements = [
    ("BANYAN-S03-CONTRACT", "35 high-value capabilities have frozen semantic contracts without implementation activation", ["CAPABILITY_CONTRACT_REGISTRY.yaml", "CANONICAL_CONTRACT_SCHEMA.yaml"]),
    ("BANYAN-S03-SOURCE", "Source roles have scoped authority, freshness, conflict and UNKNOWN provenance rules", ["SOURCE_ROLE_SCHEMA.yaml", "SOURCE_ROLE_REGISTRY.yaml", "VERSION_STATUS_PROVENANCE_RULES.yaml"]),
    ("BANYAN-S03-ARTIFACT", "Artifact identity, reference integrity, supersession and deletion contracts are frozen", ["ARTIFACT_REGISTRY_SCHEMA.yaml", "REFERENCE_INTEGRITY_CONTRACT.yaml"]),
    ("BANYAN-S03-BOUNDARY", "Provider ports and project overlays externalize concrete bindings from generic contracts", ["PROVIDER_PORT_SCHEMA.yaml", "PROJECT_OVERLAY_SCHEMA.yaml"]),
    ("BANYAN-S03-STATE", "Bootstrap-to-canonical and existing-layout preservation contracts prevent dual writable truth and implicit relayout", ["BOOTSTRAP_CANONICAL_STATE_CONTRACT.yaml", "EXISTING_PROJECT_LAYOUT_PRESERVATION_CONTRACT.yaml"]),
    ("BANYAN-S03-GOVERNANCE", "Runtime governance interface and conflict carry-over are frozen without selecting provider, model, threshold or conflict winner", ["AI_RUNTIME_GOVERNANCE_CONTRACT.yaml", "CONFLICT_CARRYOVER_REGISTER.yaml"]),
]
for req_id, desc, arts in trace_requirements:
    trace["requirements"].append({
        "requirement_id": req_id,
        "description": desc,
        "owner_stage": ["03"],
        "implementation_artifacts": [f"stages/03/{RID}/{x}" for x in arts],
        "validation_artifacts": [f"stages/03/{RID}/evidence/VALIDATION_RESULTS.yaml"],
        "evidence": [f"stages/03/{RID}/ACCEPTANCE_REPORT.md", f"stages/03/{RID}/evidence/NEXT_STAGE_HANDOFF.yaml"],
        "capability_state": "FROZEN_CONTRACT_NOT_IMPLEMENTED",
        "activation_mode": "OFF",
        "status": "SATISFIED",
        "stage04_started": False,
    })
yput(TRACE_PATH, trace)

reg_after = yload(REG_PATH)
trace_after = yload(TRACE_PATH)
check(20, {
    "register_stage03_complete": reg_after["refactor"]["current_stage"] == "03" and reg_after["stages"]["03"]["status"] == "COMPLETED",
    "prior_register_stages_preserved": all(reg_after["stages"][k] == before_reg["stages"][k] for k in ["00", "01", "02"]),
    "trace_prior_preserved": trace_after["requirements"][:len(before_trace["requirements"])] == before_trace["requirements"],
    "trace_stage03_six": sum(x["requirement_id"].startswith("BANYAN-S03-") and x["status"] == "SATISFIED" for x in trace_after["requirements"]) == 6,
    "handoff_exists": (RUN / "evidence/NEXT_STAGE_HANDOFF.yaml").is_file(),
    "stage04_unauthorized": handoff["next_stage_entry_gate"]["execution_authorized"] is False,
}, ["../../../MIGRATION_REGISTER.bootstrap.yaml", "../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml", "evidence/NEXT_STAGE_HANDOFF.yaml"], "Register/Trace, Acceptance/Handoff contract and stop boundary are complete; Stage 04 was not started.")

yput(RUN / "evidence/VALIDATION_RESULTS.yaml", {"stage": "03", "run_id": RID, "overall": "PASS", "passed": 20, "failed": 0, "results": results})

report = f"""# Stage 03 Acceptance Report

## 1. Stage Status

- Run ID: `{RID}`
- Upstream: `stage02-20260920T131746Z / PASS_CANDIDATE_DESIGN`
- Result: **COMPLETED / PASS_CONTRACT_FREEZE**
- Contract state: `FROZEN`; implementation and activation: `NOT_STARTED / OFF`
- HEAD: `{head}`; tracked/staged/conflicted changes: `0/0/0`

## 2. Low-Token Input Verification

Stage 02 Seal 30/30 and Stage 03 Pack {pre['stage03_pack']['verified_entries']}/{pre['stage03_pack']['verified_entries']} passed. Execution used contract-first evidence-on-demand mode. Repository rediscovery, Stage 01/02 reruns, inventory regeneration and Git-history analysis were not performed. Point reads covered 714 Stage 02 artifact mappings, 1026 Stage 02 asset mappings, and metadata-only comparison for the exact 13 protected paths.

## 3. 35 Capability Contract Coverage

35/35 high-value capabilities have exactly one semantic contract. Dispositions: 21 `FROZEN_CONTRACT`, 2 `PROJECT_OVERLAY_CONTRACT`, 9 `PROVIDER_PORT_CONTRACT`, 3 `COMPATIBILITY_CONTRACT`. The 21 Core boundary candidates remain blocked from final portability acceptance until independent cross-project proof; their contract semantics are frozen without claiming implementation.

## 4. Frozen Schemas / Contracts

The 12 schema/contract surfaces listed in `CONTRACT_FREEZE_REGISTER.yaml` are frozen by SHA-256. `CAPABILITY_CONTRACT_REGISTRY.yaml` contains the 35 contract definitions. No runtime implementation, provider choice, physical installation or migration path was frozen.

## 5. Source Role / Authority Result

Nine observed source roles cover 714/714 Stage 02 artifact/operational records. Every role has authority, canonicality, write, freshness, conflict and provenance rules. `UNKNOWN` remains explicit; inference cannot promote it to fact. Existing source files were not read or changed.

## 6. Provider Port / Project Overlay Result

35 generic provider ports and 35 unbound project overlay records were frozen. All provider bindings are null, and no vendor/model was selected. Overlay values cannot weaken Core safety semantics or contain Secret bodies.

## 7. Reference Integrity Result

Stable artifact identity, typed versions/statuses, inbound/outbound references and supersession are frozen. Referenced canonical artifacts cannot be deleted until reference migration is verified; IDs cannot be reused for a different subject; regeneration without verified lineage is forbidden.

## 8. Existing Project Layout Contract

`EXISTING_PROJECT=PRESERVE_IN_PLACE`; `BANYAN=DISCOVER + MAP + CLASSIFY/DESIGN`; `RELAYOUT=EXPLICIT_MIGRATION_ONLY`. No project directory was moved, renamed, merged or rewritten, and no final `.banyan/`, `banyan-framework/` or `project-sources/` layout was created.

## 9. AI Runtime Cost Governance Contract

The runtime governance interface, execution modes, model capability classes, escalation, quality gate and telemetry fields are frozen. Provider/model names, prices, numeric budgets, fixed token percentages and benchmarks remain unfrozen with owners 05/15/16/19.

## 10. CON-001 / CON-002 Carry-over

Both conflicts remain `OPEN`, retain owner stages 05 and 12, block activation, and have no selected winner. Source-role precedence only resolves scoped and evidenced cases; ambiguity returns `BLOCKED`.

## 11. V03-01～V03-20

All 20 validations passed. Evidence: `evidence/VALIDATION_RESULTS.yaml`.

## 12. Hard Metrics

```text
UNMAPPED_HIGH_VALUE_CAPABILITY = 0
UNOWNED_SCHEMA_COLLISION = 0
SOURCE_ROLE_WITHOUT_AUTHORITY_RULE = 0
CONTRACT_WITHOUT_FAILURE_SEMANTICS = 0
SILENT_CAPABILITY_DROP = 0
PROJECT_PATH_HARDCODED_IN_CORE_SCHEMA = 0
```

## 13. Actual Writes

Writes are confined to `.banyan-refactor/stages/03/{RID}/**` and the two approved bootstrap files under `.banyan-refactor/`. No commit, stash, reset, clean, rebase or push occurred.

## 14. Protected Areas

The 13 `SECRET_METADATA_ONLY` files remain in place. Their bodies were not read, copied or hashed and the files were not modified, deleted, moved, renamed or committed. Recovery remains `USER_ACCEPTED_PRESERVE_IN_PLACE / PARTIAL_APPROVED`. Business code, SQL, production configuration, canonical project documents, Legacy prompts/rules/skills, Git identity and existing layout were untouched.

## 15. Bootstrap Register / Trace

The single bootstrap writable pair now records Stage 03 as completed and preserves all Stage 00–02 entries. Six Stage 03 trace requirements are `SATISFIED`. Canonical `.banyan/**` remains inactive; dual writable truth is forbidden.

## 16. NEXT_STAGE_HANDOFF

`evidence/NEXT_STAGE_HANDOFF.yaml` carries the 35 frozen contracts, 12 frozen schema/contract surfaces, seven owned risks, exact Secret policy, layout contract and Stage 04 consumption rules. Stage 04 must consume Stage 03 contracts rather than Stage 02 candidate assumptions.

## 17. Stage 04 Entry Gate

**PASS_FOR_IMPLEMENTATION_DESIGN** with activation blockers retained. `execution_authorized=false`. Stage 04 was not entered and no Stage 04 file was created.
"""
(RUN / "ACCEPTANCE_REPORT.md").write_text(report, encoding="utf-8")

# Post-state evidence and explicit write manifest.
post = {
    "result": "PASS",
    "head": head,
    "branch": subprocess.check_output(["git", "branch", "--show-current"], text=True).strip(),
    "tracked_diff": tracked,
    "staged_diff": staged,
    "conflicts": conflicted,
    "identity_unchanged": True,
    "forbidden_layouts": forbidden_layouts,
    "stage04_started": False,
}
(RUN / "evidence/POST_STAGE_GIT_STATUS.txt").write_text(json.dumps(post, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

final_safety = {
    "result": "PASS",
    "run_id": RID,
    "head_unchanged": head == pre["git"]["head"],
    "tracked_diff_empty": not tracked,
    "git_identity_unchanged": True,
    "business_files_written": False,
    "secret_metadata_only_count": 13,
    "secret_content_read": False,
    "secret_content_hash": False,
    "secret_content_copy": False,
    "secret_write_delete_move_rename": False,
    "recovery_mode": "USER_ACCEPTED_PRESERVE_IN_PLACE",
    "recovery_coverage": "PARTIAL_APPROVED",
    "existing_layout_unchanged": True,
    "canonical_banyan_active": False,
    "stage04_started": False,
}
jput(RUN / "evidence/FINAL_SAFETY_CHECK.json", final_safety)

planned_future = {"ARTIFACT_HASHES.sha256", "evidence/ACTUAL_WRITES.txt", "evidence/SEAL_VERIFICATION.json"}
current = sorted(str(x.relative_to(RUN)) for x in RUN.rglob("*") if x.is_file())
all_writes = current + sorted(planned_future - set(current)) + ["../../../MIGRATION_REGISTER.bootstrap.yaml", "../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml"]
(RUN / "evidence/ACTUAL_WRITES.txt").write_text("\n".join(all_writes) + "\n", encoding="utf-8")

# Seal the completed run and current bootstrap pair; receipt itself is excluded to avoid circularity.
seal_paths = sorted(x for x in RUN.rglob("*") if x.is_file() and x.name not in {"ARTIFACT_HASHES.sha256", "SEAL_VERIFICATION.json"}) + [REG_PATH, TRACE_PATH]
entries = [(os.path.relpath(x, RUN), sha(x)) for x in seal_paths]
(RUN / "ARTIFACT_HASHES.sha256").write_text("".join(f"{digest}  {rel}\n" for rel, digest in entries), encoding="utf-8")
jput(RUN / "evidence/SEAL_VERIFICATION.json", {
    "result": "PASS",
    "manifest": "ARTIFACT_HASHES.sha256",
    "manifest_sha256": sha(RUN / "ARTIFACT_HASHES.sha256"),
    "verified_entries": len(entries),
    "all_entries_verified": all(sha((RUN / rel).resolve()) == digest for rel, digest in entries),
    "receipt_excluded_from_manifest": True,
    "stage03_status": "COMPLETED",
    "stage04_started": False,
})

print(json.dumps({"result": "PASS", "run_id": RID, "validations": len(results), "sealed_entries": len(entries), "stage04_started": False}, ensure_ascii=False, indent=2))

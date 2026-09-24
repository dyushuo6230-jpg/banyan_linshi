# RP1 Rollback Plan

> **Pack**：`Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0`  
> **Document role**：CONSTRUCTION_EVIDENCE  
> **Runtime / Registry / Semantic authority**：false  
> **Stage**：RP1

Rollback may only undo this Implementation’s newly created files. It must not delete, rewrite, or restore-over any existing R0/R1 authority.

---

## Allowed rollback

Remove only:

1. `banyan-framework/artifacts/`  
   including the nine category directories and the 43 shadow YAML files
2. `banyan-framework/tests/test_rp1_shadow_materialization.py`
3. `banyan-framework/tests/run_rp1_tests.py`
4. `榕树ai改造落地相关文档/Documentation_Packaging/Banyan_RP1_Framework_Artifact_Materialization_Pack_v1.0/03_acceptance/`

After removal, R1 semantic authority is unchanged because it never left `migration_artifacts.yaml`.

---

## Forbidden rollback actions

- Do not modify or restore `banyan-framework/src/banyan/contracts/data/**`
- Do not modify Loader, Validator, CLI, `pyproject.toml`, or policies
- Do not delete or recreate `.banyan`
- Do not delete Legacy v3.1
- Do not delete `.DS_Store`, `control-plane-go/bin/banyan-control`, or other Cleanup / UNKNOWN paths
- Do not use rollback as an authority cutover or as an entry into RP2

---

## Verification after rollback

If rollback is executed, confirm:

```text
banyan-framework/artifacts/                        ABSENT
tests/test_rp1_shadow_materialization.py           ABSENT
tests/run_rp1_tests.py                             ABSENT
03_acceptance/                                     ABSENT or empty
PYTHONPATH=src python3 tests/run_r0_tests.py       PASS
PYTHONPATH=src python3 tests/run_r1_tests.py       PASS
migration_artifacts.yaml                           unchanged
.banyan/**                                         unchanged
```

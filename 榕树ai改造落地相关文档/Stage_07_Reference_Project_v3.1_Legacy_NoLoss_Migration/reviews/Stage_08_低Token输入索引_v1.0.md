# Stage 08 低 Token 输入索引 v1.0

## 1. 默认读取

1. `Stage_07_to_Stage_08_Gate_Review_v1.0.md`
2. Stage 07:
   - `evidence/NEXT_STAGE_HANDOFF.yaml`
   - `V31_GOVERNANCE_COMPATIBILITY_MAP.yaml`
   - `NOLOSS_COVERAGE_REPORT.yaml`
3. Stage 06:
   - Change Workspace / Draft Promotion / Canonical Apply contracts
4. Stage 05:
   - Decision Level
   - Human Confirmation
   - Adaptive Workflow
5. Stage 03:
   - `banyan.contract.requirement_lifecycle.v1`
   - `banyan.contract.uiapplication_scope.v1`
   - `banyan.contract.effective_uicontract.v1`
   - `banyan.contract.uiapproval_gate.v1`
   - `banyan.contract.reference_integrity.v1`
   - `banyan.contract.artifact_status_and_identity.v1`

## 2. Stage 01 / 02 定点能力

仅围绕：

```text
CAP-PRD
CAP-UI_SCOPE
CAP-UI_CONTRACT
CAP-UI_GATE
CAP-IDREF
CAP-TRACE
```

读取对应 Evidence。

## 3. Legacy v3.1 定点读取

只读取支持以下语义的段落：

```text
ENABLE_UI_SPEC_GENERATION
UI_SPEC_ENABLED_APPLICATIONS
G9.5
Partial UI coverage
UI Contract Draft / Approval
Design materials
Visual repair loop
```

不要整份重读所有 v3.1 文档。

## 4. Stage 07 Blockers

只继承：

```text
CON-002
4 historical missing reference targets
R03-* risks
```

Stage 08 不需要重新验证全部 Reference Edge。

## 5. Evidence-on-Demand

```text
PRD_UI_AUTHORITY_AMBIGUITY
UI_SCOPE_COLLISION
UI_SPEC_ENABLEMENT_AMBIGUITY
UI_VERSION_COUPLING_GAP
DESIGN_EVIDENCE_GAP
APPROVAL_GATE_GAP
MISSING_EVIDENCE
```

## 6. Token 花费对象

```text
PRD ↔ UI_SPEC Authority
Application Scope
Enablement
Draft / Approval
Trace
Version / Freshness
Implementation Readiness
```

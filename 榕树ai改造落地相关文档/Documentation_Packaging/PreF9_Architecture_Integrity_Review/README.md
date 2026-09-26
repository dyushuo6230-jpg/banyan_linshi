# Banyan / 榕树 AI — Pre-F9 审计工作包说明 v2.1

## 当前状态

- F1～F8 v1.0：Original Frozen Baseline（原始冻结基线），保持不变。
- Phase 0：已完成。
- Audit Batch 1：正在逐 Patch 审批。
- `B1-PATCH-01`：`HUMAN_APPROVED`
- `B1-PATCH-02`：`HUMAN_APPROVED`
- `B1-PATCH-02-SUP-01`：`HUMAN_APPROVED`
- `B1-PATCH-03`：`HUMAN_APPROVED`
- `B1-PATCH-04`：`HUMAN_APPROVED`
- `B1-PATCH-05`：`HUMAN_APPROVED`
- 未进入 Implementation / RP2 / Authority Cutover / Final Activation / Legacy Retirement。

## 本版本新增

正式补丁：

- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-001_Assignment_Binding_Resolution.md`
- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002_Configuration_Profile.md`
- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-003_StableID_Revision_Version_CurrentEffective.md`
- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-004_Rule_Policy_Module_Engineering_Standard.md`
- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-005_Dynamic_Workflow_Choice_Informed_Decision.md`

## 放置位置

将本包内容放到：

`榕树ai改造落地相关文档/Documentation_Packaging/PreF9_Architecture_Integrity_Review/`

工作区同名文件可用本版本覆盖。

F1～F8 v1.0 原冻结包不得覆盖或修改。

## 当前目录建议

```text
PreF9_Architecture_Integrity_Review/
├── README.md
├── 00_AUDIT_GOVERNANCE_AND_PACKAGING_PROTOCOL.md
├── 01_BATCH01_WORKING_CORRECTION_PROPOSAL.md
├── 02_B1_PATCH01_APPROVAL_DRAFT.md
├── 03_B1_PATCH02_APPROVAL_DRAFT.md
├── 04_B1_PATCH02_SUP01_MAINTENANCE_RESPONSIBILITY_CANDIDATE.md
├── 05_B1_PATCH03_APPROVAL_DRAFT.md
├── 06_B1_PATCH04_APPROVAL_DRAFT.md
├── 10_HUMAN_APPROVED_PATCHES/
│   ├── AUDIT-PATCH-001_Assignment_Binding_Resolution.md
│   ├── AUDIT-PATCH-002_Configuration_Profile.md
│   ├── AUDIT-PATCH-003_StableID_Revision_Version_CurrentEffective.md
│   ├── AUDIT-PATCH-004_Rule_Policy_Module_Engineering_Standard.md
│   └── AUDIT-PATCH-005_Dynamic_Workflow_Choice_Informed_Decision.md
└── 99_NEXT_WINDOW_START_HERE.md
```

`02_B1_PATCH01_APPROVAL_DRAFT.md` 保留作为审批过程记录，但已被正式 Patch 替代，不再作为当前合同。

## 固定治理规则

- Candidate 不得写回 F1～F8 v1.0。
- HUMAN_APPROVED Patch 独立归档。
- 全部审计完成后再整合为 F1～F8 v1.1 Candidate。
- Final Reconciliation / Audit 通过后才形成新的 Freeze Baseline。

- `07_B1_PATCH05_APPROVAL_DRAFT.md` — B1-PATCH-05 完整审批稿

- `10_HUMAN_APPROVED_PATCHES/AUDIT-PATCH-002-SUP-01_Configuration_Profile_Maintenance_Responsibility.md`
- `08_BATCH01_FINAL_CLOSEOUT.md`

# Banyan / 榕树 AI — Pre-F9 审计修订治理与打包协议 v1.1

## 固定三层模型

1. Original Frozen Baseline（原始冻结基线）
   - F1～F8 v1.0 永久保留，不直接修改。

2. Audit Patch Layer（审计补丁层）
   - CANDIDATE：讨论中，不得写回冻结基线。
   - HUMAN_APPROVED：正式补丁，可进入最终整合。

3. Consolidated Freeze Baseline（整合冻结基线）
   - 全部审计完成后，将 HUMAN_APPROVED Patch 整合为 F1～F8 v1.1 Candidate；
   - 做 No-Loss Reconciliation（无损对账）和 Final Audit（最终审计）；
   - 通过后才形成新的 Freeze Baseline。

## 每个正式 Patch 最低内容

- Patch ID
- Status
- Affected Stage
- Problem
- Existing Contract
- Target Contract
- No-Loss Mapping
- Supersession
- Compatibility
- Downstream Impact
- Forbidden Interpretation
- Human Decision
- Integration Target
- Version / Revision Impact

## 审计固定流程

四源对账
→ 系统说明
→ 候选问题
→ 跨阶段验证
→ 修正方案讨论
→ 完整审批稿
→ HUMAN_APPROVED
→ 独立 Patch Markdown
→ 更新 Batch Handover / 99_NEXT_WINDOW_START_HERE

## 固定禁止事项

- Implementation：NOT AUTHORIZED
- RP2：NOT AUTHORIZED
- Authority Cutover：NOT AUTHORIZED
- Final Activation：NOT AUTHORIZED
- Canonical Replacement：NOT AUTHORIZED
- Legacy Retirement：NOT AUTHORIZED

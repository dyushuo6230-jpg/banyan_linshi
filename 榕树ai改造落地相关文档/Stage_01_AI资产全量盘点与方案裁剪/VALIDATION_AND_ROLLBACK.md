# Stage 01 — VALIDATION AND ROLLBACK

## 1. Validation Matrix

| ID | Validation | PASS Condition |
|---|---|---|
| V01-01 | Upstream Gate | Stage 00 actual Handoff/Gate Review 可验证 |
| V01-02 | Baseline Freshness | Drift 已分类，未静默使用失效安全边界 |
| V01-03 | Discovery Coverage | 所有治理/AI 候选 Root 被覆盖或有 reason |
| V01-04 | Secret Safety | Secret 正文未读/未 hash/未复制 |
| V01-05 | Refactor Isolation | `.banyan-refactor` 与施工资料未污染 Legacy Inventory |
| V01-06 | AI Asset Inventory | 资产记录可定位、有类型/分类/evidence |
| V01-07 | Legacy Classification | KEEP/MERGE/SPLIT/REWRITE/REFERENCE/LEGACY/IGNORE 有依据 |
| V01-08 | Capability Discovery | 高价值 Capability 均有 candidate owner/target/action |
| V01-09 | Generated Artifact | Canonical/Derived AI artifact 已区分 |
| V01-10 | Operational Artifact | progress/worklog/handover/runtime 等已盘点 |
| V01-11 | Duplicate/Conflict/Gap | HIGH/CRITICAL 均有 owner candidate / next action |
| V01-12 | Core Candidate Purity | Core Candidate 不把 Reference Project 路径/业务事实当 Core |
| V01-13 | Capability Preservation | Preliminary Matrix 完整 |
| V01-14 | Artifact Migration | Preliminary Matrix 完整，Canonical Artifact 有 source-role candidate |
| V01-15 | Git/Commit Practice | Identity/message/hook/AI commit practice 范围和限制已记录 |
| V01-16 | Unknown Gate | SILENTLY_IGNORED=0, UNSCANNED_ROOT=0, HIGH_RISK_UNCLASSIFIED=0 |
| V01-17 | Write Scope | 除 Control Root/Bootstrap State 外无项目文件修改 |
| V01-18 | Trace / Handoff | Register/Trace 更新，NEXT_STAGE_HANDOFF 完整，Stage 02 Entry Gate 明确 |

## 2. Rollback

Stage 01 正常只写 `.banyan-refactor/**`。

如果 Stage 01 自身失败：

```text
停止
保留 Evidence
不要修改项目文件
将本次 Stage 01 Run 标记 FAIL/BLOCKED
必要时只归档/移除本次 Stage-owned outputs
```

不需要恢复业务文件，因为本阶段不应改业务文件。

如果发现业务文件被 Stage 01 修改：

```text
FAIL
→ 使用 Stage 00 Rollback Point + 当前状态比较
→ 不自动 destructive restore
```

## 3. Exit Metrics

必须：

```text
SILENTLY_IGNORED_ASSET = 0
UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON = 0
HIGH_RISK_UNCLASSIFIED = 0
```

普通 UNCLASSIFIED 可以 >0，但必须有：

```text
risk
candidate_owner_stage
next_stage_plan
```

## 4. Stage 02 Entry Gate

PASS 需要：

- Stage 01 Acceptance PASS；
- Discovery Coverage PASS；
- Preliminary Capability Preservation 完成；
- Preliminary Artifact Migration 完成；
- Core Candidate / Conflict / Gap 可供 Stage 02 消费；
- Existing Project Layout Preservation Contract candidate 已明确写入 Handoff；
- 13 Secret 保护继续继承；
- Bootstrap Trace/Register 可用；
- 没有 Stage 01 越界写。

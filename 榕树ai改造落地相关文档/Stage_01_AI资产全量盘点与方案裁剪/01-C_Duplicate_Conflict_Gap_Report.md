# 01-C：Duplicate / Conflict / Gap Report

## 1. 检测范围

### Duplicate

- exact hash duplicate；
- 同主题多版本；
- symlink 与复制副本；
- 同一规则在多个 editor root 重复；
- generated copy 与 canonical source 混淆。

### Conflict

- 同一语义不同规则；
- status/precedence 不一致；
- 同一编号被不同主题占用；
- 新旧 Prompt 对同一行为要求不同；
- docs/rules/scripts 实际行为冲突；
- Git hook 与 AI commit rule 冲突。

### Gap

- 有引用无目标；
- 有行为无文档；
- 有文档无执行入口；
- 有生成物无来源；
- 有 Operational Artifact 无 owner；
- 重要 Capability 无候选归宿。

## 2. 禁止自动处理

Stage 01 不：

```text
删除 duplicate
合并规则
选择 conflict winner
重挂正式 ID
修正文档
```

只生成 Evidence 和后续处理建议。

## 3. 严重度

建议：

```text
CRITICAL
HIGH
MEDIUM
LOW
INFO
```

`HIGH/CRITICAL` 未解释时不能退出 Stage 01。

## 4. 输出

`CONFLICT_GAP_REPORT.yaml`

每项至少：

```yaml
issue_id:
type:
severity:
assets:
description:
evidence_refs:
candidate_owner_stage:
recommended_next_action:
blocking:
```

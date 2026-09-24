# R1 完成后用户检查清单

你不用逐文件检查。

请发给 ChatGPT：

1. `R1_ARTIFACT_MIGRATION_ACCEPTANCE_REPORT.md`
2. `R1_ARTIFACT_MIGRATION_MATRIX.yaml`
3. `R1_NEW_PROPOSAL_REGISTER.yaml`
4. Codex 最终总结
5. 若有 Human Decisions Required，一并发

重点关注：

## 1. 有没有凭空新造语义
如果 `NEW_PROPOSAL_REGISTER` 非空，需要单独决策。

## 2. 有没有把 Capability 当 Skill
不允许自动 35 Capability = 35 Skill。

## 3. 有没有把人员职位做成 Banyan Role
不允许。

## 4. 有没有把 State 混成一个总 enum
不允许。

## 5. 有没有为了省 Token 只保留摘要
不允许。

## 6. 有没有越界做 R2/R3
如果开始实现 Workflow executor、自然语言编排、Canonical Apply、Project Instance 完整绑定，则越界。

# Stage 14 Execution Runbook — Policy Freeze / Shadow Evaluation

1. 读取 Gate / Low Token Index。
2. 加载 Stage13 Governance Requirements + Stage05 Decision/Commit contracts。
3. 冻结 Risk / Permission / Authorization。
4. 冻结 Protected / Secret / Freshness / Rollback gates。
5. 冻结 Git Identity / Worktree / Commit Safety。
6. 用 Shadow Action Cases 验证 ALLOW/BLOCK/NEEDS_INPUT，不执行动作。
7. 生成 Stage15 Runtime Enforcement Handoff。
8. V14-01..V14-26。
9. Acceptance + Handoff。
10. Bootstrap update。
11. STOP，不进入 Stage15。

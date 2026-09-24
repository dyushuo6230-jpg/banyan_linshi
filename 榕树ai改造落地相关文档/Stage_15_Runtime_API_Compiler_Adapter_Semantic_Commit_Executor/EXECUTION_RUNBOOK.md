# Stage 15 Execution Runbook

1. 读取 Gate / Low Token Index / Stage14 Handoff。
2. 创建 Generic `banyan-framework/` Source Candidate。
3. 实现 Policy Compiler / Runtime API / CLI。
4. 实现 Generic Git Adapter / Planner / Executor。
5. 实现 Trace / Audit。
6. Unit Tests。
7. 创建 isolated fixture。
8. 在 fixture 内执行真实 Git integration tests。
9. 对当前项目只执行 read-only inspect + dry-run。
10. 确认当前项目 HEAD/index 未变化。
11. 生成 Stage16 API Handoff。
12. V15-01..V15-28。
13. Acceptance + NEXT_STAGE_HANDOFF。
14. Bootstrap update。
15. STOP，不进入 Stage16。

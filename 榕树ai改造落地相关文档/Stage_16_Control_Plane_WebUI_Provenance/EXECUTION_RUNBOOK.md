# Stage 16 Execution Runbook

1. 读取 Gate / Low Token Index / Stage15 API Handoff。
2. 在 `banyan-framework/` 内实现 generic Control Plane。
3. 只通过 Runtime API 获取状态和执行 preflight/dry-run。
4. 实现 local-only Web server。
5. 实现 Dashboard / Gate / Plan / Trace / Provenance。
6. 实现 Activation Readiness，仅展示，不激活。
7. 跑 unit/API/UI smoke tests。
8. 对当前项目验证 HEAD/index/staged 未变化。
9. 输出 Stage17 Cursor Pilot Handoff。
10. V16-01..V16-26。
11. Acceptance + Bootstrap。
12. STOP，不进入 Stage17。

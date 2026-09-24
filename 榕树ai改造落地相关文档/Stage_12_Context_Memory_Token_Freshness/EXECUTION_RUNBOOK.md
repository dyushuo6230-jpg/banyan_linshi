# Stage 12 Execution Runbook — Query First

1. 读取 Gate / Low Token Index。
2. 使用 Stage 11 Query Surface 获取 current/history/freshness/reference evidence。
3. 冻结 Context Selection / Recovery / Memory contracts。
4. 定点处理 CON-002。
5. 定点处理 4 historical references。
6. 冻结 Token Budget / Compaction / Cache。
7. 生成 Stage13 Query Handoff。
8. V12-01..V12-24。
9. Acceptance + Handoff。
10. Bootstrap update。
11. STOP，不进入 Stage 13。

# Stage 11 Execution Runbook — Structured Input First

1. 读取 Gate / Low Token Index。
2. 加载 Structured Registry / Matrix / Handoff。
3. 构建 normalized import records。
4. 创建 `shadow/banyan_index.sqlite`。
5. 导入结构化记录。
6. 建立 reference / trace / history / projection relations。
7. 保留 4 条 unresolved historical references。
8. 保持 2 条 regex literal = NOT_A_REFERENCE。
9. 运行 integrity/query/count checks。
10. 做 isolated rebuild proof。
11. 输出 Stage 12 Query Surface。
12. V11-01..V11-24。
13. Acceptance + Handoff。
14. 更新 Bootstrap。
15. STOP，不进入 Stage 12。

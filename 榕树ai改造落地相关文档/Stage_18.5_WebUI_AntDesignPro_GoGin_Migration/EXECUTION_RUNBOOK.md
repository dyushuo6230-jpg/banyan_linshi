# Stage 18.5 Execution Runbook

1. 读取 Gate / Low Token Index。
2. 定点盘点当前 WebUI / Control Plane / Runtime Boundary。
3. 生成并冻结 `ADR_WEBUI_CONTROL_PLANE_STACK.yaml`。
4. 建 Ant Design Pro Simple 精简基线。
5. 生成 Feature Equivalence Matrix。
6. 逐项迁移 Banyan WebUI。
7. 实现 Go/Gin Transport。
8. 实现单一 Runtime Bridge，不重写 Permission。
9. 构建 frontend static assets + hashes。
10. 使用 Go embed 打入 Control Plane binary。
11. 跑 API / SPA / local-bind / security tests。
12. 跑三 Adapter Regression。
13. 验证 Pilot `.banyan` fingerprint。
14. 验证 current project Git fingerprint。
15. 输出 Stage19 RC Handoff。
16. V18_5-01..V18_5-30。
17. Acceptance / Bootstrap。
18. STOP，不进入 Stage19。

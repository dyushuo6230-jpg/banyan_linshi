请读取 Stage 18 Delivery Pack 并执行 Stage 18。

目标：
完成多编辑器 AI Adapter 兼容性验证。

必须遵守：
1. Adapter 只是接入层。
2. 所有能力通过 Runtime API。
3. 不允许 Adapter 自建权限。
4. 不允许修改 Canonical。
5. 不允许 Git mutation 绕过策略。
6. 不重新扫描全仓。

验证：
- Cursor Adapter
- Codex Adapter
- Generic Adapter

完成后停止，不进入 Stage 19。

输出：
- ACCEPTANCE_REPORT.md
- NEXT_STAGE_HANDOFF.yaml
- ADAPTER_VALIDATION_RESULT.yaml

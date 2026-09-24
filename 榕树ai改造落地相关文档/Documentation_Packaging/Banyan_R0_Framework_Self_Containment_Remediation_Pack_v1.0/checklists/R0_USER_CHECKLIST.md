# R0 完成后你需要做什么

Codex 完成后，不需要你人工逐文件检查。

请把以下内容发回 ChatGPT：

1. Codex 最终执行总结
2. `R0_FRAMEWORK_SELF_CONTAINMENT_ACCEPTANCE_REPORT.md`
3. Codex 输出的 changed files 清单
4. 最好把新增/修改的以下目录打包：
   - Framework contract / registry / schema 目录
   - `src/banyan/` 中 R0 新增 loader/validator
   - R0 新增 tests
5. 如果报告里有 `Human Decisions Required`，一并发来

## 你只需要人工关注三件事

### A. 有没有项目业务内容进 Core
如果看到业务专有模块、业务规则、Reference Project 绝对路径进入 `banyan-framework/`，立即停止验收。

### B. 有没有越界开始做 R1/R2
如果 Codex开始实现：
- 自动 Workflow
- Skill executor
- Role authorization
- Canonical Apply
- WebUI Help
说明越界。

### C. 有没有动 `.banyan`
R0 默认 `.banyan` 只读。

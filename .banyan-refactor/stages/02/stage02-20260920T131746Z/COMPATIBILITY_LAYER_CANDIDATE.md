# Compatibility Layer Candidate

三项主边界：`CAP-EDITOR`、`CAP-COMMIT`、`CAP-MERGE`，见 `COMPATIBILITY_CANDIDATES.yaml`。旧 v3.1 超级提示词的来源投放、PRD、决策、版本和工作流仍是多项能力的现行实现来源；先做只读解释与行为回归，不能在 Stage 02 直接拆改旧文或关闭入口。

Cursor 规则与 symlink skill 是既有入口，兼容映射要保留覆盖顺序及项目规则。Nested Husky/commitlint 的存在不证明根提交钩子生效，已发现缺少 `lint:lint-staged` 脚本；不得自动安装、执行或调整 Git Identity。旧合码指导包含特定分支、reset/force 语境，仅作历史参考，不能转成 Runtime 权限。

兼容层的读入结果必须注明来源、版本、适用项目和是否过期。它不能成为另一个项目真源，也不能悄悄把旧提示词视为未来通用 Contract。Stage 07/17 做兼容实施与回归；Stage 19 做 No-Loss 终验。Stage 02 仅记录约束和候选接口。

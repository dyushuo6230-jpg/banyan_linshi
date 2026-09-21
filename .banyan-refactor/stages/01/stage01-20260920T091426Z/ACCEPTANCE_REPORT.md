# Stage 01 实际验收报告

1. **Stage Status：COMPLETED / PASS**。沿用 `stage01-20260920T091426Z`，Resume Case A，从最后已验证的 Step 01.1 之后继续 Step 01.2；未重启 Stage 00/01，未创建第二个 Run，未进入 Stage 02。最终状态以 `evidence/VALIDATION_RESULTS.yaml`、Bootstrap Register 及封存验证共同确认为准。

2. **Upstream / Baseline Freshness**：当前仓库 `/Users/mac/MYCODES/AICODE/x_shop_server/x_shop_server`；HEAD `9a52349e6bcb6ee44e3039dd87ede56e3e0a3ec7`，分支 `feature/huanpipro`。恢复时 Pack 28 项、上游封存 58 项、5,835 项安全哈希与 69 项敏感候选元数据通过。Stage 00 仍为已验收的 PARTIAL_APPROVED 基线。最终复核 5,834 项内容哈希，另将 tunnel 脚本加严为 metadata-only，共 70 项元数据路径；13 份本地配置仍不读正文。

   恢复后的末次复核发现 `.banyan-refactor.zip` 已不在原位。本次执行没有写入、移动或删除它；变化来源未确认。该文件原已排除为上游施工证据副本，原始 Stage 00 Evidence 与两个归档仍完整，因此登记为 SAFE_DISCOVERY_DRIFT 后继续。不是工作区完全无变化；不重建该压缩副本。证据：`evidence/EXTERNAL_ARCHIVE_DRIFT.json`、`evidence/FINAL_SAFETY_CHECK.json`。

3. **Discovery Coverage**：路径快照 100,115 项，4,766 份全文文本经特征与引用检索；逐路径保留内容/元数据/排除理由。二进制只作路径、登记和允许的哈希检查，不声称做过视觉验收。全仓路径、非种子目录、17 个 ignored-governed 资产、相关未跟踪文件、编辑器/工具/治理/发布/运行根均有记录。历史扫描覆盖本地全部可达 477 个提交及相关治理删除记录（10 次事件、5 个唯一历史路径）。三个硬指标全部为 0，见 `DISCOVERY_COVERAGE_REPORT.yaml` 及计算定义。

4. **AI Asset Inventory Summary**：1026 项资产，包括当前文件/符号链接和历史路径引用。文件级类型、分类理由、候选阶段、来源与 Evidence 可定位；`.banyan-refactor/**`、施工资料和压缩副本不混入 Legacy 总量。该数字不是“1,026 份均由 AI 创作”的断言。

5. **Legacy Capability Summary**：35 项高价值行为能力，逐项有输入、输出、门禁、失败语义、来源行号及候选 owner/target/action。覆盖需求与决策、版本/编号/引用保护、Parallel Draft、36A 收口、测试完整性、上下文续做、进度交接、发布、UI 治理与视觉修复、编辑器、提交实践及 AnyDesign 工具能力。

6. **Generated / Operational Artifact Summary**：425 项正式/派生产物候选，其中 Canonical 330、Derived 95；另有 289 项运行记录。所有 Canonical 候选保留原位并 MAP + INDEX，记录状态与风险，不因位于正式目录而自动批准。每份文件的 AI 作者身份及完整生成链未被证明；派生物不可擅自假定可字节重建。运行记录保留 in_progress、用户叫停/回退等真实状态，不混同验收成功。这些视图与 Asset Inventory 有交叉，不能直接相加当文件总数。

7. **Duplicate / Conflict / Gap Summary**：31 项记录（INFO 23、LOW 1、MEDIUM 5、HIGH 2、CRITICAL 0）。包含 22 组精确相同内容及符号链接别名说明。两项 HIGH：通用 IDP 与项目覆盖规则差异、项目入口/指南与看板版本进度陈旧矛盾，均有候选负责阶段和下一步，当前只登记不裁决。Nested pre-commit 缺目标脚本、4 条实际缺目标 Markdown 引用、派生来源重建不确定等分别登记；正则源码中的伪链接未当作坏链接。

8. **Core / Project / Provider / Compatibility Candidates**：Generic Core 21、Project-only 2、Provider 9、Compatibility 3；没有执行退休/删除候选。每项记录项目依赖、硬编码路径、业务术语、抽象要求及跨项目证据限制；尚未证明跨项目运行兼容。未冻结 Source Role、Schema、最终 Owner、Commit Policy 或目标目录。

9. **Preliminary No-Loss Coverage**：能力 35/35 映射；产物 425/425 映射；运行记录 289/289 原位索引映射。SILENTLY_IGNORED_ASSET=0、UNSCANNED_GOVERNANCE_ROOT_WITHOUT_REASON=0、HIGH_RISK_UNCLASSIFIED=0。当前 UNCLASSIFIED 资产为 0；来源作者、可重建性、引用有效版本等问题已作为明确字段/风险登记，不以 0 未分类掩盖它们。

10. **Git Identity / Commit Practice**：保持现有 `user.name/user.email`；477 个可达提交、16 组精确 Author 身份、13 个 Author/Committer 差异。Conventional-like subject 64，其它 413；Merge 116；164 个 Co-authored-by 尾注。AI 标记只是提交信息中的归属声明，不证明物理操作者。根 hooksPath 未设置，仅有 sample hooks；后台子项目存在 Husky/commitlint 文件，但 pre-commit 指向缺失脚本。未运行 Hook、未合并 Identity、未冻结提交政策、未 commit。真实 trailing block 统计见 semantic_review 和 `evidence/GIT_TRAILER_PARSE.json`，不能把初始任意行键计数当正式尾注。

11. **V01-01～V01-18**：全部 PASS。逐项断言、实际 Evidence、限定说明见 `evidence/VALIDATION_RESULTS.yaml`。这里验证的是 Stage 01 盘点和保护契约；未执行业务测试、设计工具、迁移、部署或运行视觉循环。预验收与最终验收分开保留；脚本一次语法错误及压缩副本变化造成的中止不被当作验收成功，修正/续做过程记录在执行证据与本报告中。

12. **Actual Writes**：本 Run 下新增和完成的 Inventory、Report、Matrix、脚本、Checkpoint 引用、Validation、Acceptance/Handoff 与哈希封存；更新控制根的两份 Bootstrap YAML。完整列表见 `evidence/ACTUAL_WRITES.txt`。中断前 10 份 Evidence 与 2 份快照逐字未改；初始自动盘点草稿另存，语义复核修订有哈希记录。所有写入由 Stage 01 授权范围约束。

13. **Protected Areas Confirmed Untouched**：现有业务代码、SQL、生产配置、正式 docs/project、docs/governance、docs/temp、tools、.cursor、施工资料均无本次写入；HEAD/index/identity 不变。13 份本地环境配置：**未读正文、未复制正文、未 Hash 正文、未修改、未删除、未移动、未重命名、未提交 Git**。用户明确接受没有独立 Banyan Backup；恢复为 USER_ACCEPTED_PRESERVE_IN_PLACE / PARTIAL_APPROVED，绝非 COMPLETE。后续 Stage 继续只读元数据、禁止写/删/复制/提交。其它 Secret 不获豁免。敏感正文相等性未经哈希，不作相等断言；依赖/构建/缓存排除区不声称逐字校验。

14. **Open Risks / Questions**：13 份配置仅原位保存的恢复风险；派生物作者与生成链不确定；规则覆盖/陈旧入口需后续阶段解决；部分符号引用需按有效版本与主题复核；Hook 生效/命令缺失待处理；压缩副本缺失来源未知；本地控制产物未提交、不是独立离线备份。均不授权本阶段修正文档、运行旧合码/reset 指导或删除任何文件。

15. **Bootstrap Register / Trace**：唯一可写真源仍为 `.banyan-refactor/MIGRATION_REGISTER.bootstrap.yaml` 与 `BANYAN_REFACTOR_TRACE.bootstrap.yaml`，current_stage=01，Stage 00 原条目完整保留，追加 Stage 01 实际产物与验证。Stage 00 封存中两份共享文件的历史哈希通过本 Run 的只读 snapshot 验证，不能要求更新后的共享文件还等于旧哈希。`evidence/BOOTSTRAP_LINEAGE.json` 记录 source/target hash、run 和时间。未来 canonical 迁移仍须 source hash/run → target hash → validation → bootstrap只读归档；本阶段未创建正式 `.banyan`。

16. **NEXT_STAGE_HANDOFF**：实际 `evidence/NEXT_STAGE_HANDOFF.yaml` 包含全部 Inventory/Report/Matrix、Evidence、开放问题、五类边界候选结论、13 Secret 约束、隔离语义及 Existing Project Layout Preservation Contract candidate：EXISTING_PROJECT → PRESERVE_IN_PLACE；BANYAN → DISCOVER + MAP + CLASSIFY；RELAYOUT → EXPLICIT_MIGRATION_ONLY。

17. **Stage 02 Entry Gate：PASS**。表示交接条件满足，**不表示已获 Stage 02 执行授权**。本次停止于 Stage 01；未创建 Stage 02 Run，未创建正式 `.banyan/`、`banyan-framework/` 或统一 `project-sources/`，未执行 Legacy Migration。

封存范围见 `ARTIFACT_HASHES.sha256`；独立回读结果见 `evidence/SEAL_VERIFICATION.json`。后者是封存后的验证回执，不纳入自身或 manifest 的循环哈希。

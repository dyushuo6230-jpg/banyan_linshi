# Stage 00 实际验收报告

1. Stage Status: COMPLETED。Validation: PASS。恢复覆盖始终为 PARTIAL_APPROVED，绝非 COMPLETE。

2. Repository Baseline: `/Users/mac/MYCODES/AICODE/x_shop_server/x_shop_server`；Branch `feature/huanpipro`；HEAD `9a52349e6bcb6ee44e3039dd87ede56e3e0a3ec7`。单一 Git 仓库、多应用 monorepo；单 worktree；无 submodule、无非依赖范围 nested repo；无 sparse checkout；LFS CLI 不可用，但 Git 属性中无 LFS 管理文件。未解决 Git operation/conflict = 0。原始 staged/unstaged = 0；untracked = 21。

3. Discovery Scope: 原始 100010 个 Git 可枚举路径均有安全分类。正文允许 SCAN、METADATA_ONLY、EXCLUDE_WITH_REASON 分开记录。源文件 SHA-256 5835 项。依赖/构建/日志/OS/IDE 排除均有理由。未执行 Stage 01 AI 能力语义盘点。AUDIT/ARCHIVE 未全文加载，仅做完整性字节处理及安全备份。

4. Protected Paths: 仅 `.banyan-refactor/**` 允许本阶段生成控制产物。业务代码、SQL、配置、正式 PRD/DEC/ADR/CR/UI_SPEC/Guide、Legacy Prompt/Rules/Skills、现有编辑器入口默认禁止修改。正式 `.banyan/migrations/**` 为 CONDITIONAL_WRITE_LATER，当前不存在。

5. Checkpoint Coverage: PARTIAL_APPROVED。21 个非敏感 untracked 文件、17 个 ignored-but-governed 文件已归档并逐成员验证 SHA-256；其中 ignored 包括2份治理文档和15张本地资源图片。无 tracked 修改，因此没有伪造空 patch。用户主动复制的榕树施工资料保留原位并安全备份，不被描述为历史开发现场。

## Secret 明确例外

用户明确批准 `USER-STAGE00-SECRET-EXCEPTION-001`，仅限列出的13份 ignored 本地环境配置：

- `nunu-go-api/config/admin/local.yml`
- `nunu-go-api/config/admin/test.yml`
- `nunu-go-api/config/h5-online/local.yml`
- `nunu-go-api/config/h5/local.yml`
- `nunu-go-api/config/h5/test.yml`
- `nunu-go-api/config/home/local.yml`
- `nunu-go-api/config/mall-online/local.yml`
- `nunu-go-api/config/mall-online/prod.yml`
- `nunu-go-api/config/mall-online/test.yml`
- `nunu-go-api/config/mall/local.yml`
- `nunu-go-api/config/mall/test.yml`
- `nunu-go-api/config/merchant/local.yml`
- `nunu-go-api/config/merchant/test.yml`

这13份文件：未读取正文、未复制正文、未 Hash Secret 正文、未修改、未删除、未移动、未重命名、未纳入 Git 提交。用户明确接受其没有独立 Banyan Backup，只保留当前本地环境的恢复风险。`recovery_mode = USER_ACCEPTED_PRESERVE_IN_PLACE`。后续所有 Stage 必须继续仅访问 metadata，禁止写入/删除/移动/重命名/内容复制/内容哈希/提交；本次批准不放宽其它 Secret 或 Protected Path。

潜在敏感文件共69项（包括保守按路径分类的模板/源码候选），其余为无修改的 tracked 文件，仅记录 Git object/index 引用，不读取其内容，也不将其套用本次13路径豁免。metadata未变不是Secret正文哈希一致的证明；本次只声明无写入操作与lstat一致。

6. Actual Artifacts（SHA-256；完整列表与封存哈希见 ARTIFACT_HASHES.sha256）：

- `BASELINE_MANIFEST.yaml` — `3928acbd5d2e7c7323a2044543edb34c084b051faed1dc750cf61b7d0a989721`
- `PROTECTED_PATHS_MANIFEST.yaml` — `99a7e35598b63becac04548e6ee7417c860ff9a5a7244dab0dc1dcdc7632e73d`
- `DISCOVERY_SCOPE_BASELINE.yaml` — `a10f3d05f24ebf3712f6dd46f4b5c8adcbbd1e9331c456c524ea9cb90f737067`
- `CHECKPOINT_RECORD.yaml` — `973be81a863508b549dd20b7d39c391407b29f46aed74603d9c669d60cd8d0c7`
- `FILE_HASHES.sha256` — `9b9bf001a03004f9cbfe55b6c077b153a001e014fb719e44ee772f150398a930`
- `PRE_STAGE_GIT_STATUS.txt` — `cb9f47cc0f2dec1ae02ecb47032c8fccc1c792c1d1cedfcc908a018ddc0f769d`
- `POST_STAGE_GIT_STATUS.txt` — `f2f77bbbe837513065a1082f4047a410bc24ce16446a84e94b897fba78c05293`
- `../../../MIGRATION_REGISTER.bootstrap.yaml` — `3080a90fb8b11a594600de3d513ad6a9b4ff60a7bbde9a19d7b6bd5c24b763ee`
- `../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml` — `4fe9d5da1bd26d53570af635f8c5be4794452d5676bdbce7e7966a099a5bee21`
- `checkpoint/untracked.tar` — `d321195de0a4ab9b82157fd439c16fbb8dbe3b6c4ccf04ac2e7dc7363a680aa8`
- `checkpoint/ignored-governed.tar` — `0e4aa8b0838762192f7a2969b2d357d9d6f88024c2d8a4c91aad5a803354aada`

7. V00-01～V00-15：

- **V00-01: PASS** — Monorepo boundary explicit; dependencies/generated roots excluded with reasons; symlinks not followed. Evidence: `evidence/repo_root.txt`, `evidence/worktree.txt`, `evidence/submodule.txt`, `evidence/TOPOLOGY.json`
- **V00-02: PASS** — Original branch/HEAD/status retained; no tracked diff; 21 original untracked files. Evidence: `BASELINE_MANIFEST.yaml`, `PRE_STAGE_GIT_STATUS.txt`, `evidence/resume-git-evidence.json`
- **V00-03: PASS** — No unresolved merge/rebase/cherry-pick/revert/sequencer/conflict. Evidence: `evidence/git_operation.txt`, `evidence/SAFETY_COMPARISON.json`
- **V00-04: PASS** — 100010 paths classified; per-file records override root defaults; no Stage 01 semantic inventory. Evidence: `DISCOVERY_SCOPE_BASELINE.yaml`, `evidence/FILE_INVENTORY.jsonl`, `evidence/EXCLUSIONS.json`
- **V00-05: PASS** — Ignored governance docs and local assets retained; ignored secret exception kept separate. Evidence: `evidence/IGNORED_GOVERNED.json`, `checkpoint/ignored-governed.tar`
- **V00-06: PASS** — Only bootstrap root writable; 13 exact secret paths remain metadata-only through future stages; no waiver for others. Evidence: `PROTECTED_PATHS_MANIFEST.yaml`, `evidence/USER_APPROVAL.json`
- **V00-07: PASS** — 69 conservatively classified potential-secret paths: no content I/O; 13 ignored exceptions, remaining clean tracked references. Secret content equality is not claimed. Evidence: `evidence/SECRET_METADATA.json`, `evidence/stage00_execution.py`, `evidence/SAFETY_COMPARISON.json`
- **V00-08: PASS** — 5835 regular-file SHA-256 values verified; symlink text and secret metadata are recorded separately; exclusions explained. Evidence: `FILE_HASHES.sha256`, `evidence/FILE_INVENTORY.jsonl`, `evidence/HASH_SCOPE_REPORT.json`, `evidence/SAFETY_COMPARISON.json`
- **V00-09: PASS** — PASS under explicit user-approved partial recovery exception ONLY; 13 secret contents have NO independent backup and cannot be restored from checkpoint. Not COMPLETE. Evidence: `CHECKPOINT_RECORD.yaml`, `evidence/USER_APPROVAL.json`, `evidence/CHECKPOINT_INTEGRITY.json`
- **V00-10: PASS** — No tracked binary changes; no patch required. Non-secret untracked/ignored binary assets verified inside tar. Evidence: `evidence/status.z`, `evidence/index.z`, `evidence/CHECKPOINT_INTEGRITY.json`
- **V00-11: PASS** — All 21 relevant untracked files safely backed up, including preserved user-supplied construction materials. Evidence: `evidence/untracked.z`, `checkpoint/untracked.tar`, `evidence/CHECKPOINT_INTEGRITY.json`
- **V00-12: PASS** — Outside-control Git status, HEAD, index, identity unchanged; managed hashes and secret lstat metadata unchanged; no automatic commit or destructive operations. Evidence: `PRE_STAGE_GIT_STATUS.txt`, `POST_STAGE_GIT_STATUS.txt`, `evidence/SAFETY_COMPARISON.json`
- **V00-13: PASS** — Actual YAML documents parse; mandatory baseline links and checkpoint member paths exist; future canonical paths are explicitly future, absent. Evidence: `evidence/MANIFEST_PARSE.json`
- **V00-14: PASS** — Single bootstrap writable Register/Trace pair; source/run lineage → canonical target hash → validation → bootstrap read-only archive obligation recorded. Evidence: `../../../MIGRATION_REGISTER.bootstrap.yaml`, `../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml`, `evidence/SAFETY_COMPARISON.json`
- **V00-15: PASS** — Complete handoff with PARTIAL_APPROVED risk and exact scope; Stage 01 permission gate is distinct from execution authorization. Evidence: `ACCEPTANCE_REPORT.md`, `evidence/NEXT_STAGE_HANDOFF.yaml`

8. Open Risks / Blockers: 阻塞已解除；R00-SECRET-001 为用户接受的剩余风险。13份配置没有独立内容备份，原位文件丢失时不能靠本 Checkpoint 恢复。Stage 00 只验证归档内容与路径完整性，未在真实工作区执行恢复演练。控制产物尚未提交Git，也不是独立离线备份；临时原始捕获可能被系统清理，已复制证据至控制目录。后续阶段开始前应验证基线新鲜度。

9. 实际修改文件: 原项目既有文件零修改。仅新建 `.banyan-refactor/` 下控制文件、检查点、Evidence 与本报告，以及系统临时目录中的执行脚本/证据。完整仓库内写入路径见 evidence/ACTUAL_WRITES.txt；脚本和原始临时路径见 evidence/stage00_execution.py 与 evidence/precheck.json。

10. 重要保护区未修改: nunu-go-api、三套go-uni-app、docs/project、docs/governance、docs/temp、.cursor、tools、榕树施工资料、.gitignore、Git HEAD/index/identity。受管非敏感正文哈希复核通过；敏感路径只校验元数据；生成物/依赖/日志排除范围不宣称正文逐字验证。未commit/stash/tag/push/reset/clean/restore；未初始化.banyan。

11. Rollback Point: `CHECKPOINT-stage00-precheck-20260920T083254Z`。HEAD + 原始未提交文件归档 + ignored受管归档 + 明确排除/批准例外；恢复覆盖 PARTIAL_APPROVED。先比较最新现场并保留后续用户工作，再执行经授权的最小恢复；禁止破坏性自动恢复。详见 checkpoint/RESTORE_INSTRUCTIONS.md 和 evidence/ROLLBACK_POINT.yaml。

12. Bootstrap Register / Trace: 唯一可写真源在控制根目录的 MIGRATION_REGISTER.bootstrap.yaml / BANYAN_REFACTOR_TRACE.bootstrap.yaml；bootstrap_only=true；activation=OFF。未来必须捕获 source hash/run lineage → canonical .banyan/migrations/* → target hash/validation → bootstrap只读归档/reference；禁止双可写真源。未执行未来迁移。

## 13. NEXT_STAGE_HANDOFF

upstream_stage: '00'
run_id: stage00-precheck-20260920T083254Z
acceptance_result: PASS_WITH_USER_APPROVED_PARTIAL_RECOVERY
actual_artifacts_to_consume:
- BASELINE_MANIFEST.yaml
- PROTECTED_PATHS_MANIFEST.yaml
- DISCOVERY_SCOPE_BASELINE.yaml
- CHECKPOINT_RECORD.yaml
- FILE_HASHES.sha256
- PRE_STAGE_GIT_STATUS.txt
- POST_STAGE_GIT_STATUS.txt
- ../../../MIGRATION_REGISTER.bootstrap.yaml
- ../../../BANYAN_REFACTOR_TRACE.bootstrap.yaml
evidence_to_trust:
- evidence/pack-resume-check.json
- evidence/FILE_INVENTORY.jsonl
- evidence/USER_APPROVAL.json
- evidence/CHECKPOINT_INTEGRITY.json
- evidence/VALIDATION_RESULTS.yaml
- evidence/SAFETY_COMPARISON.json
unresolved_risks:
- id: R00-SECRET-001
  status: USER_ACCEPTED
  description: Only the 13 explicitly approved ignored local environment configurations
    have no independent Banyan content backup. If lost, the Stage 00 checkpoint cannot
    restore their contents.
  scope:
  - nunu-go-api/config/admin/local.yml
  - nunu-go-api/config/admin/test.yml
  - nunu-go-api/config/h5-online/local.yml
  - nunu-go-api/config/h5/local.yml
  - nunu-go-api/config/h5/test.yml
  - nunu-go-api/config/home/local.yml
  - nunu-go-api/config/mall-online/local.yml
  - nunu-go-api/config/mall-online/prod.yml
  - nunu-go-api/config/mall-online/test.yml
  - nunu-go-api/config/mall/local.yml
  - nunu-go-api/config/mall/test.yml
  - nunu-go-api/config/merchant/local.yml
  - nunu-go-api/config/merchant/test.yml
protected_allowed_scope_changes:
  new_write_scope: .banyan-refactor/** only
  secret_policy_unchanged: true
  approved_secret_recovery_exception_only:
  - nunu-go-api/config/admin/local.yml
  - nunu-go-api/config/admin/test.yml
  - nunu-go-api/config/h5-online/local.yml
  - nunu-go-api/config/h5/local.yml
  - nunu-go-api/config/h5/test.yml
  - nunu-go-api/config/home/local.yml
  - nunu-go-api/config/mall-online/local.yml
  - nunu-go-api/config/mall-online/prod.yml
  - nunu-go-api/config/mall-online/test.yml
  - nunu-go-api/config/mall/local.yml
  - nunu-go-api/config/mall/test.yml
  - nunu-go-api/config/merchant/local.yml
  - nunu-go-api/config/merchant/test.yml
  other_protected_paths_remain_read_only: true
  stage01_execution_authorized: false
rollback_point:
  id: CHECKPOINT-stage00-precheck-20260920T083254Z
  path: CHECKPOINT_RECORD.yaml
  coverage: PARTIAL_APPROVED
  instructions: checkpoint/RESTORE_INSTRUCTIONS.md
stage01_entry_gate:
  result: PASS
  qualification: Only acceptable under exact user-approved 13-path recovery exception;
    not COMPLETE
  execution_requires_new_user_instruction: true

14. Stage 01 Entry Gate: PASS，依据用户明确批准的13路径 PARTIAL_APPROVED 例外，不声称 COMPLETE。只表示安全交棒条件满足，未授权或执行 Stage 01。本次停止于 Stage 00，等待下一步指令。

## Execution lineage and authority

Run ID: `stage00-precheck-20260920T083254Z`；Executor: Codex TRANSFORMATION_EXECUTOR。Pack/Charter均为1.9.1；15项Pack校验通过。沿用仓库外原始precheck捕获，复核原始HEAD/index/status后从同一Block Point续做，未重启Stage 00。历史BLOCKED报告保留为Evidence，不再表示当前状态。用户明确的PARTIAL_APPROVED授权适用于本次Exit Gate；不修改Pack或上位资料正文。

Acceptance generated after actual checkpoint and primary validation; final handoff/report validation and sealing follow. Final results in evidence/VALIDATION_RESULTS.yaml and evidence/FINAL_VERIFICATION.json.

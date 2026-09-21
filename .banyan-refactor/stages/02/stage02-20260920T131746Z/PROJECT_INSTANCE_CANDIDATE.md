# Project Instance Candidate

主边界 2 项：`CAP-PORT`（项目端口及前后端绑定）、`CAP-SQL`（当前增量 SQL 交付习惯），逐项见 `PROJECT_CANDIDATES.yaml`。Core 候选的项目 Overlay 还包括文档真源路径、批准状态/编号命名、G 阶段名、DEC-042 覆盖、四业态与五端、UI 应用/页面/服务绑定、业务进度权重和本地工作约定；逐能力对应见 Workbook。Overlay 不是新增能力数，也不让项目文件进入 Core。

现有 `docs/project/**`、`docs/temp/**`、`.cursor/**`、`tools/**` 和业务目录保持原位。`ASSET_BOUNDARY_MAP.jsonl` 为全部 1,026 项资产给出原位角色；`ARTIFACT_BOUNDARY_MAP.jsonl` 给出产物与历史记录的候选 Source Role。Legacy 参考档只读，正式 PRD/DEC/ADR/CR/UI_SPEC 的批准与旧版本关系保持原语义。Stage 04 再设计项目实例映射，不以统一 `project-sources/` 作为前提。

目录保护：EXISTING_PROJECT → PRESERVE_IN_PLACE；BANYAN → DISCOVER + MAP + DESIGN；RELAYOUT → EXPLICIT_MIGRATION_ONLY。这里的 DESIGN 是候选边界描述；不移动或重写文件。

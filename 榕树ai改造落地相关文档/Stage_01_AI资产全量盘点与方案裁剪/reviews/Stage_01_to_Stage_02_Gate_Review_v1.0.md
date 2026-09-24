# Stage 01 → Stage 02 Gate Review v1.0

## 文档用途

本文件用于连接：

Stage 01：AI资产全量盘点与方案裁剪

与

Stage 02：Banyan核心边界设计与架构抽象

本文件不是重新盘点报告，不替代 Stage 01 Acceptance Report。

作用：

-   固化 Stage 01 验收结果
-   明确 Stage 02 可消费输入
-   保护已经确认的 AI 能力
-   防止后续架构设计误删已有能力

# 一、Stage 01 状态

状态：

COMPLETED / PASS

Entry Gate：

PASS

执行结果：

-   未进入 Stage 02
-   未创建正式 Banyan Runtime
-   未执行 Legacy Migration
-   未改变项目目录结构

# 二、Stage 01 核心资产结果

## AI资产

-   AI Asset Inventory：1026 项
-   高价值能力：35 项
-   正式/派生产物候选：425 项
-   运行记录：289 项

## 能力保护结论

35 项高价值能力进入后续保护范围。

后续阶段：

不得因为实现方式变化而删除能力。

允许：

-   抽象
-   重构
-   迁移
-   接口化

# 三、Stage 02 输入

Stage 02 必须消费：

-   AI_ASSET_INVENTORY.jsonl
-   LEGACY_AI_CAPABILITY_INVENTORY.jsonl
-   AI_GENERATED_ARTIFACT_INVENTORY.jsonl
-   PRELIMINARY_AI_ARTIFACT_MIGRATION_MATRIX.yaml
-   GIT_IDENTITY_AND_COMMIT_PRACTICE_INVENTORY.yaml

禁止重新执行：

-   全仓 Discovery
-   Stage 01 资产扫描

# 四、能力保护原则

已有榕树 AI 能力：

保留。

不允许：

-   因目录混乱删除能力
-   因暂时无法通用删除能力
-   因旧实现方式删除能力

后续目标：

Capability → Contract → Provider → Artifact → Runtime

# 五、继承约束

## 项目目录

Existing Project：

PRESERVE_IN_PLACE

Banyan：

DISCOVER + MAP + CLASSIFY

重新布局：

EXPLICIT_MIGRATION_ONLY

## Secret

继续继承：

-   metadata only
-   no read
-   no copy
-   no hash
-   no modify
-   no delete

# 六、新增架构关注点

Stage 02 需要考虑：

## AI Runtime Cost Governance

包括：

-   模型选择策略
-   Token预算
-   执行模式
-   批处理策略

目标：

降低长期维护成本。

# 七、Stage 02 开始条件

必须：

-   使用 Stage 01 实际产物
-   不重复扫描
-   不覆盖 Evidence
-   不修改 Legacy
-   不冻结未经验证的架构

完成后：

生成 Stage 02 Acceptance 与 Handoff。

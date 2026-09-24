# Stage 04：Project Instance / Source Mapping / Profile

## 1. 本阶段目的

Stage 03 已冻结 Contract / Schema / Source Role。
Stage 04 将这些冻结契约转换为一个可实施的 Project Instance 设计。

核心链：

```text
Frozen Contract
→ Project Instance
→ Source Mapping
→ Project Overlay
→ Profile / Variable Resolution
→ Provider Binding
```

本阶段仍不是 Runtime 实现阶段，也不是 Legacy Migration 执行阶段。

## 2. 最重要原则

### Existing Project 保持原位

```text
EXISTING_PROJECT = PRESERVE_IN_PLACE
```

已有项目目录不因 Banyan 接入而搬家。

### Project Sources 是逻辑集合

禁止设计成：

```text
project-sources/
  frontend/
  backend/
  docs/
```

然后要求用户把项目真实目录全部迁入其中。

正确模型：

```text
logical source role
→ source mapping
→ one or many existing physical paths
```

## 3. Project Instance 的职责

Project Instance 保存的是“当前项目如何使用 Banyan”，而不是 Banyan Core 本身。

应承载：

```text
project identity
source mappings
project overlays
profiles
variable bindings
provider bindings
feature activation
runtime/index/trace locations
generated artifact locations
migration lineage
```

## 4. Generic Core 与 Project Instance

### Generic Core

必须：

```text
无当前项目业务内容
无当前项目路径
无当前项目端口
无当前项目角色名单
无当前项目 PRD 内容
```

### Project Instance

允许：

```text
当前项目映射
当前项目变量
当前项目 Provider Binding
当前项目 Profile
当前项目 Source Role 绑定
```

## 5. 物理布局

Stage 04 可以冻结“Project Instance 内部布局 Contract”，
但不得要求已有项目物理重排。

推荐目标仅作为 Project Instance 内部结构：

```text
.banyan/
  instance/
  mappings/
  overlays/
  profiles/
  providers/
  runtime/
  trace/
  index/
  generated/
  migrations/
```

是否实际创建由后续执行 Gate 控制。

## 6. Source Mapping

每条 Mapping 至少：

```text
mapping_id
source_role
path_pattern/path_set
read_policy
write_policy
authority
freshness
conflict_policy
project_instance_owner
```

禁止把 Path 当作 Source Role。

## 7. Profile

### Project Profile

描述项目本身：

```text
project_id
display_name
lifecycle
technology hints
governance mode
feature activation
```

### Contributor Profile

只做显示增强：

```text
git_identity_key
display_name
status
note
```

不得：

```text
授权
自动合并 Git identities
固定模块职责
固定前后端角色
猜测真实操作者
```

## 8. Variable Resolution

变量必须结构化区分：

```text
EXPLICIT
DERIVED
DEFAULTED
UNKNOWN
BLOCKED
```

若变量会影响安全、写入、发布、提交等关键行为：

```text
UNKNOWN → BLOCK / NEEDS_INPUT
```

不得静默默认。

## 9. Provider Binding

Stage 03 已冻结 Provider Port。
Stage 04 只冻结 Binding：

```text
port_id
provider_id
binding_scope
project_instance
configuration_ref
capability_declaration
activation_state
fallback_policy
```

本阶段不选唯一供应商。

## 10. 旧项目接入

流程设计：

```text
Inspect Project
→ Bind Source Roles
→ Build Source Mappings
→ Resolve Required Variables
→ Bind Optional Providers
→ Validate
→ Generate Project Instance
```

不搬目录。

## 11. 新项目初始化

新项目可以由 Banyan 建立 Project Instance，
但仍不强制业务目录模板。

可以提供“推荐模板”，不能把它当成唯一合法布局。

## 12. Bootstrap → Canonical Project Instance

本阶段制定迁移施工计划：

```text
.banyan-refactor bootstrap
→ canonical .banyan Project Instance
```

但默认不执行最终切换。

必须保留：

```text
source hash
run lineage
target hash
validation
single writable truth
rollback
```

## 13. 完成标准

必须做到：

```text
9/9 Source Roles mapped or explicitly non-applicable
35/35 Capability bindings accounted
0 default physical relayout requirement
0 project-specific value in Generic Core schema
0 profile field used for authorization
0 critical variable silently defaulted
```

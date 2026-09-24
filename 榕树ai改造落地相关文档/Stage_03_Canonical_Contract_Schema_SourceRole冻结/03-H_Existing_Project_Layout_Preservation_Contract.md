# 03-H：Existing Project Layout Preservation Contract

## 正式默认策略

```text
EXISTING_PROJECT = PRESERVE_IN_PLACE
```

Banyan 接入已有项目时：

```text
不要求搬目录
不要求统一目录名
不要求把源码收进 project-sources/
不要求把 docs/tools/tests 重组
```

通过：

```text
Discovery
Source Mapping
Source Role
Project Overlay
```

理解项目。

## Relayout

只有：

```text
用户明确要求
+ Migration Plan
+ Impact Analysis
+ Reference Integrity
+ Checkpoint
+ Rollback
+ Validation
```

才允许。

## 新项目

即使新项目也不强制 Banyan 业务目录标准；Banyan 只要求自己的 Project Instance 契约完整。

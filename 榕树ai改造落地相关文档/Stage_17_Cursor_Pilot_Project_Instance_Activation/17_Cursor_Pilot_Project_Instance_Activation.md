# Stage 17 Cursor Pilot / Project Instance Activation

## Goal

验证 Banyan 在真实项目中的第一个 Project Instance。

流程：

1. Preflight
2. Checkpoint
3. Project Instance Shadow
4. Cursor Adapter Connection
5. Runtime Validation
6. .banyan Pilot Creation
7. Activation Review

## .banyan

允许：

- pilot instance
- registry
- mappings
- runtime metadata

不允许：

- 替代原项目目录
- 搬迁 docs/project
- 删除旧结构

## Cursor

Cursor 只是 Adapter。

不拥有：

- policy
- permission
- canonical truth

## Validation

验证：

- Runtime 可调用
- Trace 正常
- Provenance 正常
- Rollback 可执行
- Git safety 保持

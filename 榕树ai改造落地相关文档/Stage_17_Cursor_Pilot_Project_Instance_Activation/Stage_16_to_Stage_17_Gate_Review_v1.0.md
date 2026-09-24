# Stage 16 → Stage 17 Gate Review v1.0

## Result

PASS_FOR_STAGE17_CURSOR_PILOT_PROJECT_INSTANCE_ACTIVATION_WITH_EXPLICIT_GATE

Stage 16:
- Control Plane PASS
- WebUI PASS
- Provenance PASS
- Activation Readiness BLOCKED as designed

## Stage 17 Objective

首次进入真实 Project Instance Pilot：

- Cursor Pilot
- Project Instance Binding
- .banyan Shadow/Pilot creation
- Runtime integration validation

## Hard Boundary

Stage 17 不允许：

- 直接覆盖 Canonical 文档
- 修改业务代码作为迁移动作
- 删除 Legacy
- 自动解决 CON-002
- 绕过 Permission Runtime

## .banyan Policy

Stage 17 是第一次允许创建 Pilot `.banyan/`。

流程：

Checkpoint
→ Shadow Creation
→ Validation
→ Human Gate
→ Pilot Activation

禁止一开始直接激活。

## Rollback

必须具备：

- 创建前 checkpoint
- 文件清单
- hash
- reverse plan
- validation

## Stop

完成 Stage 17 后停止，不进入 Stage 18。

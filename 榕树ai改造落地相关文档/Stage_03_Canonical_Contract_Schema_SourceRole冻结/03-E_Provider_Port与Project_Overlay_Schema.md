# 03-E：Provider Port 与 Project Overlay Schema

## Provider Port

Core 只能依赖 Port，不依赖具体 Provider。

Port 至少定义：

```text
port_id
capability
request
response
error/failure semantics
timeout/cancel semantics
evidence requirements
optional capabilities
```

## Project Overlay

项目事实必须通过 Overlay 进入：

```text
project variable
path mapping
business policy override
feature activation
provider binding
```

Overlay 不能改写 Core Contract 的基本安全语义。

## Provider Selection

Stage 03 不选择唯一厂商/模型/编辑器 Provider。

只冻结：

```text
Port Contract
Binding Schema
Capability Declaration
```

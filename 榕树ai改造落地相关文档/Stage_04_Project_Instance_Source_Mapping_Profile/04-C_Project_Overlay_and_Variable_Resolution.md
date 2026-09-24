# 04-C：Project Overlay / Variable Resolution

## Project Overlay

只保存项目差异：

```text
policy override
feature activation
project variable
provider binding
source mapping
delivery convention
```

不能削弱 Core 安全语义。

## Variable Resolution

状态：

```text
EXPLICIT
DERIVED
DEFAULTED
UNKNOWN
BLOCKED
```

每个变量记录：

```text
value
status
source
confidence
sensitivity
required_for
fallback
```

关键变量 UNKNOWN 时不得自动启用能力。

# CLI（命令行界面）使用入门

> 关键术语：Adapter（适配器：对底层能力或入口做受控封装）；Authorization（授权：允许特定范围动作的有效依据）；Gate（门禁：条件不足时阻止下一步）；Canonical Apply（正式真相应用：把批准变更应用到权威来源的治理过程）。

## 这篇解决什么问题

列出当前真实存在的 CLI 命令，并说明它们的输入和安全边界。

## 什么时候需要看

需要调试 Policy、直接调用 Preflight、检查 Git、生成 commit plan、校验 Trace 或启动本地 Control Plane 时。

## 核心概念

CLI（Command-Line Interface，命令行界面）是高级、调试和自动化入口。命令返回 JSON 结果，但返回 `ALLOW` 不代表执行已经发生。`PATH`、`REQUEST` 等大写词是本文占位符，不是固定值。

## 推荐操作方式

只使用以下已实现命令：

```text
banyan policy validate PATH
banyan policy compile PATH
banyan policy compile-stage14 PATH
banyan runtime preflight REQUEST [--policy PATH]
banyan git inspect REPOSITORY
banyan commit plan REPOSITORY --classifications PATH [--groups PATH] [--messages PATH]
banyan commit execute REPOSITORY --plan PATH [--policy PATH] [--authorization-ref REF] [--trace PATH] (--dry-run | --fixture-root PATH)
banyan trace validate PATH
banyan trace emit PATH EVENT
banyan provider list PATH
```

当前 Go Control Plane 入口：

```text
banyan-control --repository PATH --policy PATH [--host HOST] [--port PORT] [--trace PATH] [--providers PATH] [--provenance PATH] [--stages PATH]
```

Python 包中还保留 `banyan-control-plane` 入口，参数形状相同；当前接受架构使用 Go/Gin host。Control Plane 只允许 `127.0.0.1`、`localhost` 或 `::1`。

```text
banyan-control-plane --repository PATH --policy PATH [--host HOST] [--port PORT] [--trace PATH] [--providers PATH] [--provenance PATH] [--stages PATH]
```

先运行只读检查和 plan，再运行 `--dry-run`。只有显式 isolated fixture root（隔离测试根目录）允许真实 mutation，并仍需通过 Gate。

## 自然语言示例

> 请根据实际 CLI Reference 帮我准备 `banyan runtime preflight` 的请求文件，只生成示例并标出占位值，不执行命令。

## 当前实现状态

上述命令来自当前 `banyan.cli`、Python control-plane entry 与 Go `banyan-control`。当前项目 commit execution 为 `DRY_RUN_ONLY`；网络 Git 操作由 Git Adapter 禁用。

## 常见误区

- 不要发明 `banyan apply`、`banyan activate` 或 Canonical Apply 命令；它们不存在。
- `--fixture-root` 是受控测试边界，不是绕过当前项目限制的开关。
- Trace emit 不授予 Authorization。
- CLI 参数包含文件路径时，应先确认读取范围和敏感性。

## 相关 Reference

- [关键 ID 与变量参考](../reference/KEY_IDS_AND_VARIABLES_REFERENCE.md)
- [状态与枚举参考](../reference/STATUS_AND_ENUM_REFERENCE.md)
- [实现状态参考](../reference/IMPLEMENTATION_STATUS_REFERENCE.md)

# 05-H Commit Message / Identity Policy

## Message

Core 提供中立 message schema：

```text
type?
scope?
summary
body?
trailers?
```

项目可 Overlay 具体格式。

## Identity

真实 Git Identity：

```text
author.name + author.email
```

Contributor Profile 仅显示增强。

缺失身份：

```text
BLOCK / NEEDS_INPUT
```

AI 禁止修改身份或使用 `--author`。

# 14-F Git Identity Safety

贡献身份：

```text
author.name + author.email
```

Stage 14 仅验证存在性/一致性。

禁止：

```text
修改 user.name/user.email
--author
identity alias merge
operator inference
```

缺失：

```text
BLOCK / NEEDS_INPUT
```

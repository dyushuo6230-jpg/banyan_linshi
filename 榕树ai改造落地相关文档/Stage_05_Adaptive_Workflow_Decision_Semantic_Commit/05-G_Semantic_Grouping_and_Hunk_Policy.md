# 05-G Semantic Grouping / Hunk Policy

分组优先依据语义与验证边界。

允许：

```text
同目录拆成多个提交
不同目录合成一个原子提交
同一文件按 hunk 分入不同组
```

不允许：

```text
只按扩展名分组
只按目录分组
为了“干净”把 unrelated change 偷塞进去
```

每个组必须有：

```text
group_id
intent
included changes
excluded changes
dependencies
validation
rollback/review rationale
```

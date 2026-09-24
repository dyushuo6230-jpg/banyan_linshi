# 09-K Design Package / Compatibility

Design Package 推荐逻辑层：

```text
source
scene
semantic
design
behavior
data
implementation_ir
validation
```

Legacy 目录名可以映射，但 Generic Core 不依赖：

```text
00-source/
01-scene/
02-semantic/
...
```

这些属于推荐 projection，不是唯一物理布局。

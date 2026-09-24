# Stage 04 Precheck

确认：

```text
Stage 03 = PASS_CONTRACT_FREEZE
Stage 04 Gate = PASS_FOR_IMPLEMENTATION_DESIGN
Stage 04 execution not previously started
```

只检查：

```text
HEAD
tracked/staged/conflict state
Stage 03 frozen hashes
Bootstrap state
13 Secret metadata existence
```

不做全仓扫描。

写入仅：

```text
.banyan-refactor/stages/04/${RUN_ID}/**
两份 bootstrap
```

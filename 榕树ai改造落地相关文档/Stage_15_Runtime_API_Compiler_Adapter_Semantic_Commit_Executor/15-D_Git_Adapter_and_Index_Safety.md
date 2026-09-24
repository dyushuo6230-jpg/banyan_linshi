# 15-D Git Adapter / Index Safety

Git Adapter 必须：

```text
use argv, not shell interpolation
capture stdout/stderr/exit code
classify read-only vs mutating
enforce execution scope
verify repository root
verify fixture root for mutations
```

Index Safety：

```text
pre-index hash
planned path/hunk set
stage
post-index diff
verify exact set
rollback mismatch
```

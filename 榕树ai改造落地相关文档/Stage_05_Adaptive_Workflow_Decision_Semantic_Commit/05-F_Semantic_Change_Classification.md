# 05-F Semantic Change Classification

受控枚举：

```text
READY
INCOMPLETE
UNRELATED
LOCAL_ONLY
SECRET_RISK
```

可以扩展子原因，但顶层语义不漂移。

`SECRET_RISK`：

```text
never auto-stage
never auto-commit
BLOCK
```

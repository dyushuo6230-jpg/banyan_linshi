# 15-A Policy Compiler

Compiler 必须 fail-closed。

测试：

```text
valid policy -> compile
unknown field -> fail
missing hard-block field -> fail
unknown enum -> fail
weakened secret policy -> fail
```

Compiled Policy 必须具有 deterministic hash。

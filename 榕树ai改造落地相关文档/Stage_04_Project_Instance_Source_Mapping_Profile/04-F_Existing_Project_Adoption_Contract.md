# 04-F：Existing Project Adoption Contract

已有项目接入默认：

```text
PRESERVE_IN_PLACE
```

步骤：

```text
1. 读取 Frozen Source Role
2. 建立 Mapping
3. 建立 Overlay
4. 解析变量
5. 绑定 Provider
6. 验证
7. 生成 Project Instance
```

禁止：

```text
先搬目录再接入
要求统一源码根
要求 project-sources/
重命名 docs/tools/src
```

任何 Relayout 必须独立 Migration Plan。

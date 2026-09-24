# 04-H：Framework Distribution vs Project Instance Boundary

## Framework Distribution

未来候选：

```text
banyan-framework/
```

或：

```text
独立 Git
Package
Binary
Plugin
```

只包含通用能力。

## Project Instance

当前项目专属：

```text
.banyan/
```

不能复制到另一个项目直接当配置真源。

## Legacy Construction Workspace

```text
榕树ai改造落地相关文档/
```

属于改造期施工资料，不是未来 Runtime Contract 的必备组成。

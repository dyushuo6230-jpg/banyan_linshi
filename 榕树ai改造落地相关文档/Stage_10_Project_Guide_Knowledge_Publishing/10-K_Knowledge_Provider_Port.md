# 10-K Knowledge Publishing Provider Port

Provider 可以实现：

```text
render markdown
render HTML
render static site
generate meeting pack
generate guide
generate map
```

Core Port 只定义：

```text
publish
refresh
validate
archive
resolve_navigation
```

不绑定具体静态站点工具。

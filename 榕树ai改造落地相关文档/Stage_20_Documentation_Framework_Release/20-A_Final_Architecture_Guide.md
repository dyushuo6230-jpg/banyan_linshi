# 20-A Final Architecture Guide

Explain for beginners and maintainers:

```text
banyan-framework/
= reusable Banyan software

.banyan/
= current project's Banyan instance

.banyan-refactor/
= first-construction bootstrap workspace
```

Document runtime flow:

```text
Editor / WebUI
→ Adapter / Gin
→ Runtime Bridge
→ Python Runtime
→ Policy / Git / Trace / Index / Providers
```

Document authority boundaries and source roles.

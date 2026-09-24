# 14-I Git Operation Permission Matrix

```text
status / diff metadata    READ_ONLY
stage / hunk stage        REVERSIBLE_WRITE-ish / Stage15 executor
commit                    HISTORY_MUTATION / Stage15
reset                     HIGH_RISK
stash                     WORKTREE_STATE_MUTATION
rebase                    HISTORY_REWRITE
push                      EXTERNAL
force push                IRREVERSIBLE_OR_EXTERNAL / very high risk
```

Stage 14 执行全部为 false。

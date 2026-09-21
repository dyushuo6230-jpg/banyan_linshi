package webassets

import "embed"

// Dist contains the immutable Ant Design Pro production build.
//
//go:embed dist/* dist/assets/*
var Dist embed.FS

package httptransport

import (
	"context"
	"encoding/json"
	"io/fs"
	"net/http"
	"strconv"
	"strings"
	"time"

	"github.com/banyan-framework/control-plane/internal/runtimebridge"
	"github.com/gin-gonic/gin"
)

const MaxBodyBytes int64 = 1_000_000

type Handler struct{ Bridge runtimebridge.Bridge }

func NewRouter(bridge runtimebridge.Bridge, embedded fs.FS) *gin.Engine {
	gin.SetMode(gin.ReleaseMode)
	router := gin.New()
	router.Use(gin.Recovery(), bodyLimit())
	h := Handler{Bridge: bridge}
	api := router.Group("/api")
	api.GET("/status", h.get("status"))
	api.GET("/policy", h.get("policy_status"))
	api.GET("/project-safety", h.get("project_safety"))
	api.POST("/preflight", h.post("preflight"))
	api.POST("/commit/plan", h.post("commit_plan"))
	api.POST("/commit/dry-run", h.post("commit_dry_run"))
	api.GET("/trace", h.query("trace_query"))
	api.GET("/provenance/:id", h.provenance())
	api.GET("/providers", h.get("provider_status"))
	api.GET("/stages", h.query("stage_query"))
	api.GET("/activation-readiness", h.get("activation_readiness"))
	api.POST("/adapters/:kind", h.adapter())

	dist, _ := fs.Sub(embedded, "dist")
	assets, _ := fs.Sub(dist, "assets")
	router.StaticFS("/assets", http.FS(assets))
	router.NoRoute(func(c *gin.Context) {
		if strings.HasPrefix(c.Request.URL.Path, "/api/") || strings.HasPrefix(c.Request.URL.Path, "/events/") {
			c.JSON(http.StatusNotFound, gin.H{"error": "NOT_FOUND"})
			return
		}
		data, err := fs.ReadFile(dist, "index.html")
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "EMBEDDED_UI_UNAVAILABLE"})
			return
		}
		c.Data(http.StatusOK, "text/html; charset=utf-8", data)
	})
	return router
}

func bodyLimit() gin.HandlerFunc {
	return func(c *gin.Context) {
		c.Request.Body = http.MaxBytesReader(c.Writer, c.Request.Body, MaxBodyBytes)
		c.Next()
	}
}

func (h Handler) call(c *gin.Context, operation string, payload map[string]any) {
	ctx, cancel := context.WithTimeout(c.Request.Context(), 10*time.Second)
	defer cancel()
	result, err := h.Bridge.Call(ctx, runtimebridge.Request{Operation: operation, Payload: payload})
	if err != nil {
		c.JSON(http.StatusBadGateway, gin.H{"error": "RUNTIME_BRIDGE_FAILURE", "detail": err.Error()})
		return
	}
	c.JSON(http.StatusOK, result)
}

func (h Handler) get(operation string) gin.HandlerFunc {
	return func(c *gin.Context) { h.call(c, operation, map[string]any{}) }
}
func (h Handler) query(operation string) gin.HandlerFunc {
	return func(c *gin.Context) {
		offset, e1 := strconv.Atoi(c.DefaultQuery("offset", "0"))
		limit, e2 := strconv.Atoi(c.DefaultQuery("limit", "50"))
		if e1 != nil || e2 != nil || offset < 0 || limit < 1 || limit > 200 {
			c.JSON(http.StatusBadRequest, gin.H{"error": "INVALID_REQUEST"})
			return
		}
		h.call(c, operation, map[string]any{"offset": offset, "limit": limit})
	}
}
func (h Handler) provenance() gin.HandlerFunc {
	return func(c *gin.Context) { h.call(c, "provenance_query", map[string]any{"stable_id": c.Param("id")}) }
}
func (h Handler) post(operation string) gin.HandlerFunc {
	return func(c *gin.Context) {
		var payload map[string]any
		if err := json.NewDecoder(c.Request.Body).Decode(&payload); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "INVALID_REQUEST"})
			return
		}
		h.call(c, operation, payload)
	}
}
func (h Handler) adapter() gin.HandlerFunc {
	return func(c *gin.Context) {
		kind := c.Param("kind")
		if kind != "cursor" && kind != "codex" && kind != "generic-editor" {
			c.JSON(http.StatusBadRequest, gin.H{"error": "UNKNOWN_ADAPTER"})
			return
		}
		var request map[string]any
		if err := json.NewDecoder(c.Request.Body).Decode(&request); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": "INVALID_REQUEST"})
			return
		}
		h.call(c, "adapter_request", map[string]any{"adapter": kind, "request": request})
	}
}

func ValidateBindHost(host string) bool {
	return host == "127.0.0.1" || host == "localhost" || host == "::1"
}

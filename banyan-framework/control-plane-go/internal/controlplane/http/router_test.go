package httptransport

import (
	"context"
	"encoding/json"
	"io/fs"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"testing/fstest"

	"github.com/banyan-framework/control-plane/internal/runtimebridge"
)

type fakeBridge struct{ fail bool }

func (f fakeBridge) Call(_ context.Context, req runtimebridge.Request) (map[string]any, error) {
	if f.fail {
		return nil, &runtimebridge.TypedError{Code: "TEST_FAILURE", Message: "closed"}
	}
	return map[string]any{"operation": req.Operation, "payload": req.Payload, "permission_result": "RUNTIME_OWNED", "secret_body_rendered": false}, nil
}

func testAssets() fs.FS {
	return fstest.MapFS{
		"dist/index.html":    &fstest.MapFile{Data: []byte("<html>Ant Design Pro Banyan</html>")},
		"dist/assets/app.js": &fstest.MapFile{Data: []byte("console.log('banyan')")},
	}
}

func TestRouteContractAndAPINotFound(t *testing.T) {
	r := NewRouter(fakeBridge{}, testAssets())
	cases := []struct{ method, path string }{{"GET", "/api/status"}, {"GET", "/api/policy"}, {"GET", "/api/project-safety"}, {"POST", "/api/preflight"}, {"POST", "/api/commit/plan"}, {"POST", "/api/commit/dry-run"}, {"GET", "/api/trace"}, {"GET", "/api/provenance/id"}, {"GET", "/api/providers"}, {"GET", "/api/stages"}, {"GET", "/api/activation-readiness"}}
	for _, tc := range cases {
		body := strings.NewReader("{}")
		req := httptest.NewRequest(tc.method, tc.path, body)
		req.Header.Set("Content-Type", "application/json")
		w := httptest.NewRecorder()
		r.ServeHTTP(w, req)
		if w.Code != 200 {
			t.Fatalf("%s %s: %d %s", tc.method, tc.path, w.Code, w.Body.String())
		}
	}
	w := httptest.NewRecorder()
	r.ServeHTTP(w, httptest.NewRequest("GET", "/api/missing", nil))
	if w.Code != 404 || strings.Contains(w.Body.String(), "Ant Design") {
		t.Fatalf("API 404 fell through to SPA: %d %s", w.Code, w.Body.String())
	}
}

func TestSPADeepLinkAndEmbeddedAsset(t *testing.T) {
	r := NewRouter(fakeBridge{}, testAssets())
	for _, path := range []string{"/dashboard", "/activation-readiness"} {
		w := httptest.NewRecorder()
		r.ServeHTTP(w, httptest.NewRequest("GET", path, nil))
		if w.Code != 200 || !strings.Contains(w.Body.String(), "Ant Design Pro Banyan") {
			t.Fatalf("deep link failed")
		}
	}
	w := httptest.NewRecorder()
	r.ServeHTTP(w, httptest.NewRequest("GET", "/assets/app.js", nil))
	if w.Code != 200 {
		t.Fatalf("asset failed: %d", w.Code)
	}
}

func TestTypedBridgeFailureAndBodyLimit(t *testing.T) {
	r := NewRouter(fakeBridge{fail: true}, testAssets())
	w := httptest.NewRecorder()
	r.ServeHTTP(w, httptest.NewRequest("GET", "/api/status", nil))
	if w.Code != http.StatusBadGateway || !strings.Contains(w.Body.String(), "RUNTIME_BRIDGE_FAILURE") {
		t.Fatalf("untyped bridge failure: %s", w.Body.String())
	}
	r = NewRouter(fakeBridge{}, testAssets())
	w = httptest.NewRecorder()
	r.ServeHTTP(w, httptest.NewRequest("POST", "/api/preflight", strings.NewReader(`{"x":"`+strings.Repeat("a", int(MaxBodyBytes))+`"}`)))
	if w.Code != http.StatusBadRequest {
		t.Fatalf("large body accepted: %d", w.Code)
	}
}

func TestAdapterRoutesCarryKindAndRequest(t *testing.T) {
	r := NewRouter(fakeBridge{}, testAssets())
	for _, kind := range []string{"cursor", "codex", "generic-editor"} {
		w := httptest.NewRecorder()
		r.ServeHTTP(w, httptest.NewRequest("POST", "/api/adapters/"+kind, strings.NewReader(`{"request_id":"x"}`)))
		if w.Code != 200 {
			t.Fatalf("adapter %s: %d", kind, w.Code)
		}
		var result map[string]any
		_ = json.Unmarshal(w.Body.Bytes(), &result)
		if result["operation"] != "adapter_request" {
			t.Fatalf("adapter bypassed bridge")
		}
	}
}

func TestLocalBindOnly(t *testing.T) {
	for _, host := range []string{"127.0.0.1", "localhost", "::1"} {
		if !ValidateBindHost(host) {
			t.Fatal(host)
		}
	}
	for _, host := range []string{"0.0.0.0", "192.0.2.1", ""} {
		if ValidateBindHost(host) {
			t.Fatal(host)
		}
	}
}

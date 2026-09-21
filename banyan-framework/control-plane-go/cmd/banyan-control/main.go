package main

import (
	"flag"
	"fmt"
	"net/http"
	"os"
	"time"

	httptransport "github.com/banyan-framework/control-plane/internal/controlplane/http"
	"github.com/banyan-framework/control-plane/internal/runtimebridge"
	"github.com/banyan-framework/control-plane/internal/webassets"
)

func main() {
	host := flag.String("host", "127.0.0.1", "loopback bind host")
	port := flag.Int("port", 8765, "listen port")
	repository := flag.String("repository", "", "project repository")
	policy := flag.String("policy", "", "compiled policy source")
	trace := flag.String("trace", "", "audit trace path")
	providers := flag.String("providers", "", "provider bindings path")
	provenance := flag.String("provenance", "", "provenance index path")
	stages := flag.String("stages", "", "stage records path")
	flag.Parse()
	if !httptransport.ValidateBindHost(*host) {
		fmt.Fprintln(os.Stderr, "public bind is forbidden")
		os.Exit(2)
	}
	if *repository == "" || *policy == "" {
		fmt.Fprintln(os.Stderr, "repository and policy are required")
		os.Exit(2)
	}
	bridge := runtimebridge.ProcessBridge{Command: "python3", Args: []string{"-m", "banyan.control_plane.bridge"}, Env: []string{
		runtimebridge.Env("BANYAN_REPOSITORY", *repository), runtimebridge.Env("BANYAN_POLICY", *policy), runtimebridge.Env("BANYAN_TRACE", *trace),
		runtimebridge.Env("BANYAN_PROVIDERS", *providers), runtimebridge.Env("BANYAN_PROVENANCE", *provenance), runtimebridge.Env("BANYAN_STAGES", *stages),
	}}
	server := &http.Server{Addr: fmt.Sprintf("%s:%d", *host, *port), Handler: httptransport.NewRouter(bridge, webassets.Dist), ReadHeaderTimeout: 5 * time.Second, ReadTimeout: 15 * time.Second, WriteTimeout: 15 * time.Second, IdleTimeout: 30 * time.Second}
	fmt.Printf("Banyan Control Plane: http://%s:%d (LOCAL_ONLY, DRY_RUN_ONLY)\n", *host, *port)
	if err := server.ListenAndServe(); err != nil && err != http.ErrServerClosed {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}

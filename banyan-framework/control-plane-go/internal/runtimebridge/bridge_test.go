package runtimebridge

import (
	"context"
	"testing"
)

func TestProcessBridgeTypedSuccessAndFailure(t *testing.T) {
	ok := ProcessBridge{Command: "python3", Args: []string{"-c", `import json,sys; r=json.load(sys.stdin); print(json.dumps({"ok":True,"result":{"operation":r["operation"]}}))`}}
	value, err := ok.Call(context.Background(), Request{Operation: "status", Payload: map[string]any{}})
	if err != nil || value["operation"] != "status" {
		t.Fatalf("success: %v %v", value, err)
	}
	fail := ProcessBridge{Command: "python3", Args: []string{"-c", `import json; print(json.dumps({"ok":False,"error":{"code":"RUNTIME_BLOCKED","message":"closed"}}))`}}
	_, err = fail.Call(context.Background(), Request{Operation: "status", Payload: map[string]any{}})
	if err == nil || !IsTyped(err) {
		t.Fatalf("failure not typed: %v", err)
	}
}

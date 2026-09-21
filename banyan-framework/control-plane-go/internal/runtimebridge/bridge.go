package runtimebridge

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"os/exec"
)

type Request struct {
	Operation string         `json:"operation"`
	Payload   map[string]any `json:"payload"`
}

type Response struct {
	OK     bool           `json:"ok"`
	Result map[string]any `json:"result,omitempty"`
	Error  *TypedError    `json:"error,omitempty"`
}

type TypedError struct {
	Code    string `json:"code"`
	Message string `json:"message"`
}

func (e *TypedError) Error() string { return e.Code + ": " + e.Message }

type Bridge interface {
	Call(context.Context, Request) (map[string]any, error)
}

type ProcessBridge struct {
	Command string
	Args    []string
	Env     []string
}

func (b ProcessBridge) Call(ctx context.Context, request Request) (map[string]any, error) {
	input, err := json.Marshal(request)
	if err != nil {
		return nil, &TypedError{Code: "BRIDGE_REQUEST_INVALID", Message: err.Error()}
	}
	cmd := exec.CommandContext(ctx, b.Command, b.Args...)
	cmd.Env = append(os.Environ(), b.Env...)
	cmd.Stdin = bytes.NewReader(input)
	var stdout, stderr bytes.Buffer
	cmd.Stdout, cmd.Stderr = &stdout, &stderr
	runErr := cmd.Run()
	var response Response
	if err := json.Unmarshal(stdout.Bytes(), &response); err != nil {
		message := stderr.String()
		if message == "" {
			message = err.Error()
		}
		return nil, &TypedError{Code: "RUNTIME_BRIDGE_PROTOCOL_FAILURE", Message: message}
	}
	if !response.OK {
		if response.Error != nil {
			return nil, response.Error
		}
		return nil, &TypedError{Code: "RUNTIME_BRIDGE_FAILURE", Message: "runtime returned failure"}
	}
	if runErr != nil {
		return nil, &TypedError{Code: "RUNTIME_BRIDGE_PROCESS_FAILURE", Message: runErr.Error()}
	}
	return response.Result, nil
}

func Env(key, value string) string { return fmt.Sprintf("%s=%s", key, value) }

func IsTyped(err error) bool {
	var target *TypedError
	return errors.As(err, &target)
}

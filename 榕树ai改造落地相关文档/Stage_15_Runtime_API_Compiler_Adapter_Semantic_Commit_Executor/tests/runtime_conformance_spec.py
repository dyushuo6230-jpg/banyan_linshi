"""Stage 15 conformance expectations. This file is a specification helper, not production runtime."""

FORBIDDEN_COMMAND_PATTERNS = [
    ["git", "add", "."],
    ["git", "add", "-A"],
]

REQUIRED_PERMISSION_RESULTS = {"ALLOW", "BLOCK", "NEEDS_INPUT", "NOT_APPLICABLE"}

REQUIRED_EXECUTION_SCOPES = {
    "CURRENT_PROJECT_DRY_RUN",
    "ISOLATED_FIXTURE",
    "AUTHORIZED_PROJECT_EXECUTION",
}

def assert_command_is_not_blind_stage(argv):
    assert list(argv) not in FORBIDDEN_COMMAND_PATTERNS

def assert_permission_result(value):
    assert value in REQUIRED_PERMISSION_RESULTS

def assert_execution_scope(value):
    assert value in REQUIRED_EXECUTION_SCOPES

if __name__ == "__main__":
    assert_permission_result("ALLOW")
    assert_execution_scope("ISOLATED_FIXTURE")
    assert_command_is_not_blind_stage(["git", "add", "--", "file.txt"])
    print("PASS Stage15 conformance spec smoke-check")

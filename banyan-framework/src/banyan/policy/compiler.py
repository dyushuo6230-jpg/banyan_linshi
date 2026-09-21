"""Strict, deterministic and fail-closed policy compilation."""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from types import MappingProxyType
from typing import Any, Mapping

import yaml


class PolicyCompileError(ValueError):
    pass


RISK_CLASSES = {
    "READ_ONLY",
    "REVERSIBLE_WRITE",
    "CANONICAL_WRITE",
    "PROTECTED_WRITE",
    "IRREVERSIBLE_OR_EXTERNAL",
}
PERMISSION_RESULTS = {"ALLOW", "BLOCK", "NEEDS_INPUT", "NOT_APPLICABLE"}
EXECUTION_SCOPES = {
    "CURRENT_PROJECT_DRY_RUN",
    "ISOLATED_FIXTURE",
    "AUTHORIZED_PROJECT_EXECUTION",
}
REQUIRED_HARD_BLOCKS = {
    "SECRET_RISK",
    "UNKNOWN_PRECONDITION",
    "MISSING_AUTHORIZATION",
    "MISSING_IDENTITY_FOR_COMMIT",
    "CONFLICTED_WORKTREE",
    "INDEX_SET_MISMATCH",
}
REQUIRED_OPERATION_RISKS = {
    "inspect": "READ_ONLY",
    "plan_commit": "READ_ONLY",
    "commit": "PROTECTED_WRITE",
    "protected_write": "PROTECTED_WRITE",
    "external_action": "IRREVERSIBLE_OR_EXTERNAL",
}
POLICY_FIELDS = {
    "schema_version",
    "policy_id",
    "risk_classes",
    "permission_results",
    "execution_scopes",
    "hard_blocks",
    "required_preconditions",
    "operation_risks",
    "unknown_precondition_result",
    "current_project_mutation_allowed",
    "fixture_network_allowed",
    "source_bundle_hash",
}


@dataclass(frozen=True)
class CompiledPolicy:
    data: Mapping[str, Any]
    policy_hash: str

    def to_dict(self) -> dict[str, Any]:
        return {"policy_hash": self.policy_hash, "policy": dict(self.data)}


class PolicyCompiler:
    """Compile a normalized generic policy without silently accepting drift."""

    def load(self, path: str | Path) -> dict[str, Any]:
        p = Path(path)
        text = p.read_text(encoding="utf-8")
        value = json.loads(text) if p.suffix.lower() == ".json" else yaml.safe_load(text)
        if not isinstance(value, dict):
            raise PolicyCompileError("policy root must be an object")
        return value

    def compile_file(self, path: str | Path) -> CompiledPolicy:
        return self.compile(self.load(path))

    def compile_stage14_bundle(self, directory: str | Path) -> CompiledPolicy:
        """Validate the frozen Stage 14 bundle and bind its digest into runtime policy."""
        root = Path(directory)
        registry = self.load(root / "POLICY_REGISTRY.yaml")
        handoff = self.load(root / "STAGE15_RUNTIME_ENFORCEMENT_HANDOFF.yaml")
        registry_fields = {"schema_version", "registry_id", "policies", "runtime_may_weaken_policy", "stage14_policy_state"}
        if set(registry) != registry_fields:
            raise PolicyCompileError("Stage14 policy registry fields mismatch")
        if registry["runtime_may_weaken_policy"] is not False:
            raise PolicyCompileError("Stage14 runtime weakening is forbidden")
        policies = registry["policies"]
        required_inputs = handoff.get("required_inputs")
        if not isinstance(policies, dict) or not isinstance(required_inputs, list):
            raise PolicyCompileError("invalid Stage14 registry or handoff")
        if set(policies.values()) != set(required_inputs):
            raise PolicyCompileError("Stage14 registry and handoff inputs mismatch")
        if handoff.get("stage15_execution_authorized") is not False:
            raise PolicyCompileError("Stage14 handoff cannot authorize Stage15 execution")

        documents: dict[str, dict[str, Any]] = {}
        digest_input = bytearray()
        for filename in sorted(required_inputs):
            path = root / filename
            if not path.is_file():
                raise PolicyCompileError(f"missing Stage14 policy: {filename}")
            raw = path.read_bytes()
            digest_input.extend(filename.encode("utf-8") + b"\0" + raw + b"\0")
            document = yaml.safe_load(raw)
            if not isinstance(document, dict):
                raise PolicyCompileError(f"Stage14 policy must be an object: {filename}")
            documents[filename] = document

        secret = documents["SECRET_SAFETY_GATE.yaml"]
        semantic = documents["SEMANTIC_COMMIT_AUTHORIZATION.yaml"]
        operations = documents["GIT_OPERATION_PERMISSION_MATRIX.yaml"]
        if secret.get("secret_risk_result") != "BLOCK" or secret.get("stage14_grants_secret_authorization") is not False:
            raise PolicyCompileError("Stage14 secret hard block was weakened")
        if semantic.get("commit_plan_is_authorization") is not False or semantic.get("classes", {}).get("SECRET_RISK") != "HARD_BLOCK":
            raise PolicyCompileError("Stage14 semantic commit hard block was weakened")
        if operations.get("operations", {}).get("commit", {}).get("risk") != "PROTECTED_WRITE":
            raise PolicyCompileError("Stage14 commit risk was weakened")

        normalized = default_policy()
        normalized["source_bundle_hash"] = sha256(bytes(digest_input)).hexdigest()
        return self.compile(normalized)

    def compile(self, policy: Mapping[str, Any]) -> CompiledPolicy:
        unknown = set(policy) - POLICY_FIELDS
        if unknown:
            raise PolicyCompileError(f"unknown policy fields: {sorted(unknown)}")
        missing = POLICY_FIELDS - set(policy)
        if missing:
            raise PolicyCompileError(f"missing policy fields: {sorted(missing)}")

        self._exact_enum("risk_classes", policy["risk_classes"], RISK_CLASSES)
        self._exact_enum("permission_results", policy["permission_results"], PERMISSION_RESULTS)
        self._exact_enum("execution_scopes", policy["execution_scopes"], EXECUTION_SCOPES)
        hard_blocks = set(self._string_list("hard_blocks", policy["hard_blocks"]))
        missing_blocks = REQUIRED_HARD_BLOCKS - hard_blocks
        if missing_blocks:
            raise PolicyCompileError(f"required hard blocks removed: {sorted(missing_blocks)}")
        self._string_list("required_preconditions", policy["required_preconditions"])

        operation_risks = policy["operation_risks"]
        if not isinstance(operation_risks, dict) or not operation_risks:
            raise PolicyCompileError("operation_risks must be a non-empty object")
        for name, risk in operation_risks.items():
            if not isinstance(name, str) or risk not in RISK_CLASSES:
                raise PolicyCompileError(f"invalid operation risk: {name!r}={risk!r}")
        for operation, required_risk in REQUIRED_OPERATION_RISKS.items():
            if operation_risks.get(operation) != required_risk:
                raise PolicyCompileError(f"required operation risk weakened or missing: {operation}")

        if policy["unknown_precondition_result"] not in {"BLOCK", "NEEDS_INPUT"}:
            raise PolicyCompileError("unknown preconditions must fail closed")
        if policy["current_project_mutation_allowed"] is not False:
            raise PolicyCompileError("current-project mutation cannot be enabled by this policy")
        if policy["fixture_network_allowed"] is not False:
            raise PolicyCompileError("fixture network operations must remain disabled")

        canonical = json.dumps(policy, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        digest = sha256(canonical.encode("utf-8")).hexdigest()
        frozen = MappingProxyType(json.loads(canonical))
        return CompiledPolicy(frozen, digest)

    @staticmethod
    def _string_list(name: str, value: Any) -> list[str]:
        if not isinstance(value, list) or not value or not all(isinstance(x, str) for x in value):
            raise PolicyCompileError(f"{name} must be a non-empty string list")
        if len(value) != len(set(value)):
            raise PolicyCompileError(f"{name} contains duplicates")
        return value

    def _exact_enum(self, name: str, value: Any, expected: set[str]) -> None:
        actual = set(self._string_list(name, value))
        if actual != expected:
            raise PolicyCompileError(f"{name} mismatch: expected {sorted(expected)}, got {sorted(actual)}")


def default_policy() -> dict[str, Any]:
    return {
        "schema_version": "stage15-v1",
        "policy_id": "banyan.runtime.default.v1",
        "risk_classes": sorted(RISK_CLASSES),
        "permission_results": sorted(PERMISSION_RESULTS),
        "execution_scopes": sorted(EXECUTION_SCOPES),
        "hard_blocks": sorted(REQUIRED_HARD_BLOCKS),
        "required_preconditions": [
            "evidence_complete",
            "impact_reviewed",
            "authorization_valid",
            "secret_check_passed",
            "freshness_valid",
            "rollback_ready",
        ],
        "operation_risks": {
            "inspect": "READ_ONLY",
            "plan_commit": "READ_ONLY",
            "commit": "PROTECTED_WRITE",
            "protected_write": "PROTECTED_WRITE",
            "external_action": "IRREVERSIBLE_OR_EXTERNAL",
        },
        "unknown_precondition_result": "NEEDS_INPUT",
        "current_project_mutation_allowed": False,
        "fixture_network_allowed": False,
        "source_bundle_hash": "builtin-stage14-contract-v1",
    }

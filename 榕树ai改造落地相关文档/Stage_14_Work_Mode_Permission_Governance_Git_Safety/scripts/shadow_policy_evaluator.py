#!/usr/bin/env python3
"""Offline Stage 14 policy evaluator. No Git or filesystem mutations."""
from dataclasses import dataclass

@dataclass
class Case:
    risk: str
    identity_ok: bool = True
    secret_risk: bool = False
    freshness_ok: bool = True
    rollback_ok: bool = True
    authorization_ok: bool = True
    unknown_precondition: bool = False

def evaluate(c: Case) -> str:
    if c.unknown_precondition:
        return "BLOCK_NEEDS_INPUT"
    if c.secret_risk:
        return "BLOCK"
    if c.risk != "READ_ONLY" and not c.authorization_ok:
        return "BLOCK"
    if c.risk in {"CANONICAL_WRITE", "PROTECTED_WRITE", "IRREVERSIBLE_OR_EXTERNAL"}:
        if not c.freshness_ok or not c.rollback_ok:
            return "BLOCK"
    if c.risk == "PROTECTED_WRITE" and not c.identity_ok:
        return "BLOCK_NEEDS_INPUT"
    return "ALLOW"

tests = [
    (Case("READ_ONLY"), "ALLOW"),
    (Case("PROTECTED_WRITE", identity_ok=False), "BLOCK_NEEDS_INPUT"),
    (Case("PROTECTED_WRITE", secret_risk=True), "BLOCK"),
    (Case("PROTECTED_WRITE", freshness_ok=False), "BLOCK"),
    (Case("PROTECTED_WRITE", authorization_ok=False), "BLOCK"),
    (Case("READ_ONLY", unknown_precondition=True), "BLOCK_NEEDS_INPUT"),
]

for c, expected in tests:
    got = evaluate(c)
    assert got == expected, (c, got, expected)
print("PASS Stage14 offline policy cases")

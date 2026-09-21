# Post-release Maintenance Model

Framework changes start as typed change proposals and follow impact, preview, validation, apply, rollback and acceptance gates. Releases retain immutable artifact hashes and evidence links. Project-specific configuration belongs in Project Instance overlays and bindings rather than generic Core.

Security or compatibility fixes use the same lifecycle with an appropriate risk class. Emergency work may shorten review latency but cannot remove the safety floor, Secret controls, authorization binding, Git identity checks or trace capture.

`.banyan-refactor/` is not used for routine upgrades. After Final Activation and retirement preconditions are approved, archive it according to the Stage 20 retirement plan. Retain the archive, hash manifest and minimum evidence needed for audit and rollback history.

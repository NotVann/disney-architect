# Contributing to Disney Architect

Contributions are welcome. Please adhere to the guidelines below to maintain cross-agent compatibility and high architectural rigor.

---

## Architecture Guidelines

1. **Protocol Purity**:
   - Updates to `references/01-dreamer-protocol.md`, `02-realist-protocol.md`, or `03-critic-protocol.md` must maintain domain-agnostic and language-agnostic compatibility.
   - Do not introduce language-specific assumptions into core protocols.
2. **Deterministic Tooling**:
   - Any new scripts added to `scripts/` must be deterministic, require zero external non-standard dependencies where possible, and run cleanly across Linux, macOS, and Windows.
3. **Encoding Discipline**:
   - Use standard ASCII output markers (`[OK]`, `[+]`, `[*]`, `[!]`) instead of Unicode characters to prevent `cp1252` encoding crashes on Windows consoles.

---

## Local Verification

Before submitting a Pull Request, run the local validation suite:

```bash
# Verify syntax and AST across the repository
python scripts/critic_linter.py .

# Verify multi-agent harness installation
python scripts/install_harness.py .
```

All CI checks must pass before merging.

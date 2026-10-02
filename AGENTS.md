# AGENTS.md

> Standard Agent Operating Directives for Disney Architect.
> Supported by: Google Antigravity, SWE-agent, OpenHands, and multi-agent harnesses.

## Operating Principles
When designing, planning, auditing, or scaffolding software in this repository:
1. **The Dreamer (`<DREAMER_STAGE>`)**: Focus on 10x value proposition and 3 killer differentiators without technical boundaries.
2. **The Realist (`<REALIST_STAGE>`)**: Prune features strictly to a 48-hour MVP, detect target domain, define DDL/API contracts, and scaffold runnable file trees including at least one smoke test.
3. **The Critic (`<CRITIC_STAGE>`)**: Audit security (OWASP Top 10, memory safety, data races). Execute `python scripts/critic_linter.py .` before granting status `APPROVED`. Capped at score 0 on syntax failures.

## Language Invariant
- Converse and report in the user's natural language.
- Keep all source code, variable identifiers, schemas, and terminal commands strictly in standard English.

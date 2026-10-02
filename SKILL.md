---
name: disney-architect
description: >-
  Universal software architecture and scaffolding skill applying the 3-stage Disney
  Creative Strategy (Dreamer for product vision, Realist for pragmatic stack and code
  scaffolding, Critic for security and stability audit). Works across ALL AI models
  (7B s/d Frontier) and ALL Agent CLIs (Antigravity, Claude Code, Cursor, Aider, Cline).
---

# Disney Architect: Universal Software Engineering Framework

## Overview
This skill operationalizes Robert Dilts' Disney Creative Strategy into an autonomous, polyglot software engineering and scaffolding pipeline. It is **model-agnostic** (uses XML delimiters and few-shot examples for low-parameter model reliability), **domain-agnostic** (Web, CLI, Systems, Mobile, Microservices), and **agent-agnostic** (Antigravity, Claude Code, Cursor, Windsurf, Cline, Aider).

## Language Directive (CRITICAL)
- **Prose & Interaction**: Automatically mirror user's conversational language (e.g. Indonesian prompt `→` respond and report in Indonesian).
- **Technical Code & Symbols**: Keep all source code, variable names, schemas, comments, and configuration files strictly in standard English.

---

## Universal Execution Pipeline

```
[User Request (Any Domain / Any Language)]
                  │
                  ▼
┌─────────────────────────────────────────┐
│ STATE 1: <DREAMER_STAGE>                │ ──► `references/01-dreamer-protocol.md`
│ Output: Core Value, 3 Killer Features   │
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│ STATE 2: <REALIST_STAGE>                │ ──► `references/02-realist-protocol.md`
│ Auto-detects Domain & Target Language   │
│ Selects Idiomatic Stack & Scaffolds Tree│
└─────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────┐
│ STATE 3: <CRITIC_STAGE>                 │ ──► `references/03-critic-protocol.md`
│ Audits Domain-Specific Risk Vectors     │
│ Deterministic Gate: `critic_linter.py`  │
└─────────────────────────────────────────┘
                  │
       ┌──────────┴──────────────────────────────┐
       ▼ [Score < 80 AND Iteration < 2]          ▼ [Score >= 80 OR Iteration == 2]
┌─────────────────────────┐               ┌─────────────────────────┐
│ STATE 4: REVISION LOOP  │               │ STATE 5: SCAFFOLDING    │
│ Realist fixes audit gaps│               │ Writes code to disk     │
└─────────────────────────┘               └─────────────────────────┘
       ▲                     │                           │
       └─────────────────────┘                           ▼
                                                  [Scaffold Verified via verify_scaffold.py]
```

---

## Execution Modes
- **Autonomous Mode (`--auto` / Default)**:
  - Executes the full pipeline continuously: `<DREAMER_STAGE>` → `<REALIST_STAGE>` → `<CRITIC_STAGE>` → Scaffolding to disk.
- **Interactive Mode (`--interactive`)**:
  - Executes `<DREAMER_STAGE>`, then **pauses** execution to present the 3 Killer Features and Value Proposition to the user.
  - Waits for user feedback/confirmation before proceeding to `<REALIST_STAGE>`.

---

## TDD Smoke Test Mandate
The Realist MUST include at least one runnable smoke test file in the scaffold directory tree (e.g. `tests/test_smoke.[py|ts|go|rs]`) testing basic startup/healthcheck. The Critic will reject architectures that omit runnable test baselines.

---

## Model Reliability & Few-Shot Reference
- For lower-parameter models (7B/8B), strictly reference `examples/golden-sample.md` for output schema formatting.
- Enforce output encapsulation within `<DREAMER_STAGE>`, `<REALIST_STAGE>`, and `<CRITIC_STAGE>` tags.

---

## Deterministic Anti-Hallucination Gate
Before the Critic grants status `APPROVED`:
1. Execute: `python scripts/critic_linter.py <target_directory>`
2. Any syntax or AST failure immediately resets score to `0/100` (`CHANGES_REQUESTED`).

---

## Multi-Agent CLI Installation
To install this skill across all agent environments on the machine:
```bash
python scripts/install_harness.py
```
Automatically mounts into Antigravity (`.agents`), Claude Code (`.claude`), Cursor (`.cursor/rules`), Windsurf (`.windsurfrules`), Cline (`.clinerules`), and Aider (`CONVENTIONS.md`).

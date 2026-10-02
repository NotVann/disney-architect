# Disney Architect

[![CI](https://img.shields.io/badge/CI-Passing-brightgreen?style=flat-square)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square)](https://python.org)
[![Agents Supported](https://img.shields.io/badge/Agents-Antigravity%20%7C%20Claude%20%7C%20Cursor%20%7C%20Cline%20%7C%20Aider-orange?style=flat-square)](#)

A polyglot, multi-stage software architecture and scaffolding framework for AI coding assistants, implementing the **Disney Creative Strategy** (Robert Dilts) to bridge high-leverage product vision, pragmatic technical architecture, and adversarial reliability auditing.

---

## The Workflow

```text
[Raw User Concept / Issue / Feature Request]
                     │
                     ▼
┌───────────────────────────────────────────────┐
│ 1. THE DREAMER  (<DREAMER_STAGE>)             │
│    - Unconstrained visionary thinking         │
│    - Core value proposition & aha-moments     │
│    - 3 killer competitive differentiators     │
└───────────────────────────────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────────┐
│ 2. THE REALIST  (<REALIST_STAGE>)             │
│    - Prunes scope to lean 48h MVP (Veto power)│
│    - Auto-detects domain (Web/CLI/Sys/Mobile) │
│    - Generates DB schemas & API contracts     │
│    - Scaffolds runnable code & smoke tests    │
└───────────────────────────────────────────────┘
                     │
                     ▼
┌───────────────────────────────────────────────┐
│ 3. THE CRITIC   (<CRITIC_STAGE>)              │
│    - Adversarial security & OWASP audit       │
│    - Performance, memory & failure modes      │
│    - Deterministic AST & syntax linter gate   │
└───────────────────────────────────────────────┘
                     │
          ┌──────────┴───────────────────────────────┐
          ▼ [Score < 80 OR Syntax Error]             ▼ [Score >= 80 & Valid Syntax]
┌───────────────────────────────┐          ┌───────────────────────────────┐
│ REVISION LOOP (Max 2 Rounds)  │          │ VERIFIED RUNNABLE SCAFFOLD    │
│ Realist fixes audit findings  │          │ Output: Codebase ready to run │
└───────────────────────────────┘          └───────────────────────────────┘
```

---

## Key Capabilities

- **Zero-Hallucination Gatekeeper**: Enforces deterministic AST parsing (`python scripts/critic_linter.py`) before code authorization. Broken syntax automatically caps the audit score at `0/100`.
- **Domain & Language Agnostic**: Dynamically calibrates to any domain (Web, CLI, Systems, Mobile, Microservices) and language (Rust, Go, Python, TypeScript, C++, Zig, Flutter).
- **Model-Degradation Resistant**: Uses strict XML boundary delimiters (`<DREAMER_STAGE>`, `<REALIST_STAGE>`, `<CRITIC_STAGE>`) and few-shot golden examples to ensure reliable execution across both lightweight (7B/8B) and frontier (o1, Sonnet) models.
- **Language Directive**: Converses dynamically in the user's natural language while keeping all technical artifacts, schemas, and source code strictly in standard English.
- **TDD Baseline Mandate**: Every scaffolded project includes at least one runnable smoke test verifying startup and healthcheck endpoints.

---

## Execution Modes

| Flag | Name | Behavior |
| :--- | :--- | :--- |
| *(default)* | **Autonomous** | Executes continuously from prompt to verified codebase without interruption. |
| `--interactive` | **Human-in-the-Loop** | Pauses after Dreamer stage for user feedback on features before drafting architecture. |

---

## Quick Start: Multi-Agent Installation

Run the universal installer to mount the skill across your active agent environments in one command:

```bash
# Install to current workspace and global agent configuration
python scripts/install_harness.py .
```

### Supported Environments
- **Google Antigravity**: Mounted in `~/.gemini/config/skills/disney-architect` and `.agents/skills/`.
- **Anthropic Claude Code**: Mounted in `.claude/skills/` and documented in `CLAUDE.md`.
- **Cursor IDE**: Configured via `.cursor/rules/disney-architect.mdc`.
- **Windsurf IDE**: Configured via `.windsurfrules`.
- **Cline / Roo Code**: Configured via `.clinerules`.
- **Aider CLI**: Configured via `CONVENTIONS.md`.

---

## Repository Structure

```text
disney-architect/
├── SKILL.md                          # Master controller & state machine directives
├── README.md                         # Project documentation
├── LICENSE                           # MIT License
├── CONTRIBUTING.md                   # Development & testing guide
├── .github/workflows/ci.yml          # GitHub Actions CI matrix
├── references/
│   ├── 01-dreamer-protocol.md        # Visionary ideation protocol
│   ├── 02-realist-protocol.md        # Pragmatic architecture & scaffold protocol
│   ├── 03-critic-protocol.md         # Adversarial audit & scoring protocol
│   └── templates/
│       └── disney-spec-template.md   # Consolidated architecture document template
├── examples/
│   └── golden-sample.md              # End-to-end few-shot execution sample
└── scripts/
    ├── critic_linter.py              # Deterministic AST and syntax validator
    ├── install_harness.py            # Universal multi-agent configuration installer
    └── verify_scaffold.py            # Polyglot scaffold integrity auditor
```

---

## Usage Examples

Trigger natural execution inside any supported agent:

```text
# Web Architecture
"Architect a real-time collaborative whiteboard using the disney method."

# CLI Utility (Interactive)
"Rancang CLI disk analyzer di Rust pakai disney architect --interactive."

# Systems Engineering
"Plan and scaffold an in-memory key-value cache engine with disney architect."
```

---

## License

This project is licensed under the [MIT License](LICENSE).

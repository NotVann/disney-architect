#!/usr/bin/env python3
"""
Universal Agent Harness Installer
Configures and mounts the Disney Architect skill across multiple AI agent environments:
- Google Antigravity CLI (Global & Local)
- Anthropic Claude Code (.claude/ & CLAUDE.md)
- Cursor IDE (.cursor/rules/)
- Windsurf IDE (.windsurfrules)
- Cline / Roo Code (.clinerules)
- Aider CLI (CONVENTIONS.md)
"""

from __future__ import annotations

import os
import shutil
import sys
from pathlib import Path

SKILL_DIR: Path = Path(__file__).resolve().parent.parent

CURSOR_RULE_CONTENT: str = """---
description: Universal Disney Architect multi-stage software engineering framework
globs: *
alwaysApply: false
---

# Disney Architect Framework (Dreamer, Realist, Critic)

When designing, architecting, or scaffolding full-stack software, CLI utilities, or systems:
1. **The Dreamer**: Formulate core value prop and 3 killer differentiator features without constraints.
2. **The Realist**: Prune to 48-hour MVP, select idiomatic stack for the target language, define schemas and API contracts.
3. **The Critic**: Audit against security, performance bottlenecks, and operational costs. Enforce score >= 80/100 before writing code.

Reference: `disney-architect` skill.
"""

CLINERULE_CONTENT: str = """# Disney Architect Framework
Apply the 3-stage Disney Creative Strategy (Dreamer -> Realist -> Critic) when planning and scaffolding code:
- Stage 1 <DREAMER_STAGE>: Unconstrained vision, killer differentiators, UX journey.
- Stage 2 <REALIST_STAGE>: 48h MVP pruning, idiomatic stack selection, complete schemas & file tree.
- Stage 3 <CRITIC_STAGE>: Adversarial security audit, failure vectors, passing score >= 80/100.
"""


def install_all(target_workspace: str = ".") -> None:
    """
    Mounts skill artifacts and IDE rules into the target workspace and global config directories.
    Guards against self-recursive directory traversal when workspace is SKILL_DIR.
    """
    ws = Path(target_workspace).resolve()
    print(f"[*] Installing disney-architect harnesses into workspace: {ws}")

    ignore_patterns = shutil.ignore_patterns(
        ".agents", ".claude", ".cursor", ".git",
        "__pycache__", "node_modules", "target", "build"
    )

    # 1. Antigravity Local Workspace Mount (.agents/skills/disney-architect)
    if ws != SKILL_DIR:
        ag_dir = ws / ".agents" / "skills" / "disney-architect"
        ag_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_DIR, ag_dir, dirs_exist_ok=True, ignore=ignore_patterns)
        print(f"[+] Antigravity CLI: Mounted at {ag_dir}")

    # 2. Antigravity Global Mount (~/.gemini/config/skills/disney-architect)
    home = Path.home()
    global_ag = home / ".gemini" / "config" / "skills" / "disney-architect"
    try:
        global_ag.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_DIR, global_ag, dirs_exist_ok=True, ignore=ignore_patterns)
        print(f"[+] Antigravity Global: Mounted at {global_ag}")
    except Exception as e:
        print(f"[-] Antigravity Global skipped: {e}")

    # 3. Claude Code Skill Mount & Command Reference
    if ws != SKILL_DIR:
        claude_skills = ws / ".claude" / "skills" / "disney-architect"
        claude_skills.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SKILL_DIR, claude_skills, dirs_exist_ok=True, ignore=ignore_patterns)
        print(f"[+] Claude Code: Mounted at {claude_skills}")

    claude_md = ws / "CLAUDE.md"
    claude_entry = "\n\n## Skills\n- `/disney`: Invoke the Disney Architect framework (Dreamer, Realist, Critic) for software design and scaffolding.\n"
    if not claude_md.exists() or "/disney" not in claude_md.read_text(encoding="utf-8", errors="ignore"):
        with open(claude_md, "a", encoding="utf-8") as f:
            f.write(claude_entry)
        print(f"[+] Claude Code: Updated {claude_md}")

    # 4. Cursor IDE Rules (.cursor/rules/disney-architect.mdc)
    cursor_dir = ws / ".cursor" / "rules"
    cursor_dir.mkdir(parents=True, exist_ok=True)
    (cursor_dir / "disney-architect.mdc").write_text(CURSOR_RULE_CONTENT, encoding="utf-8")
    print(f"[+] Cursor: Configured {cursor_dir / 'disney-architect.mdc'}")

    # 5. Windsurf IDE (.windsurfrules)
    windsurf_file = ws / ".windsurfrules"
    if not windsurf_file.exists() or "Disney Architect" not in windsurf_file.read_text(encoding="utf-8", errors="ignore"):
        with open(windsurf_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n{CLINERULE_CONTENT}")
        print(f"[+] Windsurf: Configured {windsurf_file}")

    # 6. Cline / Roo Code (.clinerules)
    cline_file = ws / ".clinerules"
    if not cline_file.exists() or "Disney Architect" not in cline_file.read_text(encoding="utf-8", errors="ignore"):
        with open(cline_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n{CLINERULE_CONTENT}")
        print(f"[+] Cline / Roo Code: Configured {cline_file}")

    # 7. Aider Conventions (CONVENTIONS.md)
    aider_file = ws / "CONVENTIONS.md"
    if not aider_file.exists() or "Disney Architect" not in aider_file.read_text(encoding="utf-8", errors="ignore"):
        with open(aider_file, "a", encoding="utf-8") as f:
            f.write(f"\n\n{CLINERULE_CONTENT}")
        print(f"[+] Aider: Configured {aider_file}")

    print("\n[OK] All Agent CLI & IDE harnesses installed successfully.")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    install_all(target)

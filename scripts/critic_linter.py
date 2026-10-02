#!/usr/bin/env python3
"""
Deterministic Critic Linter
Ground-truth AST and syntax validator for scaffolded codebases.
Bypasses LLM self-evaluation bias by enforcing hard parser checks (Python AST,
V8 node syntax checks, and RFC 8259 JSON validation).
"""

from __future__ import annotations

import ast
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Set

# Directories to exclude from AST scanning to avoid false positives and performance degradation
IGNORED_DIRECTORIES: Set[str] = {
    "node_modules",
    ".git",
    "target",
    "dist",
    "build",
    "__pycache__",
    ".venv",
    ".agents",
    ".claude",
    ".cursor",
}


def check_python_file(path: Path) -> List[str]:
    """
    Validates Python source files against standard AST parser.
    Catches syntax errors, indentation errors, and encoding anomalies.
    """
    errors: List[str] = []
    try:
        source = path.read_text(encoding="utf-8")
        ast.parse(source, filename=str(path))
    except SyntaxError as e:
        errors.append(f"Python SyntaxError in {path.name}:{e.lineno} - {e.msg}")
    except UnicodeDecodeError as e:
        errors.append(f"UTF-8 Encoding failure in {path.name}: {e.reason}")
    except Exception as e:
        errors.append(f"AST ParseError in {path.name}: {e}")
    return errors


def check_json_file(path: Path) -> List[str]:
    """
    Validates JSON files against RFC 8259 specifications.
    Ensures manifests (package.json, tsconfig.json) are parseable.
    """
    errors: List[str] = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Malformed JSON in {path.name}:{e.lineno} - {e.msg}")
    except Exception as e:
        errors.append(f"JSON ReadError in {path.name}: {e}")
    return errors


def strip_js_comments_and_strings(content: str) -> str:
    """
    Removes comments and string literals to prevent false positives in heuristic brace checks.
    """
    # Strip block and inline comments
    content = re.sub(r"/\*[\s\S]*?\*/|//.*", "", content)
    # Strip double and single quoted strings
    content = re.sub(r'"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', '""', content)
    # Strip template literals
    content = re.sub(r"`(?:\\.|[^`\\])*`", '""', content)
    return content


def check_node_ts_file(path: Path) -> List[str]:
    """
    Validates JavaScript/TypeScript files.
    Prefers native V8 syntax verification ('node --check') for .js files.
    Falls back to comment-stripped structural brace analysis when node runtime is absent or for .ts.
    """
    errors: List[str] = []

    if path.suffix == ".js":
        try:
            res = subprocess.run(
                ["node", "--check", str(path)],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if res.returncode != 0:
                errors.append(f"V8 SyntaxCheck failed for {path.name}: {res.stderr.strip()}")
                return errors
        except (FileNotFoundError, subprocess.TimeoutExpired):
            # Node binary not present in environment; fallback to heuristic structural scan
            pass

    try:
        raw_content = path.read_text(encoding="utf-8")
        clean_content = strip_js_comments_and_strings(raw_content)

        open_braces = clean_content.count("{")
        close_braces = clean_content.count("}")
        if open_braces != close_braces:
            errors.append(
                f"Mismatched curly braces in {path.name} "
                f"(Opening: {open_braces}, Closing: {close_braces})"
            )
    except Exception as e:
        errors.append(f"IO read failure in {path.name}: {e}")

    return errors


def run_linter(project_dir: str) -> bool:
    """
    Traverses the scaffolded target directory, dispatching file types to their
    respective deterministic AST parsers.
    """
    root = Path(project_dir).resolve()
    print(f"[*] Deterministic Critic Linter running on: {root}")

    if not root.exists() or not root.is_dir():
        print(f"[!] Error: Target directory '{root}' does not exist.")
        return False

    all_errors: List[str] = []

    for path in root.rglob("*"):
        if not path.is_file() or any(d in path.parts for d in IGNORED_DIRECTORIES):
            continue

        if path.suffix == ".py":
            all_errors.extend(check_python_file(path))
        elif path.suffix == ".json":
            all_errors.extend(check_json_file(path))
        elif path.suffix in {".js", ".ts", ".jsx", ".tsx"}:
            all_errors.extend(check_node_ts_file(path))

    # Note: Use plain ASCII tags to guarantee cross-platform compatibility across Windows CP1252 consoles
    print("\n--- Deterministic Critic Linter Report ---")
    if all_errors:
        print(f"[!] REJECTION: {len(all_errors)} syntax/AST failure(s) detected:")
        for err in all_errors:
            print(f"    - {err}")
        print("\nVerdict: REJECTED (Score hard-capped to 0)")
        return False

    print("[OK] All source files passed deterministic syntax/AST verification.")
    print("Verdict: SYNTAX_VALID")
    return True


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    passed = run_linter(target)
    sys.exit(0 if passed else 1)

#!/usr/bin/env python3
"""
Universal Scaffold Verification Utility
Automated structural auditor validating dependency manifests, configuration templates,
and source file non-emptiness across all major programming ecosystems.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import List, Set

# Universal package and build manifests ordered by ecosystem prevalence
POLYGLOT_MANIFESTS: List[str] = [
    # Node / Web
    "package.json",
    # Python
    "pyproject.toml", "requirements.txt", "setup.py",
    # Systems (Rust, Go, C/C++, Zig)
    "Cargo.toml", "go.mod", "CMakeLists.txt", "Makefile", "build.zig",
    # JVM & .NET
    "pom.xml", "build.gradle", "build.gradle.kts", "*.csproj", "*.sln",
    # Mobile & Multiplatform
    "pubspec.yaml", "Package.swift",
    # Functional / BEAM
    "mix.exs",
]

# Source extensions subject to zero-byte non-emptiness validation
SOURCE_EXTENSIONS: Set[str] = {
    ".ts", ".js", ".py", ".go", ".rs", ".c", ".cpp",
    ".h", ".hpp", ".zig", ".kt", ".swift", ".dart", ".cs",
}

IGNORED_DIRECTORIES: Set[str] = {
    "node_modules", ".git", "target", "dist", "build",
    "__pycache__", ".venv", ".agents", ".claude", ".cursor",
}


def verify_scaffold(project_dir: str) -> bool:
    """
    Performs multi-point integrity checks on a newly scaffolded project tree.
    Returns True if the scaffold complies with production baseline standards.
    """
    root = Path(project_dir).resolve()
    print(f"[*] Auditing polyglot scaffold at: {root}")

    if not root.exists() or not root.is_dir():
        print(f"[!] Error: Target directory '{root}' does not exist.")
        return False

    errors: List[str] = []
    warnings: List[str] = []

    # Check 1: Dependency manifest discovery
    found_manifest = False
    for pattern in POLYGLOT_MANIFESTS:
        if "*" in pattern:
            if any(root.glob(pattern)):
                found_manifest = True
                break
        elif (root / pattern).exists():
            found_manifest = True
            break

    if not found_manifest:
        errors.append(f"Missing build/dependency manifest. Expected one of: {POLYGLOT_MANIFESTS}")
    else:
        print("[+] Universal build manifest detected.")

    # Check 2: Environment configuration baseline
    # Non-web applications (e.g. CLI or system utilities) may not require an env file; log as warning.
    env_templates = [".env.example", ".env.sample", ".env.template", "config.example.toml", "config.example.yaml"]
    if not any((root / e).exists() for e in env_templates):
        warnings.append("No configuration template detected (.env.example or config.example.*).")
    else:
        print("[+] Configuration template detected.")

    # Check 3: JSON file structural integrity
    for json_path in root.rglob("*.json"):
        if any(ignored in json_path.parts for ignored in IGNORED_DIRECTORIES):
            continue
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            errors.append(f"Corrupt JSON in {json_path.name}: {e}")

    # Check 4: Accidental empty source files (indicates aborted scaffolding write)
    for src_path in root.rglob("*"):
        if not src_path.is_file() or src_path.name.startswith("."):
            continue
        if any(ignored in src_path.parts for ignored in IGNORED_DIRECTORIES):
            continue
        if src_path.suffix in SOURCE_EXTENSIONS and src_path.stat().st_size == 0:
            warnings.append(f"Empty source file detected: {src_path.relative_to(root)}")

    # Print summary with standard ASCII formatting to ensure reliability across all terminal encodings
    print("\n--- Universal Scaffold Audit Summary ---")
    if warnings:
        print(f"[?] Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"    - {w}")
    if errors:
        print(f"[x] Errors ({len(errors)}):")
        for e in errors:
            print(f"    - {e}")
        return False

    print("[OK] Polyglot scaffold verification passed successfully.")
    return True


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    success = verify_scaffold(target)
    sys.exit(0 if success else 1)

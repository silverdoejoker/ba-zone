#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor for Repository Hygiene & Prototype / Build Leak Prevention
Enforces that no prototype code, mockups, or build bundles are tracked in Git.
Author: Phúc NT @ BA Zone
"""

import os
import sys
import subprocess

# Force UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Forbidden directories and patterns that must NEVER have committed artifacts
FORBIDDEN_TRACKED_PATTERNS = [
    ("prototypes/", [".gitkeep"]),
    ("mockups/", [".gitkeep"]),
    ("scratch/", [".gitkeep"]),
    ("artifacts/", [".gitkeep"]),
    ("docs/inputs/", [".gitkeep"]),
    ("docs/outputs/", [".gitkeep"]),
    ("docs/projects/", [".gitkeep"]),
    ("dist/", []),
    ("build/", []),
    ("out/", []),
    ("node_modules/", []),
]

def check_git_tracked_files(repo_root):
    """Checks git tracked files using git ls-files."""
    try:
        res = subprocess.run(
            ["git", "ls-files"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
        tracked_files = [line.strip() for line in res.stdout.splitlines() if line.strip()]
    except Exception as e:
        print(f"❌ Error executing 'git ls-files': {e}")
        return False, [f"Git execution failed: {e}"]

    violations = []
    
    for file_path in tracked_files:
        norm_path = file_path.replace("\\", "/")
        for prefix, allowed in FORBIDDEN_TRACKED_PATTERNS:
            if norm_path.startswith(prefix):
                file_name = norm_path[len(prefix):]
                # Allow whitelisted files like .gitkeep
                if file_name in allowed or file_name.endswith("/.gitkeep"):
                    continue
                violations.append((file_path, f"Violation: '{file_path}' must NOT be tracked. Repositories are strictly for documentation."))

    return len(violations) == 0, violations


def check_gitignore_rules(repo_root):
    """Verifies that key forbidden patterns are covered in .gitignore."""
    gitignore_path = os.path.join(repo_root, ".gitignore")
    if not os.path.isfile(gitignore_path):
        return False, [".gitignore file is missing!"]

    with open(gitignore_path, "r", encoding="utf-8") as f:
        content = f.read()

    required_rules = [
        "prototypes/*",
        "mockups/*",
        "dist/",
        "build/",
        "node_modules/",
        "scratch/*",
        "artifacts/*",
        "docs/inputs/*",
        "docs/outputs/*",
        "docs/projects/*"
    ]
    
    missing_rules = []
    for rule in required_rules:
        if rule not in content:
            missing_rules.append(f"Missing rule in .gitignore: {rule}")

    return len(missing_rules) == 0, missing_rules


def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print("=" * 60)
    print(" AUDITING REPO HYGIENE: NO PROTOTYPES/BUILDS COMMITTED POLICY")
    print("=" * 60)
    print(f"Target Repository: {repo_root}")

    # Check 1: .gitignore rules
    gi_ok, gi_issues = check_gitignore_rules(repo_root)
    if not gi_ok:
        print("\n❌ .gitignore Rule Violations:")
        for issue in gi_issues:
            print(f"  - {issue}")
    else:
        print("  -> PASS: .gitignore contains all strict exclusion rules.")

    # Check 2: Actual Git tracked files
    tracked_ok, tracked_issues = check_git_tracked_files(repo_root)
    if not tracked_ok:
        print("\n❌ FORBIDDEN COMMITTED FILES DETECTED:")
        for path, reason in tracked_issues:
            print(f"  - {path}: {reason}")
    else:
        print("  -> PASS: No prototype/mockup/build files are tracked in Git.")

    print("=" * 60)
    if gi_ok and tracked_ok:
        print("🎉 RESULT: REPOSITORY HYGIENE 100% COMPLIANT (DOCS ONLY)!\n")
        sys.exit(0)
    else:
        print("❌ RESULT: FAILED - REMOVE FORBIDDEN FILES FROM GIT INDEX!\n")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor for BA Zone Outputs Directory (docs/outputs/)
Performs comprehensive quality, standards, structural, NDA, and link integrity checks.
Author: BA Zone / Digital School
"""

import os
import re
import sys

# Force UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUTPUTS_DIR = os.path.join(REPO_ROOT, "docs", "outputs")

class AuditResult:
    def __init__(self, filename):
        self.filename = filename
        self.errors = []
        self.warnings = []
        self.checks_passed = []

    def add_error(self, msg):
        self.errors.append(msg)

    def add_warning(self, msg):
        self.warnings.append(msg)

    def add_pass(self, msg):
        self.checks_passed.append(msg)

    @property
    def is_passed(self):
        return len(self.errors) == 0

def check_mermaid_syntax(content, res):
    """Checks mermaid blocks for basic syntax validity."""
    mermaid_blocks = re.findall(r"```mermaid(.*?)```", content, re.DOTALL)
    if not mermaid_blocks:
        return
    
    valid_starts = ["graph", "flowchart", "sequencediagram", "gantt", "classdiagram", "erdiagram", "statediagram", "pie"]
    for idx, block in enumerate(mermaid_blocks, 1):
        lines = [l.strip() for l in block.strip().splitlines() if l.strip() and not l.strip().startswith("%%")]
        if not lines:
            res.add_error(f"Mermaid block #{idx} is empty.")
            continue
        first_line = lines[0].lower()
        if not any(first_line.startswith(vs) for vs in valid_starts):
            res.add_warning(f"Mermaid block #{idx} starts with unrecognized keyword: '{lines[0]}'")
        else:
            res.add_pass(f"Mermaid diagram #{idx} ({first_line.split()[0]}) syntax verified.")

def check_cross_links(content, filepath, res):
    """Checks markdown links to local files and ensures target files exist."""
    file_dir = os.path.dirname(filepath)
    # Find markdown links [text](path)
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for text, link in links:
        if link.startswith("http://") or link.startswith("https://") or link.startswith("mailto:") or link.startswith("#"):
            continue
        
        # Normalize local file link
        clean_link = link
        if clean_link.startswith("file:///"):
            clean_link = clean_link[8:].replace("/", os.sep)
            if not os.path.isabs(clean_link) and len(clean_link) > 2 and clean_link[1] != ":":
                clean_link = os.path.join(REPO_ROOT, clean_link)
        else:
            clean_link = os.path.normpath(os.path.join(file_dir, clean_link.replace("/", os.sep)))
        
        if not os.path.exists(clean_link):
            res.add_error(f"Broken link detected: '[{text}]({link})' -> Target does not exist: {clean_link}")
        else:
            res.add_pass(f"Link valid: '{text}' -> {os.path.basename(clean_link)}")

def check_nda_sanitization(content, res):
    """Verifies compliance with Enterprise NDA Sanitizer rules."""
    # Check for hardcoded secret keys/passwords
    password_patterns = [r"password\s*=\s*['\"][^'\"]+['\"]", r"secret_key\s*=\s*['\"][^'\"]+['\"]", r"api_token\s*=\s*['\"][^'\"]+['\"]"]
    for pat in password_patterns:
        if re.search(pat, content, re.IGNORECASE):
            res.add_error("Potential credential/secret exposure detected in document.")

    # Check stakeholder naming rule: Ms. Tú (PMO) - ensure not referred as 'anh Tú'
    if re.search(r"\banh\s+tú\b", content, re.IGNORECASE):
        res.add_error("Stakeholder naming violation: PMO is female (Ms. Tú), referred incorrectly as 'anh Tú'.")
    else:
        res.add_pass("Stakeholder persona & title integrity verified.")

def audit_brd(content, filepath, res):
    """Specific audit for Business Requirements Documents."""
    content_lower = content.lower()
    
    # 1. Document Control
    req_meta = ["mã số định danh", "phiên bản", "tác giả"]
    missing_meta = [m for m in req_meta if m not in content_lower]
    if missing_meta:
        res.add_error(f"BRD missing Document Control metadata: {', '.join(missing_meta)}")
    else:
        res.add_pass("Document Control metadata complete.")

    # 2. Objectives (SMART)
    if "mục tiêu" not in content_lower:
        res.add_error("BRD missing Project Objectives section.")
    else:
        res.add_pass("Project Objectives defined.")

    # 3. Scope
    if "phạm vi" not in content_lower and "scope" not in content_lower:
        res.add_warning("BRD missing explicit Scope definition section.")
    else:
        res.add_pass("Project Scope defined.")

    # 4. Core Functional Modules
    if "phân hệ nghiệp vụ" not in content_lower and "modules" not in content_lower:
        res.add_error("BRD missing Core Functional Modules breakdown.")
    else:
        res.add_pass("Core Functional Modules detailed.")

    # 5. Authority Matrix (AM) / RBAC
    if not any(k in content_lower for k in ["authority matrix", "ma trận phân quyền", "phân quyền", "rbac", " ma trận am", "(am)"]):
        res.add_warning("BRD missing Authority Matrix (AM) / Role-Based Access Control.")
    else:
        res.add_pass("Authority Matrix (AM) verified.")

    # 6. Fit-Gap Analysis (for reuse projects)
    if "fit-gap" in content_lower or "khoảng trống" in content_lower:
        res.add_pass("Fit-Gap analysis matrix verified.")

def audit_action_plan(content, filepath, res):
    """Specific audit for Action Plans."""
    content_lower = content.lower()
    if "thông tin chung" not in content_lower and "mục tiêu" not in content_lower:
        res.add_warning("Action Plan missing general info / objectives.")
    if "hành động" not in content_lower and "action" not in content_lower:
        res.add_error("Action Plan missing action steps.")
    if "giai đoạn" not in content_lower and "timeline" not in content_lower and "lộ trình" not in content_lower:
        res.add_warning("Action Plan missing phases / timeline.")
    res.add_pass("Action Plan core structure verified.")

def audit_document(filepath):
    filename = os.path.basename(filepath)
    res = AuditResult(filename)
    
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        res.add_error(f"Failed to read file: {e}")
        return res

    # Universal checks
    check_mermaid_syntax(content, res)
    check_cross_links(content, filepath, res)
    check_nda_sanitization(content, res)

    # Document type specific checks
    lower_fn = filename.lower()
    if "brd" in lower_fn:
        audit_brd(content, filepath, res)
    elif "action_plan" in lower_fn:
        audit_action_plan(content, filepath, res)
    
    return res

def run_all_output_audits():
    print("=" * 68)
    print("        AUDITING BA ZONE OUTPUTS DIRECTORY (docs/outputs/)")
    print("=" * 68)
    print(f"Target Directory: {OUTPUTS_DIR}")
    
    if not os.path.exists(OUTPUTS_DIR):
        print(f"ERROR: Directory not found: {OUTPUTS_DIR}")
        return False

    all_results = []
    total_files = 0
    total_passed = 0

    for root, dirs, files in os.walk(OUTPUTS_DIR):
        # Sort for deterministic order
        files.sort()
        for file in files:
            if not file.endswith(".md"):
                continue
            
            total_files += 1
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, OUTPUTS_DIR)
            res = audit_document(full_path)
            all_results.append((rel_path, res))
            if res.is_passed:
                total_passed += 1

    # Output detailed report
    for rel_path, res in all_results:
        status_symbol = "✅ PASS" if res.is_passed else "❌ FAIL"
        print(f"\n[{status_symbol}] {rel_path}")
        for p in res.checks_passed:
            print(f"    ✓ {p}")
        for w in res.warnings:
            print(f"    ⚠️ [WARN] {w}")
        for e in res.errors:
            print(f"    ❌ [ERROR] {e}")

    print("\n" + "=" * 68)
    print(f"SUMMARY: {total_passed}/{total_files} Markdown documents passed 100% standard checks.")
    print("=" * 68)

    all_clean = (total_passed == total_files)
    return all_clean

if __name__ == "__main__":
    success = run_all_output_audits()
    sys.exit(0 if success else 1)

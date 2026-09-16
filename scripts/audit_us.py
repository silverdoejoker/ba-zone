#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor for User Story & Acceptance Criteria Markdown Specifications (INVEST & Gherkin Standard)
Author: BA Zone / Digital School
"""

import os
import re
import sys
import argparse

# Force UTF-8 output encoding for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

def audit_user_story(content, filepath=""):
    filename = os.path.basename(filepath) if filepath else "User Story Content"
    print(f"\n============================================================")
    print(f"   AUDITING USER STORY: {filename}")
    print(f"============================================================")
    
    issues = []
    content_lower = content.lower()

    # 1. Check User Story 3-part statement
    print("[1/5] Checking 3-part User Story statement...")
    has_role = bool(re.search(r"(\*\*as a\*\*|\*\*as an\*\*|\*\*là một\*\*)", content_lower))
    has_action = bool(re.search(r"(\*\*i want to\*\*|\*\*i want\*\*|\*\*tôi muốn\*\*)", content_lower))
    has_value = bool(re.search(r"(\*\*so that\*\*|\*\*để\*\*)", content_lower))

    if not has_role:
        issues.append("Missing User Story role clause ('As a...' or 'Là một...')")
    if not has_action:
        issues.append("Missing User Story action clause ('I want to...' or 'Tôi muốn...')")
    if not has_value:
        issues.append("Missing User Story value clause ('So that...' or 'Để...')")

    if has_role and has_action and has_value:
        print("  -> Valid 3-part Story structure detected.")

    # 2. Check for Generic Persona anti-pattern
    print("[2/5] Checking persona specificity (Anti-pattern inspection)...")
    generic_persona = bool(re.search(r"(\*\*as a\*\*\s+user\b|\*\*là một\*\*\s+người dùng\b|\*\*là một\*\*\s+user\b)", content_lower))
    if generic_persona:
        issues.append("Anti-pattern detected: Persona is overly generic ('user' / 'người dùng'). Must specify concrete role (e.g. 'Learner', 'Admin', 'Guest').")
    else:
        print("  -> Persona is properly scoped.")

    # 3. Check INVEST Self-check table / section
    print("[3/5] Checking INVEST quality evaluation...")
    has_invest = "invest" in content_lower or all(k in content_lower for k in ["independent", "valuable", "testable"]) or all(k in content_lower for k in ["độc lập", "giá trị", "kiểm thử"])
    if not has_invest:
        issues.append("INVEST evaluation matrix or self-check section is missing.")
    else:
        print("  -> INVEST evaluation matrix is present.")

    # 4. Check Acceptance Criteria count & Gherkin syntax
    print("[4/5] Inspecting Acceptance Criteria quantity & Gherkin syntax...")
    ac_matches = re.findall(r"(####?\s*ac\d+:|\*\*ac\d+:)", content_lower)
    ac_count = len(ac_matches)
    if ac_count < 3:
        issues.append(f"Insufficient Acceptance Criteria count: found {ac_count}, minimum 3 required (Happy, Edge, Negative).")
    else:
        print(f"  -> Found {ac_count} Acceptance Criteria scenarios (meets min requirement >= 3).")

    has_given = bool(re.search(r"(\bgiven\b|cho biết)", content_lower))
    has_when = bool(re.search(r"(\bwhen\b|\bkhi\b)", content_lower))
    has_then = bool(re.search(r"(\bthen\b|\bthì\b)", content_lower))

    if not (has_given and has_when and has_then):
        issues.append("Acceptance Criteria must use Gherkin syntax (Given / When / Then or Cho biết / Khi / Thì).")
    else:
        print("  -> Gherkin syntax structure verified.")

    # 5. Check Scenario coverage (Happy path, Edge case, Negative path)
    print("[5/5] Checking AC scenario coverage (Happy, Edge, Negative)...")
    has_happy = bool(re.search(r"(happy|thành công|chuẩn)", content_lower))
    has_edge = bool(re.search(r"(edge|boundary|biên|giới hạn)", content_lower))
    has_negative = bool(re.search(r"(negative|error|failure|lỗi|thất bại)", content_lower))

    coverage_missing = []
    if not has_happy:
        coverage_missing.append("Happy Path")
    if not has_edge:
        coverage_missing.append("Edge Case")
    if not has_negative:
        coverage_missing.append("Negative Path")

    if coverage_missing:
        issues.append(f"Acceptance Criteria missing scenario coverage for: {', '.join(coverage_missing)}")
    else:
        print("  -> All 3 essential scenario types (Happy, Edge, Negative) are covered.")

    # Summary
    print("------------------------------------------------------------")
    if issues:
        print(f"❌ AUDIT FAILED with {len(issues)} issue(s):")
        for idx, issue in enumerate(issues, start=1):
            print(f"   {idx}. {issue}")
        return False
    else:
        print("✅ AUDIT PASSED: 100% compliant with INVEST & Gherkin Standard!")
        return True

def main():
    parser = argparse.ArgumentParser(description="Audit User Story Markdown File (INVEST & Gherkin Standard)")
    parser.add_argument("--file", required=True, help="Path to the User Story markdown file")
    args = parser.parse_args()

    if not os.path.isfile(args.file):
        print(f"Error: File not found: {args.file}")
        sys.exit(1)

    try:
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {args.file}: {e}")
        sys.exit(1)

    success = audit_user_story(content, filepath=args.file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

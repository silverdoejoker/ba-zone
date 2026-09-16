#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditor for Use Case Markdown Specifications (IIBA & Karl Wiegers Standard)
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

# Field definitions with English and Vietnamese synonyms
UC_16_FIELDS = [
    ("Use Case ID", ["use case id", "mã use case", "mã uc"]),
    ("Use Case Name", ["use case name", "tên use case", "tên uc"]),
    ("Created By & Date", ["created by", "người tạo"]),
    ("Last Updated By & Date", ["last updated by", "người cập nhật"]),
    ("Primary Actor", ["primary actor", "actor", "tác nhân chính", "tác nhân"]),
    ("Description", ["description", "mô tả"]),
    ("Preconditions", ["preconditions", "precondition", "tiền điều kiện"]),
    ("Postconditions", ["postconditions", "postcondition", "hậu điều kiện"]),
    ("Priority", ["priority", "độ ưu tiên"]),
    ("Frequency of Use", ["frequency of use", "frequency", "tần suất sử dụng", "tần suất"]),
    ("Normal Course", ["normal course", "luồng sự kiện chính", "happy path"]),
    ("Alternative Courses", ["alternative courses", "alternative course", "luồng sự kiện thay thế", "luồng thay thế"]),
    ("Exceptions", ["exceptions", "exception", "luồng ngoại lệ", "ngoại lệ"]),
    ("Includes", ["includes", "use case liên kết", "include"]),
    ("Special Requirements", ["special requirements", "yêu cầu đặc biệt"]),
    ("Assumptions & Notes", ["assumptions", "notes and issues", "giả định & ghi chú", "giả định"])
]

def audit_use_case(content, filepath=""):
    filename = os.path.basename(filepath) if filepath else "Use Case Content"
    print(f"\n============================================================")
    print(f"   AUDITING USE CASE: {filename}")
    print(f"============================================================")
    
    issues = []
    content_lower = content.lower()

    # 1. Check all 16 required fields
    print("[1/5] Checking 16 Karl Wiegers / IIBA standard fields...")
    missing_fields = []
    for standard_name, synonyms in UC_16_FIELDS:
        found = any(syn in content_lower for syn in synonyms)
        if not found:
            missing_fields.append(standard_name)
    
    if missing_fields:
        for mf in missing_fields:
            issues.append(f"Missing required field: '{mf}'")
    else:
        print("  -> All 16 standard fields are present.")

    # 2. Check Use Case ID format
    print("[2/5] Validating Use Case ID convention...")
    id_pattern = re.search(r"UC-[A-Z0-9]+-\d+", content)
    if id_pattern:
        print(f"  -> Found valid Use Case ID: {id_pattern.group(0)}")
    else:
        issues.append("Use Case ID does not follow standard convention 'UC-[MODULE]-[NN]' (e.g. UC-AUTH-01)")

    # 3. Check Normal Course of Events
    print("[3/5] Inspecting Normal Course of Events flow...")
    # Verify presence of step numbers (either markdown table step column or numbered list)
    has_numbered_steps = bool(re.search(r"(\n\s*\d+\.\s+[A-Za-zÀ-ỹ]+)|(\|\s*\d+\s*\|)", content))
    if not has_numbered_steps:
        issues.append("Normal Course does not contain numbered steps (e.g., '1. ...' or table step index)")
    else:
        print("  -> Numbered steps detected.")

    # Check for embedded if/else logic in Normal Course
    normal_course_match = re.search(r"(normal course|luồng sự kiện chính)(.*?)(alternative course|luồng sự kiện thay thế|exceptions|luồng ngoại lệ)", content_lower, re.DOTALL)
    if normal_course_match:
        normal_text = normal_course_match.group(2)
        if " if " in normal_text or " else " in normal_text or " nếu " in normal_text or " ngược lại " in normal_text:
            issues.append("Normal Course contains embedded branching ('if' / 'else' / 'nếu'). Branching must be documented in Alternative Courses or Exceptions.")
        else:
            print("  -> Normal course flow is linear without forbidden embedded branching.")

    # 4. Check Alternative Courses
    print("[4/5] Checking Alternative Courses...")
    has_ac_id = bool(re.search(r"UC-[A-Z0-9]+-\d+\.(AC|LTT)\.\d+", content, re.IGNORECASE))
    if not has_ac_id:
        issues.append("Alternative Courses must have formatted ID (e.g., UC-MODULE-01.AC.1 or UC-MODULE-01.LTT.1)")
    else:
        print("  -> Alternative Course ID convention satisfied.")

    # 5. Check Exceptions
    print("[5/5] Checking Exceptions...")
    has_ex_id = bool(re.search(r"UC-[A-Z0-9]+-\d+\.(EX|NL)\.\d+", content, re.IGNORECASE))
    if not has_ex_id:
        issues.append("Exceptions must have formatted ID (e.g., UC-MODULE-01.EX.1 or UC-MODULE-01.NL.1)")
    else:
        print("  -> Exception ID convention satisfied.")

    # Summary
    print("------------------------------------------------------------")
    if issues:
        print(f"❌ AUDIT FAILED with {len(issues)} issue(s):")
        for idx, issue in enumerate(issues, start=1):
            print(f"   {idx}. {issue}")
        return False
    else:
        print("✅ AUDIT PASSED: 100% compliant with IIBA & Karl Wiegers UC Standard!")
        return True

def main():
    parser = argparse.ArgumentParser(description="Audit Use Case Markdown File (IIBA Standard)")
    parser.add_argument("--file", required=True, help="Path to the Use Case markdown file")
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

    success = audit_use_case(content, filepath=args.file)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()

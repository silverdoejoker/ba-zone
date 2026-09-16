import re
import sys
import argparse

def validate_use_case(content):
    print("\n--- Validating Use Case ---")
    issues = []
    
    # Check for the 16 fields
    fields = [
        "Use Case ID", "Use Case Name", "Created By", "Last Updated By", 
        "Date Created", "Date Last Updated", "Actor", "Description", 
        "Preconditions", "Postconditions", "Priority", "Frequency of Use", 
        "Normal Course of Events", "Alternative Courses", "Exceptions", 
        "Includes", "Special Requirements", "Assumptions", "Notes and Issues"
    ]
    
    for field in fields:
        if not re.search(rf"\*\*{field}[:\*]", content, re.IGNORECASE) and not re.search(rf"{field}[:]", content, re.IGNORECASE):
            issues.append(f"[C1-C20] Missing or incorrectly formatted field: {field}")
            
    # Check ID format
    id_match = re.search(r"\*\*Use Case ID:?\*\*\s*\|\s*(UC-[A-Z]+-\d+)", content)
    if id_match:
        print(f"✅ Found Use Case ID: {id_match.group(1)}")
    else:
        issues.append("[C3] Use Case ID is missing or does not follow format UC-<module>-<seq>")

    # Check for numbered Normal Course
    if re.search(r"\*\*Normal Course of Events:?\*\*", content):
        if not re.search(r"1\.\s+[A-Za-z]+", content):
            issues.append("[C12] Normal Course of Events does not seem to contain numbered steps (1., 2., etc.)")

    # Check for if/else in Normal Course
    normal_course_match = re.search(r"\*\*Normal Course of Events:?\*\*(.*?)\*\*Alternative Courses", content, re.DOTALL)
    if normal_course_match:
        normal_course_content = normal_course_match.group(1).lower()
        if "if " in normal_course_content or "else " in normal_course_content or "otherwise " in normal_course_content:
            issues.append("[C14] Normal Course contains if/else/otherwise logic (should be in Alternative/Exceptions)")

    # Check for Alternatives and Exceptions naming convention
    if not re.search(r"UC-[A-Z]+-\d+\.AC\.\d+", content) and not re.search(r"UC-[A-Z]+-\d+\.LTT\.\d+", content):
        issues.append("[C16] Alternative Courses missing or not following UC-XX.AC.N (or UC-XX.LTT.N) format")
        
    if not re.search(r"UC-[A-Z]+-\d+\.EX\.\d+", content) and not re.search(r"UC-[A-Z]+-\d+\.NL\.\d+", content):
        issues.append("[C17] Exceptions missing or not following UC-XX.EX.N (or UC-XX.NL.N) format")

    if issues:
        print("❌ Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ Use Case validation passed basic checks!")
    return len(issues) == 0

def validate_user_story(content):
    print("\n--- Validating User Story ---")
    issues = []
    
    # Check Core US Format
    if not re.search(r"\*\*As a\*\*\s+.+", content, re.IGNORECASE):
        issues.append("Missing or malformed 'As a' statement")
    if not re.search(r"\*\*I want to\*\*\s+.+", content, re.IGNORECASE):
        issues.append("Missing or malformed 'I want to' statement")
    if not re.search(r"\*\*So that\*\*\s+.+", content, re.IGNORECASE):
        issues.append("Missing or malformed 'So that' statement")
        
    # Check Generic Persona
    if re.search(r"\*\*As a\*\*\s+user", content, re.IGNORECASE):
        issues.append("Persona is too generic ('As a user'). Be specific.")

    # Check INVEST Table
    if "INVEST" not in content.upper():
        issues.append("INVEST Self-check section is missing")
        
    # Check Acceptance Criteria
    ac_count = len(re.findall(r"\*\*AC\d+:", content, re.IGNORECASE))
    if ac_count < 3:
        issues.append(f"Found {ac_count} Acceptance Criteria. Minimum 3 required (Happy, Edge, Negative).")

    # Check Gherkin syntax
    if not re.search(r"\*\*Given\*\*", content, re.IGNORECASE) or not re.search(r"\*\*When\*\*", content, re.IGNORECASE) or not re.search(r"\*\*Then\*\*", content, re.IGNORECASE):
        issues.append("Acceptance Criteria are missing Given/When/Then keywords.")

    if issues:
        print("❌ Issues Found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ User Story validation passed basic checks!")
    return len(issues) == 0

def main():
    parser = argparse.ArgumentParser(description="Audit Use Case or User Story Markdown files.")
    parser.add_argument("--file", required=True, help="Path to the markdown file to audit")
    parser.add_argument("--type", choices=["uc", "us", "auto"], default="auto", help="Document type to validate")
    
    args = parser.parse_args()
    
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file {args.file}: {e}")
        sys.exit(1)

    doc_type = args.type
    if doc_type == "auto":
        # Heuristic detection
        if "As a" in content and "I want to" in content:
            doc_type = "us"
        elif "Normal Course" in content or "Use Case ID" in content or "Preconditions" in content:
            doc_type = "uc"
        else:
            print("Could not auto-detect document type. Please specify --type uc or --type us.")
            sys.exit(1)
            
    print(f"Auditing file: {args.file} as {doc_type.upper()}")
    
    if doc_type == "uc":
        success = validate_use_case(content)
    else:
        success = validate_user_story(content)
        
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()

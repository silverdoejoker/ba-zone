---
name: us-uc-writer
description: |
  Generate Use Case (UC) and User Story (US) specifications in English or Vietnamese Markdown following IT BA standards (Karl Wiegers / IIBA, extended / Alistair Cockburn). 
  Use whenever a BA needs to scope, analyze, document, refine, or review a Use Case or a User Story.
  The skill enforces Cockburn's guidelines (coffee-break test, goal levels) for UCs and the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable) + Gherkin syntax (Given-When-Then) for USs.
  The skill supports 2 output languages via `output_language` variable (default: `en`, can be set to `vi`).
author: Phúc NT @ BA Zone (Synthesized)
---

# User Story & Use Case Writer — Skill for IT Business Analysts
> Based on works by **Phúc NT** · BA Zone · Digital School

This skill helps IT BAs **scope, analyze, and document Use Cases (UCs) and User Stories (USs)** in English or Vietnamese Markdown following standard templates and best practices (IIBA, Alistair Cockburn).

## When to use this skill
Trigger this skill whenever the user needs to:
- Draft a new UC or US from a feature description, BRD, or PRD.
- Refine or review an existing UC/US.
- Split a large feature into smaller UCs or USs.
- Write a specific section of a UC (Normal Course, Alternative Course, Exceptions) or add Acceptance Criteria (AC) to a US.
- Validate a UC or US against quality checklists.

## Session variable: `output_language`
This skill uses a session variable to control the language of the output artifact:
- `output_language=en` (English - default)
- `output_language=vi` (Vietnamese)

**Rules:**
1. The conversational language between skill and user should always match the user's input language, regardless of `output_language`.
2. `output_language` ONLY controls the language of the final generated UC/US document (field labels, content, steps, etc.).
3. Ask for the preferred output language if not specified in the first prompt.

---

## Workflow: 4 Steps

### Step 1: Classify input and pick a mode
Identify if the user wants to write a **Use Case (UC)** or a **User Story (US)**.
If vague, **ASK before writing**: 
1. Are we writing a Use Case or a User Story?
2. Who is the primary actor / persona?
3. What is the specific goal?
4. Which system/module does this belong to?

### Step 2: Scope the Requirement
- **For UCs:** Apply the Coffee-break test (user-goal level, 1 actor, 1 goal, 1 session).
- **For USs:** Ensure the goal is small enough (Estimable, Small) and provides clear value (Valuable). Suggest splitting if it covers multiple CRUD operations or has too many ACs.

### Step 3: Write the Content

#### Option A: Writing a Use Case (UC)
Generate ONE SECTION GROUP at a time, then **STOP and ask the user to confirm** before continuing.
**Template (16 fields):**
- **Group 1:** Use Case ID, Name (Verb + Noun), Created By/Date, Last Updated By/Date, Actor, Description.
- **Group 2:** Preconditions, Postconditions, Priority, Frequency of Use.
- **Group 3:** Normal Course of Events (Numbered list, alternating Actor/System, no embedded if/else).
- **Group 4:** Alternative Courses (`UC-XX.AC.1`), Exceptions (`UC-XX.EX.1`).
- **Group 5:** Includes, Special Requirements, Assumptions, Notes and Issues.

#### Option B: Writing a User Story (US)
**Template:**
1. User Story Statement:
   - **As a** [specific persona]
   - **I want to** [specific, measurable action]
   - **So that** [clear business value]
2. Acceptance Criteria (Minimum 3: Happy path, Edge case, Negative path). Use Gherkin format:
   - **Given** [precondition]
   - **When** [action]
   - **Then** [measurable result]
3. Notes (Dependencies, Assumptions, Open Questions).

### Step 4: Validate against Quality Checklists
**ALWAYS run the checklist BEFORE handing over the final document.**

#### Validation for Use Cases (20-point checklist)
- **Scope & Identification:** Name is verb+object, user-goal level, unique ID, 1 primary actor, clear system boundary.
- **Actor & Context:** Specific role, Description has WHY+WHAT+OUTCOME, Frequency quantified.
- **Pre/Post Conditions:** Verifiable preconditions, Postconditions cover all system changes, Preconditions != Assumptions.
- **Normal Course:** Numbered, 1 action/step, alternates Actor/System, no nested if/else, complete flow.
- **Alternative & Exception:** AC specifies "at step N", Exception has trigger+response+final state, common failure modes covered.
- **Completeness:** Includes are valid, Special Req are non-functional.

#### Validation for User Stories (INVEST + AC)
- **INVEST:** Independent, Negotiable, Valuable, Estimable, Small, Testable.
- **AC Quality:** Minimum 3 ACs, Given-When-Then format, measurable outcomes, covers happy/edge/negative paths, no technical logic/UI details in ACs.

Output a summary table of the validation (e.g. `Item | Status | Note` with ✅ ❌ ⚠️ markers) before finalizing the output document.

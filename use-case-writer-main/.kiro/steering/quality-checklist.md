---
inclusion: fileMatch
fileMatchPattern: "**/references/quality-checklist.md"
---

# Quality Checklist Steering

When the quality checklist is in context, run the full 20-point validation:

## Checklist Groups

### A. Scope & Identification (C1-C5)
- C1: UC Name = "verb + object", active voice
- C2: User-goal level (coffee-break test passes)
- C3: UC ID unique + follows naming convention
- C4: Exactly 1 primary actor + 1 clear goal
- C5: System boundary is clear

### B. Actor & Context (C6-C8)
- C6: Actor is specific role/class (not "User")
- C7: Description has WHY + WHAT + OUTCOME
- C8: Frequency is quantified (number + time unit)

### C. Pre/Post Conditions (C9-C11)
- C9: Preconditions are verifiable
- C10: Postconditions cover all state changes
- C11: No precondition/assumption confusion

### D. Normal Course (C12-C15)
- C12: Numbered, one action per step
- C13: Actor/System alternating with clear subjects
- C14: No embedded if/else/loop
- C15: Flow complete from trigger to postcondition

### E. Alternative & Exception (C16-C18)
- C16: Each AC has "at step N" + condition + rejoin point
- C17: Each Exception has trigger + response + final state
- C18: Common failure modes covered (validation, business rule, external service, auth, concurrency)

### F. Completeness (C19-C20)
- C19: Includes point to existing UCs
- C20: Special Requirements are non-functional only

## Output Format

Always output a validation table:
```
| # | Item | Status | Note |
|---|------|--------|------|
| C1 | ... | ✅/❌/⚠️ | ... |
```

Followed by a summary: X/20 ✅ + Y ⚠️. State if UC is ready or needs fixes.

#[[file:references/quality-checklist.md]]

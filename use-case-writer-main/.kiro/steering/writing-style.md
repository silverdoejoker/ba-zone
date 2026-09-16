---
inclusion: fileMatch
fileMatchPattern: "**/references/writing-style.md"
---

# Writing Style Steering

When the writing style guide is in context, enforce these conventions:

## Core Rules

1. **Active voice + present tense** — "Learner clicks" not "is clicked by" or "will click"
2. **Clear subject** — every step starts with Actor name or "System" (Subject + Verb + Object)
3. **One step = one action** — split if "and" connects different-kind actions
4. **No vague verbs** — replace Manage/Handle/Do/Get/Use with specific verbs (Create/Validate/Submit/Retrieve/Apply)
5. **No implementation details** — describe WHAT not HOW (no API endpoints, no DB table names, no component names)
6. **Consistent numbering** — Normal Course: 1,2,3; AC sub-steps: 5a,5b,5c; Exceptions: UC-XX.EX.N
7. **Bold UI elements** — use actual on-screen labels in bold: "clicks the **Enroll Now** button"
8. **No vague words** — replace "sometimes/may/if needed/valid/appropriate/quickly" with specifics
9. **Don't embed business rules** — reference by BR-ID, keep steps about flow
10. **Length guidelines** — UC Name 3-7 words, Description 2-4 sentences, Normal Course 5-15 steps, each step <30 words

## Anti-Patterns to Catch

- UC as pixel-by-pixel UI spec
- Mixing actor and system in one step
- Skipping system responses
- Embedded conditional logic in Normal Course
- Vague triggers
- Postcondition written as action instead of state
- UC with 2 primary actors
- Vague "System processes"
- Repeating Description in Normal Course
- Forgetting failure modes

#[[file:references/writing-style.md]]

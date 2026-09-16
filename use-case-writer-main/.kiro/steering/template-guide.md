---
inclusion: fileMatch
fileMatchPattern: "**/references/template-guide.md"
---

# Template Guide Steering

When the template guide is in context, apply these rules for filling UC fields:

## Field-Filling Standards

- **UC ID**: Format `UC-<module>-<seq>`, pad to 2-3 digits
- **UC Name**: 3-7 words, "Verb + Object", no vague verbs (manage, handle, process)
- **History**: Always include Created By + Date, Last Updated By + Date in YYYY-MM-DD
- **Actor**: Primary (initiator) + Secondary (supporting systems). Never "User" — use specific roles
- **Description**: Must answer WHY + WHAT + OUTCOME in 2-3 sentences
- **Preconditions**: Verifiable boolean conditions, numbered. Not motivations, not business rules
- **Postconditions**: System STATE after success (not actions). Verifiable via DB/API
- **Priority**: Use project's scheme (MoSCoW or High/Medium/Low) + one-sentence justification
- **Frequency**: Specific numbers with time units + peak info
- **Normal Course**: Numbered, one action/step, Actor/System alternating, active voice, present tense
- **Alternative Courses**: ID format `UC-XX.AC.N`, starts with "At step Y, if [condition]", sub-numbered Na/Nb, states where to rejoin
- **Exceptions**: ID format `UC-XX.EX.N`, needs trigger + response + final state
- **Includes**: Only for logic reused across multiple UCs, must reference existing UC IDs
- **Special Requirements**: Non-functional only (performance, security, reliability, compliance)
- **Assumptions**: Believed true but not verified — distinct from preconditions
- **Notes and Issues**: Format `[TBD-N] | Owner | Due | Resolution`

#[[file:references/template-guide.md]]

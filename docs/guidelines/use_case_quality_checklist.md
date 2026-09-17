# Quality Checklist — 20 Points to Validate a Use Case
> Bảng kiểm định chất lượng 20 điểm cho Use Case · **BA Zone** · Karl Wiegers & Alistair Cockburn Standards  
> Biên soạn bởi **Phúc NT** · Digital School · BA Zone

Run this checklist BEFORE handing over a UC. Each item has: definition, how to check, pass/fail examples.

## How to use

1. After writing the UC, walk through items C1-C20.
2. Mark Status: ✅ Pass / ❌ Fail / ⚠️ Needs review.
3. If Fail → fix it or flag it to the user.
4. Output a summary table at the end.

---

## GROUP A: Scope & Identification (C1-C5)

### C1. UC Name follows "verb + object", active voice
- **Definition**: UC Name starts with an active verb + an object noun, with no actor name embedded.
- **Pass**: "Enroll in course", "Approve mentor session request", "Issue completion certificate".
- **Fail**: "Enrollment" (no verb), "Learner books session" (actor included), "Manage courses" (vague verb).

### C2. UC is at user-goal level (passes the coffee-break test)
- **Definition**: After completing the UC, the actor can stop and take a break — the goal is achieved.
- **Pass**: "Enroll in course" (learner has course access), "Book mentor session" (session request submitted).
- **Fail**: "Verify OTP" (too small — just a sub-step), "Manage entire customer lifecycle" (too large).

### C3. UC ID is unique and follows naming convention
- **Definition**: ID is unique in the project and matches `UC-<module>-<seq>`.
- **Pass**: `UC-AUTH-01`, `UC-LEARN-03`.
- **Fail**: `UC1`, `UseCase_CourseEnroll`.

### C4. Exactly 1 primary actor + clear business goal
- **Definition**: One UC has 1 primary actor (the initiator) and 1 specific goal.
- **Pass**: Primary: Learner. Goal: enroll in a course and gain immediate access.
- **Fail**: Primary: Learner + HR Manager (2 actors). -> Split into 2 UCs.

### C5. System boundary is clear
- **Definition**: The UC describes interaction with one specific system, not multiple systems mixed together.
- **Pass**: All steps refer consistently to the core platform system.

---

## GROUP B: Actor & Context (C6-C8)

### C6. Actor is a specific role/class
- **Pass**: "Learner (Premium subscriber)", "Mentor (Certified, active account)".
- **Fail**: "User", "Person", "Actor 1".

### C7. Description answers WHY + WHAT + OUTCOME
- **Pass**: Must state why the actor needs it, what they do, and what the final verifiable outcome is.
- **Fail**: "This UC is about issuing certificates." (missing WHY and OUTCOME).

### C8. Frequency of Use is quantified
- **Pass**: "~500 enrollments/day platform-wide; peak ~100/hour during promotional campaigns".
- **Fail**: "Frequent", "Often" (no quantitative estimate).

---

## GROUP C: Pre/Post Conditions (C9-C11)

### C9. Preconditions are verifiable
- **Pass**: "Learner progress = 100%", "Payment Gateway is reachable".
- **Fail**: "Learner is motivated to learn" (unverifiable motivation).

### C10. Postconditions cover the success state + all changes
- **Pass**: Describes data changes, external state updates (emails, notifications), and UI state changes.
- **Fail**: Only "Enrollment succeeded" without any state details.

### C11. Preconditions are not confused with Assumptions
- **Precondition**: MUST BE TRUE, verifiable by the system.
- **Assumption**: BELIEVED to be true (e.g., user has basic computer skills).

---

## GROUP D: Normal Course (C12-C15)

### C12. Numbered list, one action per step
- **Pass**: Numbered 1, 2, 3... with a single distinct action per step.
- **Fail**: "Learner enters topic and clicks Send and waits for confirmation" (3 actions combined).

### C13. Alternates Actor / System with clear subjects
- **Pass**: Clear step flow alternating between Actor action and System response.
- **Fail**: Sequence of only Actor actions without any System feedback.

### C14. NO embedded if/else/loop in the Normal Course
- **Pass**: Linear happy path only.
- **Fail**: "If premium do X, else do Y" embedded in main flow -> Move branches to Alternative Courses.

### C15. Flow runs from trigger to postcondition
- **Pass**: Step 1 is the user trigger; final step produces the promised postcondition.

---

## GROUP E: Alternative & Exception (C16-C18)

### C16. Each AC specifies "at step N" + condition
- **Format**: `UC-XX.AC.N`: At step [N], if [Condition], then perform [Steps], rejoin at step [M] or exit.

### C17. Each Exception has trigger + response + final state
- **Three mandatory parts**: (1) Trigger condition, (2) System response/error message, (3) Safe rollback state.

### C18. Common failure modes are covered
- Validation error, business rule violation, external service timeout, concurrency conflict, network drop.

---

## GROUP F: Completeness (C19-C20)

### C19. Includes (if any) point to existing UCs
- Referencing valid `UC-MODULE-XX` specs that exist in the project registry.

### C20. Special Requirements don't duplicate functional requirements
- Non-functional requirements only (latency < 2s, 99.9% uptime, data retention regulations).

---
inclusion: fileMatch
fileMatchPattern: "**/references/examples-edtech.md"
---

# EdTech Examples Steering

When the examples file is in context, use these as reference patterns:

## Available Examples

1. **UC-LEARN-01: Enroll in a Digital School course** — Learner-facing, payment integration, async LMS fallback
2. **UC-MENTOR-03: Approve learner 1-on-1 mentor session request** — Mentor-facing, concurrency, quota enforcement, calendar integration

## Patterns to Learn From

- **Async fallback**: Payment succeeds but downstream system fails → never roll back payment, retry asynchronously (UC-LEARN-01.EX.4)
- **Quota enforcement at decision time**: Check quota when mentor approves, not just at request time (UC-MENTOR-03.EX.4)
- **Concurrency conflict**: Multi-actor queue where status can change between view and action (UC-MENTOR-03.EX.1)
- **Voucher validation**: Always server-side, never expose remaining counts to client
- **Business rules by reference**: Use BR-IDs instead of inlining logic in Normal Course steps

## Structural Patterns Both Examples Share

- 1 primary actor + clear secondary actors
- Description with WHY + WHAT + OUTCOME
- Verifiable preconditions (not motivations)
- Postconditions as state changes
- 9-10 step Normal Course alternating Actor/System
- 2 Alternative Courses + 3-4 Exceptions
- Special Requirements that are non-functional only
- Notes with TBDs including owner + due date

#[[file:references/examples-edtech.md]]

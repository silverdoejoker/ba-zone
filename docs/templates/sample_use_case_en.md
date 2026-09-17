# Use Case Specification: UC-AUTH-01 - Register Student Account
> Sample Reference · **BA Zone** (Karl Wiegers / IIBA BABOK Standard)

| Field | Details |
|---|---|
| **Use Case ID** | `UC-AUTH-01` |
| **Use Case Name** | Register Student Account |
| **Created By & Date** | Phúc NT · 2026-09-16 |
| **Last Updated By & Date** | Phúc NT · 2026-09-16 |
| **Primary Actor** | Prospective Student |
| **Description** | A prospective student registers for a new account on the portal to enroll in courses and access learning resources. |
| **Preconditions** | 1. User has access to the Internet and a valid email address.<br>2. User does not already have an active account with the provided email. |
| **Postconditions** | 1. A new student record is created in the database.<br>2. An activation email with a verification code is dispatched. |
| **Priority** | High (Critical user onboarding flow) |
| **Frequency of Use** | ~300 registrations per day |

### Normal Course of Events (Happy Path)

| Step | Actor Action | System Response |
|---|---|---|
| 1 | Prospective Student navigates to the registration page. | System displays the registration form with required input fields. |
| 2 | Prospective Student enters valid registration details and submits the form. | System validates form inputs against data integrity rules. |
| 3 | | System creates a pending student record and dispatches an OTP verification code via email. |
| 4 | Prospective Student enters the received verification OTP. | System verifies the OTP and activates the student account. |
| 5 | | System redirects Prospective Student to the welcome dashboard. |

### Alternative Courses

#### UC-AUTH-01.AC.1: Register via Google SSO
- **Branch Point**: At step 1 of Normal Course.
- **Condition**: Prospective Student selects "Continue with Google".
- **Flow**:
  1. System redirects Actor to Google OAuth authentication window.
  2. Actor authorizes Google profile permissions.
  3. System retrieves verified email and creates active account automatically.
- **Rejoin / Exit**: Rejoin Normal Course at step 5.

### Exceptions

#### UC-AUTH-01.EX.1: Email Already Registered
- **Trigger**: At step 2, System detects email is already bound to an active account.
- **System Response**: System displays alert: "Email is already registered. Please sign in or reset your password."
- **Final State**: No new account created. Actor remains on registration page.

### Supplemental Specifications

| Field | Details |
|---|---|
| **Includes** | UC-AUTH-02: Verify OTP |
| **Special Requirements** | - **Performance**: Form submission response within 1.5 seconds.<br>- **Security**: Passwords hashed using bcrypt; all traffic encrypted via TLS 1.3. |
| **Assumptions & Notes** | External email delivery gateway has 99.9% uptime SLA. |

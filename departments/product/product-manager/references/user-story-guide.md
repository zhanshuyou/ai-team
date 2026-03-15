# User Story Writing Guide

## Format

```
As a [type of user],
I want [an action/feature],
so that [benefit/value].
```

## Acceptance Criteria (Given/When/Then)

Each user story must include acceptance criteria:

```
Given [precondition],
When [action],
Then [expected result].
```

## INVEST Checklist

Good user stories are:

- **I**ndependent — Can be developed in any order
- **N**egotiable — Details can be discussed
- **V**aluable — Delivers value to the user
- **E**stimable — Team can estimate the effort
- **S**mall — Completable within one sprint
- **T**estable — Clear pass/fail criteria

## Priority Levels

| Priority | Meaning | Guideline |
|----------|---------|-----------|
| P0 | Must have | Product does not work without it |
| P1 | Should have | Important but not blocking |
| P2 | Nice to have | Enhances experience |
| P3 | Future | Backlog for later consideration |

## Example

**Story**: As a new user, I want to sign up with my email, so that I can access the platform.

**Acceptance Criteria**:
- Given I am on the landing page, When I click "Sign Up", Then I see a registration form
- Given I fill in a valid email and password, When I click "Submit", Then my account is created and I receive a confirmation email
- Given I enter an already-registered email, When I click "Submit", Then I see an error message "Email already in use"

## Story Sizing Reference

| Size | Points | Example |
|------|--------|---------|
| XS | 1 | Change button label |
| S | 2 | Add form validation |
| M | 3-5 | New CRUD feature |
| L | 8 | New integration |
| XL | 13+ | Should be broken down |

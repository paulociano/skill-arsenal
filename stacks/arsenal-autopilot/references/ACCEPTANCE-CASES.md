# Arsenal Autopilot — Acceptance Cases

These cases validate routing and governance. They are not executable tests unless a future runtime compiles them into checks.

## Case 1 — Batch of external repositories
**Input:** user provides 8 repositories and asks to evaluate/import useful skills.

**Expected:**
- trigger `arsenal-autopilot`;
- read Arsenal index first;
- triage all sources;
- deepen only plausible novelty;
- produce capability ledger when overlap is material;
- create fewer skills than repositories when appropriate;
- publish evaluation even if some/all candidates are rejected.

## Case 2 — One simple external skill
**Input:** user provides one small SKILL.md and asks to evaluate it.

**Expected:**
- prefer `evaluate-and-import-skill`;
- do not invoke full Autopilot machinery unless ownership/overlap becomes complex.

## Case 3 — Runtime-heavy ecosystem
**Input:** repository offers swarm CLI, hooks, installers, memory DB and hundreds of skills.

**Expected:**
- classify technical/runtime surface separately from portable methodology;
- do not run installer;
- inspect only relevant files;
- reuse existing owners where possible;
- do not pretend external runtime exists.

## Case 4 — Duplicate methodology with one new idea
**Input:** external repo overlaps TDD, code review and debugging but adds a distinct verified practice.

**Expected:**
- do not clone TDD/review/debugging skills;
- route overlapping fragments to existing owners;
- create/update only the distinct capability if incremental value is demonstrable.

## Case 5 — No adoptable capability
**Input:** repository is useful software but has no portable method beyond existing Arsenal coverage.

**Expected:**
- create no artificial skill;
- record classification, security/dependency notes and decision in `evaluations/`;
- leave index unchanged except when an existing description genuinely needs correction.

## Near miss — ordinary Arsenal task
**Input:** `arsenal: melhore este dashboard`.

**Expected:**
- do not trigger Autopilot;
- route to dashboard/design/implementation skills normally.

## Completion checks
- every source classified;
- every adopted capability has one canonical owner;
- no duplicate trigger introduced knowingly;
- no external installer executed for evaluation;
- index updated iff routing changed;
- evaluation published;
- read-after-write performed after final material change.

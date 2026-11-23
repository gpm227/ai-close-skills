---
name: improve-skill
description: "Investigate an actual failed skill output, reproduce the miss on a known release, and prepare the smallest tested change for the skill owner. Use for a reported regression or failed output check; use standardize-task-instructions for a new workflow."
---

# Improve a skill

Start with the original request, its disappointing answer, what should have happened, and a copy of the instructions you can actually inspect. A chat excerpt and the current instruction text are enough to investigate. Capture the run ID, release and evaluator verdict when available. For a personal skill without releases, save the exact current text as a dated baseline, give the proposed revision a separate name, and leave the original run's version unknown unless you can establish it. Keep user satisfaction, technical checks, delivery and business outcome separate. Retain sensitive source material in its authorized location; use cleared reproductions for wider review.

1. Attribute the artifact to its producing release. If attribution is unknown, say so and reproduce privately on a known version before proposing an edit. Preserve the original output and freeze the owner-approved criteria with stable identifiers before writing the fix. If comparison depends on missing evidence, name precisely what would resolve it.
2. Inspect the smallest relevant artifact and contract. Reproduce the task on the old version with the original inputs, tool access and a comparable configuration. If a failure is intermittent, record attempts and reproduction frequency. Classify the cause as source input, context/tool, check, ambiguous standard or skill instructions. A failed evaluator may be wrong; verify its claim against the owner's benchmark. Only change the responsible component.
3. For a skill gap, propose the smallest general rule whose scope matches the failure. Keep the failing input as a future regression. Reserve a different input and a case that previously passed. Keep expected answers out of worker instructions. Where feasible, exercise the candidate in isolation on the same input as the old version and have an independent worker run the held-out case. Cite the actual output or location per criterion. Mark missing evidence unknown.
4. Give the owner the exact proposed replacement and where it belongs, old and proposed behavior side by side, revision identifiers, results of each test and any untested criteria. For a shared release, put this in the private change request. A personal owner can keep the same evidence beside the two instruction copies. If only the checker failed, propose its correction and tests instead. A hand-written example or an unrun plan supports a candidate, not a verified fix.
5. The owner decides release. After applying the change, verify which version a fresh session serves, repeat the check and record actual behavior. Use a second person when available; a solo owner can run this check and label it self-verified. Record any later business outcome separately. Keep the last good text so the owner can restore it if the new rule regresses.

[Distinguish a broken evaluator from a broken skill](examples/practice.md).

## Try it on your work

The instructions that ran, one input, the actual result and what should have happened.

> Find why the skill missed, propose the smallest correction and check it against both the failure and a case that used to work.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `improve-skill.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

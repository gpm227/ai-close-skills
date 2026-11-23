---
name: improve-skill
description: "Investigate an actual failed skill output, reproduce the miss on a known release, and prepare the smallest tested change for the skill owner. Use for a reported regression or failed output check; use standardize-task-instructions for a new workflow."
---

# Improve a skill

Obtain the input and output as originally used, run ID and skill release, applicable owner standard, evaluator verdict (if any), and the observed problem with evidence. Keep user satisfaction, technical checks, delivery and business outcome separate. Retain sensitive source material in its authorized location; use cleared reproductions for wider review.

1. Attribute the artifact to its producing release. If attribution is unknown, say so and reproduce privately on a known version before proposing an edit. Preserve the original output and freeze the owner-approved criteria with stable identifiers before writing the fix. If comparison depends on missing evidence, name precisely what would resolve it.
2. Inspect the smallest relevant artifact and contract. Reproduce the task on the old version with the original inputs, tool access and a comparable configuration. If a failure is intermittent, record attempts and reproduction frequency. Classify the cause as source input, context/tool, check, ambiguous standard or skill instructions. A failed evaluator may be wrong; verify its claim against the owner's benchmark. Only change the responsible component.
3. For a skill gap, propose the smallest general rule whose scope matches the failure. Keep the failing input as a future regression. Reserve a different input and a case that previously passed. Keep expected answers out of worker instructions. Where feasible, exercise the candidate in isolation on the same input as the old version and have an independent worker run the held-out case. Cite the actual output or location per criterion. Mark missing evidence unknown.
4. Prepare a private change request with exact diff, old and proposed behavior side by side, release IDs, regression, held-out and preservation results, unresolved risks, proposed version and owner. If only the checker failed, propose its correction and tests instead. Do not mark the skill fixed based on a hand-written example or a test plan.
5. The owner decides release. After approval and release, have a second person verify the served version in a fresh session, run the check, record actual behavior and separately record any later business outcome. Use a forward release restoring the last good rule if a regression warrants rollback under the team's release procedure.

[Distinguish a broken evaluator from a broken skill](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

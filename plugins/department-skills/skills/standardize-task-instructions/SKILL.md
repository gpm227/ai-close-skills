---
name: standardize-task-instructions
description: "Turn a recurring task, its source inputs and an accepted output into reusable instructions and an acceptance test. Use to document a departmental SOP or design a new skill from examples; use improve-skill for a failure in an existing released skill."
---

# Write reusable task instructions

Start with a representative input and an example the process owner accepted. If the task only exists in someone's head, ask them to walk through the last instance: what arrived, what they checked, what decision they made, what they handed over and to whom. Turn that account into a provisional SOP and a small sample result. Highlight the first decision another operator would have to guess and give the owner a concrete choice to settle it. Label a reconstructed example and its expected answer as proposed until the owner confirms them.

1. Define the task boundary: start condition, inputs, permission, endpoint and audience. Distinguish required data from optional context. Record the source of each material rule (owner decision, policy or example). A single example can illustrate an implementation; ask before elevating an accidental detail to policy.
2. Mark each item as invariant, variable input, default, or owner judgment. If two requirements conflict, cite both and explain which part of the job depends on the decision. Continue unaffected work and label any conditional result. Never silently choose one priority.
3. Write a compact instruction with decision branches where outcomes differ, evidence to retain, exact output structure, and recovery behavior for missing, invalid or contradictory input. Separate an output's formatting from the substantive decision the output must encode. Include a realistic invocation that a new operator can use without hidden chat history.
4. Freeze observable assertions for the normal case, one materially different or unseen input and one exception before assessing an output. Keep the expected evidence with the grader, separate from the worker's instructions for a fresh evaluation. Replay on the original; ask an independent worker to use only the candidate instructions and a reserved input when available.
5. Deliver the SOP, invocation, fixture inputs, expected outputs and a short verification record with input, instruction revision, observed artifact, verdict per check and unresolved owner decisions. Clearly distinguish a designed test from a run. The owner approves the rule before it becomes policy.

[Turn a weekly summary into a reproducible SOP](examples/practice.md).

## Try it on your work

A walkthrough of the last time you did the task. Add an accepted result if available.

> Write instructions another person can follow and a check they can run on the result. Identify the judgment calls that still need the owner's input.

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

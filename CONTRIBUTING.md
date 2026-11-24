# Contributing

Two kinds of contribution are welcome: a skill that is missing, and evidence that an existing one produced a bad answer.

## Report a bad answer

The most useful report contains four things:

1. The input you used, or a version of it with the sensitive parts removed.
2. What came back.
3. What should have come back.
4. What the wrong answer would have cost you.

"The copy was generic" is not a report. "It wrote a 60% time saving we cannot support, and I would have published it" is.

## Request a skill

Open an issue with the job, the input someone starts with, the artifact they need at the end, and how they would know it worked. If you cannot describe the check, the job is not ready to be a skill.

## Add a skill

1. Copy [docs/SKILL-TEMPLATE.md](docs/SKILL-TEMPLATE.md) to `skills/<name>/SKILL.md`.
2. Name it after the job, in kebab case: `cold-email`, not `outreach-master`.
3. Write the description as a routing sentence. Start with "When the user wants…", then name the situations, then point neighbouring jobs at their own skill. It is the only part a router reads.
4. Keep the five house sections: Bring, What comes back, The trap and the check, Company hooks, Related skills.
5. Add the row to `SKILLS.md` with a status.
6. Run `bash tools/check.sh`. It must pass.

## What makes a skill good here

| Test | Why |
| --- | --- |
| The trap names an actual wrong answer | "Be specific" helps nobody. "It will invent a percentage" is checkable |
| The check takes under a minute | A check nobody runs is decoration |
| The output format is a shape, not a lecture | Tables and headings the user can paste |
| It says what it cannot do | The limit is part of the instruction |
| It asks only questions that change the deliverable | Every extra question loses a user |

## Review

One reviewer approves a new skill, and the reviewer must have run it on a real input. A skill that has only been read is unproven.

For a change to an existing skill, include the case that failed before and the case that already worked. A fix that breaks the previously good case is not a fix.

## Security and data

- Never put customer names, prices or private numbers in a skill. They belong in the context document or `custom/`.
- Never write instructions that tell an agent to publish, send, delete or spend without an explicit confirmation step.
- Skills that touch live accounts must name the confirmation in the skill body, not rely on the model's judgement.

## Mentioning tools

Name a tool only when the job needs it, and describe it in two clauses: what it is and when to reach for it. No placement is for sale, and no skill is edited to prefer a vendor. If you maintain a tool, say so in the same sentence.

---
name: skill-name-in-kebab-case
description: "When the user wants <the job>, or asks <the adjacent ask>: <the three or four situations this covers>. For <neighbouring job>, see <skill>. For <other neighbour>, see <skill>."
metadata:
  version: 0.1.0
---

# Human readable title

<One paragraph. Who you are for this job, and the decision or artifact at the end of it.>

## Bring

| What | Minimum to start | What makes the answer good |
| --- | --- | --- |
| | | |

## What comes back

- <the deliverable, item by item, in the order the reader will use it>

## The trap, and the check

<The specific mistake a plain request makes. Not "AI can be vague" — the actual wrong answer, with an example.>

**Check:** <the test the user can run on the answer in under a minute.>

## Read the company context first

Read `.agents/close-context.md` if it exists, then `.agents/product-marketing.md`, then the `.claude/` equivalents. Use what is there and ask only for gaps.

## How to do the job

1. <step>
2. <step>

## Output format

<exact shape of the reply: headings, table columns, word limits, what to leave out>

## Questions that change the answer

1. <question whose answer changes the deliverable>

## Company hooks

- House rules: read `custom/<skill-name>.md` and apply it after this file. Where the two conflict, the house rule wins on method and this file wins on nothing else.
- Facts, claims and pricing come from the context doc, never from the model.
- <one skill-specific hook, e.g. a framework, a banned phrase list, a template>

## Related skills

- **<skill>**: <when to switch to it instead>

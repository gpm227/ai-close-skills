# AI Close Skills

Give your team a way to do a job with AI and judge whether the work is good enough to use. Start with the result you need. Each skill is a Markdown file you can bring into your own AI workspace.

## What do you need to do?

| I need to… | Bring this | Get this |
| --- | --- | --- |
| [Tell whether orders are actually down this month](plugins/department-skills/skills/period-report/SKILL.md) | Daily totals for this month and last month, plus the reporting cutoff | A like-for-like comparison showing the dates, totals, and change. |
| [Fix a mistake the team keeps making with AI](plugins/department-skills/skills/improve-skill/SKILL.md) | The skill version, an output that missed the mark, and evidence of what should have happened | A proposed change the team lead can review, with a test for the next time someone does the job. |

## Try it on a report

You’re 18 days into May. The team has 180 orders. April closed at 300. Someone looking at those two numbers could report a 40% decline. But April also had 180 orders through the 18th. Orders are flat. The decision to investigate a drop turns on which dates you compare.

1. Copy the [reporting skill](plugins/department-skills/skills/period-report/SKILL.md) into a fresh conversation in Claude or your preferred LLM.
2. Attach the [sample order export](proof/a/daily.csv) and ask: **How did orders change month over month through May 18, 2026?**
3. Check the answer. It should compare May 1–18 with April 1–18, show 180 orders in each period, and report 0% change.

To verify the result locally, save the JSON object from the answer as `actual-a.json` in a local copy of this repo. Run `python3 proof/check.py a actual-a.json`. The checker names any field that differs from the expected result. There’s a [second export](proof/b/daily.csv) to try in a fresh conversation.

## What we’re building for outbound teams

A rep needs a one-sheet for a buyer meeting. To produce one they can send, the writer needs to know who the buyer is, what the company can promise, which claims it can prove, and how the company sounds. The next outbound email needs much of the same material. Define it once and both jobs get better inputs.

The [outbound catalog](CATALOG.md) lays out 21 planned skills, from defining an ideal customer to writing the one-sheet and evaluating a campaign. Each entry names the deliverable. The two skills at the top of this page are available today.

## Bring it into your company

Keep your rules, examples, and approved changes in a private repo your company owns. When someone spots a recurring error, the team lead can review a correction and the evidence behind it. Once released, the next person can use what the team learned. The [deployment guide](company/DEPLOY.md) covers that process. The [run record](company/run-record.json) gives you a place to connect a prompt and its output to cost and the business result when you can observe them.

For help putting a departmental workflow into practice, visit [AI Close](https://aiclosehq.com/).

## Contribute a case

A useful contribution can be as small as one example where the answer looked reasonable and would have led someone to the wrong decision.

- **Found a failure?** [Open an issue](https://github.com/gpm227/ai-close-skills/issues/new) with a shareable input, the output you got, the result you expected, and why the difference matters.
- **Have a skill your team uses?** Open a pull request with the instructions, an example someone else can run, and a way to tell whether it worked. Use synthetic or cleared examples so others can reproduce the work.
- **See a gap in the catalog?** Tell us what someone is trying to get done, what they start with, and what they need in hand when they finish.

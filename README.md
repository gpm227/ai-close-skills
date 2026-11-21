# AI Close Skills

A library of business workflows for your AI workspace. Pick the result you need, open the skill file, and give your model the instructions and inputs.

[Browse the skill index](#skill-index) · [Run an example](#agency-reporting-example) · [Contribute a case](#contribute-a-case)

## Skill index

| Category | What someone needs to get done | Where to start |
| --- | --- | --- |
| Agency | Give a client an accurate month-to-date performance update. | [Compare matching periods](plugins/department-skills/skills/period-report/SKILL.md) · available |
| Financial and cash services | Give sales a list of institutions that fit the offer and operate inside its service area. | [Target-account lists and buying contacts](CATALOG.md) · planned, §4.1–4.2 |
| Marketing and growth | Turn an approved offer and customer proof into a one-sheet a rep can send or an email sequence the team can run. | [One-sheets, outbound email, and sequences](CATALOG.md) · planned, §3.7, §3.3, §4.3 |
| Analytics | Determine whether a metric moved and show the dates and totals behind the conclusion. | [Run the reporting example](#agency-reporting-example) · available with a Python check |
| Fast-casual restaurants | Tell an operator whether orders at a location are up or down through the same day last month. | [Use the period report](plugins/department-skills/skills/period-report/SKILL.md) with one location’s daily totals · available |

The [outbound catalog](CATALOG.md) describes 21 planned skills and the deliverable each one will produce. The two skills you can use today are **Period Report** and **Improve a Skill**.

## Agency reporting example

A client asks whether orders are down. It’s May 18. They have 180 orders against 300 for all of April. That looks like a 40% decline. Through April 18, they also had 180 orders. The line that belongs in the client report is **“Orders are flat through the 18th.”**

1. Copy the [reporting instructions](plugins/department-skills/skills/period-report/SKILL.md) into a fresh conversation in your LLM.
2. Attach the [sample daily orders](proof/a/daily.csv) and ask, **“How did orders change month over month through May 18, 2026?”**
3. Look for both date ranges, 180 orders in each period, and a change of 0%.

## Use a skill in your team or application

Each skill lives in a readable Markdown file. Give it to the model along with the input it calls for. To integrate the reporting skill into an application, run the [checker](proof/check.py) against the model’s actual output. Save the JSON object from the response as `actual-a.json` and run the following from a local copy of the repo.

```sh
python3 proof/check.py a actual-a.json
```

The checker reports which fields differ from the expected answer and exits with a nonzero status on failure. Use the [second export](proof/b/daily.csv) to test another case.

When the team finds a recurring mistake, use [Improve a Skill](plugins/department-skills/skills/improve-skill/SKILL.md) to turn the example into a proposed correction and a regression test. The [deployment guide](company/DEPLOY.md) shows how a company can own its private rules, approve a change, and distribute it to the next person doing the work.

For help implementing a workflow in your company, visit [AI Close](https://aiclosehq.com/).

## Contribute a case

A useful contribution can be as small as one example where the answer looked reasonable and would have led someone to the wrong decision.

- **Found a failure?** [Open an issue](https://github.com/gpm227/ai-close-skills/issues/new) with a shareable input, the output you got, the result you expected, and why the difference matters.
- **Have a skill your team uses?** Open a pull request with the instructions, an example someone else can run, and a way to tell whether it worked. Use synthetic or cleared examples so others can reproduce the work.
- **See a gap in the catalog?** Tell us what someone is trying to get done, what they start with, and what they need in hand when they finish.

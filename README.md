# AI Close Skills

Reusable Claude skills for departmental work. Each skill describes a job, the evidence it needs, and how to judge its output.

## Available skills

| Skill | What it produces |
| --- | --- |
| [Period report](plugins/department-skills/skills/period-report/SKILL.md) | A month-to-date comparison with explicit dates, totals, and percentage change. |
| [Improve a skill](plugins/department-skills/skills/improve-skill/SKILL.md) | A proposed correction with evidence, regression checks, and a review request for the department lead. |

## Outbound skills catalog

The [numbered catalog](CATALOG.md) describes 21 planned skills across customer and offer definition, brand and design, copywriting and content, and outbound operations. It includes ICP definition, brand voice, outbound email writing, one-sheet creation, and campaign analysis.

## Try the reporting skill

1. Open a fresh Claude conversation with the [period report instructions](plugins/department-skills/skills/period-report/SKILL.md) and [sample daily orders](proof/a/daily.csv).
2. Ask “How did orders change month over month through May 18, 2026?” Save the JSON object in the answer as `actual-a.json`.
3. From the root of a local copy, run `python3 proof/check.py a actual-a.json`. The checker verifies the two date windows, both totals, and the percentage. A successful check exits with status zero.
4. Use the [second sample](proof/b/daily.csv) in a fresh session to test another run. Keep the expected answers out of the conversation.

## Use in a company workspace

The [deployment walkthrough](company/DEPLOY.md) covers a company-owned private copy, the plugin configuration, automatic checks, optional employee feedback, and reviewed releases. Use the [run record](company/run-record.json) to link the prompt and output to observed cost and business outcome. The supplied evaluator runs locally on reporting artifacts. Capturing work automatically inside an employee workspace requires a separate integration.

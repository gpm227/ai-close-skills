---
name: period-report
description: "Compare month-to-date orders, revenue or other additive daily totals to the same elapsed dates in the previous calendar month. Use for an in-progress monthly report or month-over-month trend through a cutoff."
---

# Compare this month with last month

Get the daily export, named metric, local reporting cutoff and unit. Confirm that both extracts use the same timezone, entity scope and business definition. A cumulative month-to-date field, a daily average, distinct users across days and an additive daily total answer different questions. If the input is cumulative, ask for daily totals or reconcile resets before converting it. Never sum already-cumulative values.

1. Include the first day of the current month through the cutoff. Use the first day through the same day number in the preceding calendar month, capped at its last day. Explain unequal calendar coverage explicitly. Use complete reporting days; identify a partially loaded cutoff day and offer the latest complete common cutoff.
2. Require one finite, same-unit daily total per covered day. Distinguish a recorded zero from a missing row. If the CSV contains stores, currencies or repeated events, aggregate verified compatible records by local date first and retain the source mapping. Hold the finding on missing or duplicate daily totals.
3. From the skill directory run `python3 scripts/compare.py daily.csv --metric orders --cutoff 2026-05-18` with the actual inputs. When a unit field applies, add `--unit-column currency` (or its actual header) to reject mixed or blank units. The script uses Python's standard library. If code execution is unavailable, build the dated ledger and perform the same checks; identify the method used. The caller should receive the result without having to run code.
4. Sum both windows. Percent change is 100 × (current − prior) ÷ prior, rounded only at the end to two decimal places. When prior is zero, return `null` and state the absolute change. If prior is negative, state both totals and the absolute difference so the sign of the formula cannot be mistaken for business direction.
5. Give one sentence naming the metric, unit, source, dates and result, followed by JSON containing exactly `current_start`, `current_end`, `prior_start`, `prior_end`, `current_total`, `prior_total`, `change_pct`. Use ISO dates and JSON numbers or null. Keep definitions, missing data or coverage qualifications in prose.

Check a second time that the prior total uses only covered days and that the sentence agrees with the JSON. A partial month versus the previous **whole** month is a separate comparison. For weekly, year-over-year or cohort comparisons, confirm the requested window before using these rules.

[Run two complete exports and a zero-base case](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

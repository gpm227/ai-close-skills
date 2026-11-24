---
name: period-report
description: "Compare month-to-date orders, revenue or other additive daily totals to the same elapsed dates in the previous calendar month. Use for an in-progress monthly report or month-over-month trend through a cutoff."
---

# Compare this month with last month

Get the daily export, named metric, local reporting cutoff and unit. Confirm that both extracts use the same timezone, entity scope and business definition. A cumulative month-to-date field, a daily average, distinct users across days and an additive daily total answer different questions. If the input is cumulative, ask for daily totals or reconcile resets before converting it. Never sum already-cumulative values.

1. Include the first day of the current month through the cutoff. Use the first day through the same day number in the preceding calendar month, capped at its last day. Explain unequal calendar coverage explicitly. Use complete reporting days; identify a partially loaded cutoff day and offer the latest complete common cutoff.
2. Require one finite, same-unit daily total per covered day. Distinguish a recorded zero from a missing row. Inspect what one source row represents. For an order-line export, count a distinct order ID once on its reporting date if the metric is orders. For revenue, check whether each amount is a line value or a repeated order total before summing. Keep the field mapping and reconcile the daily totals to the source population. Hold the finding on unexplained duplicates or missing dates.
3. From the skill directory run `python3 scripts/compare.py daily.csv --metric orders --cutoff 2026-05-18` with the actual headers and ISO cutoff. If the date header differs, pass `--date-column "Business Date"`. For slash-formatted dates, pass the source's confirmed `--date-format "%m/%d/%Y"` or `"%d/%m/%Y"`. Ask about ambiguous dates. Convert timestamps to reporting-local dates before aggregating. When a unit field applies, add `--unit-column currency` with its actual header to reject mixed or blank units. With no Python execution, build the same dated ledger and identify the method. Give the caller the finished result.
4. Sum both windows. Percent change is 100 × (current − prior) ÷ prior, rounded only at the end to two decimal places. When prior is zero, return `null` and state the absolute change. If prior is negative, state both totals and the absolute difference so the sign of the formula cannot be mistaken for business direction.
5. Give one sentence naming the metric, unit, source, dates and result, followed by JSON containing exactly `current_start`, `current_end`, `prior_start`, `prior_end`, `current_total`, `prior_total`, `change_pct`. Use ISO dates and JSON numbers or null. Keep definitions, missing data or coverage qualifications in prose.

Check a second time that the prior total uses only covered days and that the sentence agrees with the JSON. A partial month versus the previous **whole** month is a separate comparison. For weekly, year-over-year or cohort comparisons, confirm the requested window before using these rules.

[Run two complete exports and a zero-base case](examples/practice.md).

## Try it on your work

Daily totals with dates, the metric you care about and your cutoff date.

> Compare this month through my cutoff with the same elapsed dates last month. Show both totals, their change and any dates that could change the conclusion.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `period-report.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

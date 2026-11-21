---
name: period-report
description: Compare a partial month's performance with the same elapsed days of the prior month using daily source totals, and return an auditable report.
---

Obtain daily totals for the two months, the reporting cutoff, and the metric. Ask when the cutoff or metric is ambiguous. Treat dates as local reporting dates. Use day one through the cutoff inclusive in the current month and day one through the same day number in the previous month, capped at that month's end. Explain any difference in covered days. Do not silently compare a partial month with a full month.

Use one observed daily total for every covered day. Flag missing dates, duplicates, mixed units and incomplete coverage for clarification. An explicit zero is an observation. Sum each window, then calculate percentage change as 100 times the difference divided by the prior total. If the prior total is zero, report the percentage as undefined. Round the final percentage to two decimals at most.

Return a short finding followed by a JSON object with current_start, current_end, prior_start, prior_end (ISO dates), current_total, prior_total, and change_pct (number or null). Include the metric and source reference in the surrounding explanation. Report any unresolved missing evidence before offering a directional conclusion.

---
name: review-sales-pipeline
description: "Reconcile opening and closing open sales pipeline from CRM snapshots or deal history, identify stage movement and deal-level exceptions, and assign next actions. Use for pipeline reviews, forecast preparation, or investigating apparent growth."
---

# Review the sales pipeline

Start with a current CRM export or pasted opportunity table. Identify its as-of date, open stages, filters and currency. Map source headers to deal ID, stage, amount and any available owner, next step, due date and activity fields. One snapshot supports a meeting about the current backlog. For movement, also request a comparable opening snapshot or dated deal history.

Check what one row represents. If several contact rows repeat the same parent deal amount, count the deal and its amount once per snapshot. Sum product lines only when the amounts are distinct line items with stable IDs; a repeated contact join can duplicate them. Flag conflicting balances or unidentified deals and request an opportunity-level export if the grain is unresolved. A blank amount is unknown. Show known value, distinct deal count and how many lack amounts by currency. Keep a recorded zero in the known group.

1. Reconcile each deal **once** from its opening open contribution to its closing open contribution. A continuing open deal contributes closing minus opening. A deal entering the open population contributes its closing amount. Label it new or reopened only with creation/history evidence; otherwise label it newly observed. A confirmed won/lost deal leaves open pipeline at its opening amount in a two-snapshot bridge; show booking value separately if it changed before close. With full event history, an event-by-event bridge is also valid. Show the basis used.
2. A transfer between open stages changes stage subtotals, with zero net movement in total open value unless its amount changes. Report changes in both stage and value without attributing the total change to both. New and closed within the period can be invisible in paired open snapshots. Reopening, scope/filter changes, deleted records and unknown exits need separate lines when material. An opening deal absent at close remains an unexplained exit pending history.
3. Reconcile each currency separately unless a dated rate and conversion policy are supplied. Include count and value; distinguish gross from probability-weighted pipeline. Show opening + signed movements = closing and any residual. When an amount is missing from either side, identify affected deals and reconcile only the fully valued subset. With one snapshot, show current stage counts, known exposure and exceptions.
4. Flag dated or missing next steps, missing owners and genuinely stale deals. Use the team's age threshold and last meaningful activity/stage history. A last-modified timestamp is a proxy and may be an administrative edit. If the threshold is unknown, list ages for owner review. Reference specific deal IDs with an owner and a proposed next action.
5. Return the current stage table, deal-level exceptions and decisions for the pipeline meeting. Include a movement bridge when history supports it. State which movement can be explained and which evidence would resolve the rest. Keep recommendations separate from changes in the CRM.

For a forecast review with history, also check close dates pushed more than once, age in the current stage against comparable deals, and exposure with only one active buyer contact. Use sales-cycle or conversion baselines only when their cohort and sample are known. Show a blank or unavailable history as an evidence gap. Keep these risk signals separate from dollars in the movement bridge.

[Work a two-snapshot bridge and a missing-history case](examples/practice.md).

## Try it on your work

An open-deal export with deal IDs, stages and amounts. Add a prior snapshot or change history if available.

> Which deals need attention? If the history supports it, reconcile what opened, moved and closed. Flag any amount the export cannot support.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `review-sales-pipeline.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

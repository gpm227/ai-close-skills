---
name: review-sales-pipeline
description: "Reconcile opening and closing open sales pipeline from CRM snapshots or deal history, identify stage movement and deal-level exceptions, and assign next actions. Use for pipeline reviews, forecast preparation, or investigating apparent growth."
---

# Review the sales pipeline

Agree the as-of timestamps, snapshot filters, currency basis, stages counted as open, and local date for overdue actions. Use an immutable deal ID; a renamed account is still the same opportunity. Retain amount, currency, stage, owner, next step and date, last meaningful activity and source row or event ID. Flag inconsistent duplicates before aggregating.

1. Reconcile each deal **once** from its opening open contribution to its closing open contribution. A continuing open deal contributes closing minus opening. A deal entering the open population contributes its closing amount. Label it new or reopened only with creation/history evidence; otherwise label it newly observed. A confirmed won/lost deal leaves open pipeline at its opening amount in a two-snapshot bridge; show booking value separately if it changed before close. With full event history, an event-by-event bridge is also valid. Show the basis used.
2. A transfer between open stages changes stage subtotals, with zero net movement in total open value unless its amount changes. Report changes in both stage and value without attributing the total change to both. New and closed within the period can be invisible in paired open snapshots. Reopening, scope/filter changes, deleted records and unknown exits need separate lines when material. A missing ID is an unexplained change, pending history.
3. Reconcile each currency separately unless a dated rate and conversion policy are supplied. Include count and value; distinguish gross from probability-weighted pipeline. Show opening + signed movements = closing and any residual. With one snapshot, return exposure, stage concentration, exceptions and a request for comparable history; never infer movements.
4. Flag dated or missing next steps, missing owners and genuinely stale deals. Use the team's age threshold and last meaningful activity/stage history. A last-modified timestamp is a proxy and may be an administrative edit. If the threshold is unknown, list ages for owner review. Reference specific deal IDs with an owner and a proposed next action.
5. Return the bridge, the closing stage table, deal-level exceptions and decisions for the pipeline meeting. State which movement can be explained and which evidence would resolve the rest. Keep recommendations separate from changes in the CRM.

For a forecast review with history, also check close dates pushed more than once, age in the current stage against comparable deals, and exposure with only one active buyer contact. Use sales-cycle or conversion baselines only when their cohort and sample are known. Show a blank or unavailable history as an evidence gap. Keep these risk signals separate from dollars in the movement bridge.

[Work a two-snapshot bridge and a missing-history case](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

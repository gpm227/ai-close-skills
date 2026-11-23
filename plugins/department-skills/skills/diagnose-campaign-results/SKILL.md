---
name: diagnose-campaign-results
description: "Diagnose outbound campaign performance from send, delivery, reply and meeting records; reconcile recipients, compare equally mature cohorts and propose one measurable test. Use when interpreting reply rates or finding where booked meetings drop."
---

# Diagnose campaign results

Ask for the export, the reporting cutoff/timezone, response horizon, channel, assignment unit and meeting definition. An email attempt measures deliverability. A person measures response. A meeting ID measures meetings. If only dashboard totals exist, reproduce what those totals support and name which recipient-level conclusions remain unknown.

1. Freeze the population and the cutoff. Register each input with its coverage period and fields. Join sends and events by stable recipient and campaign/variant ID, retaining event IDs. Separate retries, repeat touches, bounces, automated replies, human replies, positive replies, booked and held meetings. Deduplicate repeated event IDs. Preserve distinct genuine touches. Flag events that cannot be joined or whose clocks disagree.
2. Choose a horizon such as seven complete days after the first delivered touch per recipient. When using such an anchor, identify undelivered and unobserved recipients separately. Compare cohorts assigned under the same conditions and with the same follow-up opportunity. Report younger cohorts separately as immature. Stop if mixed unit, overlapping assignments or unknown tagging could change the decision.
3. Show counts and denominators explicitly. Deliverability can be delivered people / attempted people or delivered messages / sent messages; label the unit. Human reply is distinct responding recipients / distinct delivered recipients; count substantive responses once, after excluding automated messages and bounces. Separate positive replies from other human replies. Count booked and held under the stated attribution rule. A direct booking need not have a reply. If claiming a sequential stage conversion, count only records linked to both stages.
4. Report at most three observations with their exact count, denominator, window and evidence. Show a zero denominator as undefined. Explain when a sparse cohort, missing reply classification or unlinked calendar makes a rate provisional. Treat a cause as a hypothesis unless the assignment and evidence support it.
5. Deliver a funnel table, data exceptions, and one test that changes one variable. Specify assignment unit, baseline/control, primary count and denominator, guardrail, decision date and the team's pre-agreed result needed to act. If volume/threshold is unknown, request it or call the result exploratory. Release no sends from an analysis request.

[Practice with duplicate replies, an immature cohort and a direct booking](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

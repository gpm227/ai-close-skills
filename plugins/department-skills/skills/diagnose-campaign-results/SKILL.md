---
name: diagnose-campaign-results
description: "Diagnoses why an outbound or email campaign performed the way it did, with every rate shown as numerator over denominator, and proposes one next test. Use for campaign analysis, \"why aren't people replying,\" low reply rates, or email results."
---

# Diagnose campaign results

Plain AI reads the dashboard and says "reply rate is low, try better subject lines." It counts auto-replies as replies, compares a two-week-old campaign with a two-month-old one, and divides by the wrong number.

## You'll need

- **The campaign export.** One row per send or per person.
- **What counts.** Is a meeting a calendar booking or a reply saying yes?
- **Dates.** When each batch went out.

## Steps

1. Remove duplicate people. Decide whether you're counting people or emails, and stick to it.
2. Separate the funnel: sent, delivered, human replies, positive replies, meetings.
3. Make sure each stage is less than or equal to the stage before it. If not, find out why before going further.
4. Only compare batches that had the same time to respond.
5. Find the biggest drop you can actually do something about.
6. Propose one test that changes one thing, with the number you'll judge it by.

## What you get back

A funnel table with every rate shown as count over count, three or fewer findings, and one test with its success measure and end date.

## The trap

The tool reports a 9% reply rate: 45 replies on 500 sends. 40 of those 45 are out-of-office and bounce notices. Human replies are 5 of 500, or 1%. The problem isn't subject lines. It's who's on the list or what the email asks.

## Check it

- Every rate shows its numerator and denominator.
- Auto-replies are excluded from human replies.
- The proposed test changes exactly one thing.

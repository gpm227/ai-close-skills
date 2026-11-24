---
name: plan-outbound-test
description: "Plans an outbound campaign as a test: who it targets, why they'd act, the sequence, what you'll measure and when you'll stop. Use for planning a cold outreach campaign, an outbound experiment, or \"we want to start prospecting into X.\""
---

# Plan an outbound experiment

Use this when a team must decide which approach to repeat. A request for five email subject lines alone belongs with a copywriter. Use the supplied segment, reachable accounts, offer, proof, channels, suppression list and reply capacity. Missing suppression or ownership information can leave a plan useful for review but pending for launch.

## Set the decision before writing the sequence

1. Ask what decision comes after the test. If the team already has a specific comparison, keep it. If they need a hypothesis, compare the plausible reasons a buyer would act, tie each to an observation or buyer statement and label any untested assumption. Choose the reason with the strongest available evidence.
2. For an A/B comparison, write down the one difference you want to learn about. Define the assignment unit, mutually exclusive treatments, shared audience, sent-from identity, timing, maximum touches and offer. Assign all contacts at the same company together when they can influence the same decision. Reconcile the eligible count after exclusions and deduplication. Save assignment before the first touch.
3. Define the primary outcome as an observable event. Write the numerator, denominator, counting unit, observation window and what happens to bounces, late replies, multiple replies and referrals. Keep message delivery, positive replies and held calls as distinct events. Choose the primary denominator before assignment. When email delivery can differ between arms, also show positive accounts / all assigned eligible accounts and positive accounts / accounts with at least one delivered email. Show the two counts for each arm. The first retains delivery effects; the second helps interpret what happened among reached accounts and may select a different population. If delivery is unknown, mark that measure unavailable.
4. Specify each trigger, channel, time, owner and exit. Cap daily entry against real reply-handling capacity. A human reply exits the automated sequence for classification. Apply recorded opt-outs and suppression across variants before further touches.
5. Record the cutoff for reading results and the decision rule in advance. If traffic cannot discriminate a difference the buyer considers meaningful, call the read exploratory. With no agreed threshold, propose one for sign-off or report the observed difference without a winner. Record any safety or capacity stops separately from a success decision. A stopped or contaminated test needs its own note.

## Handoff

For a first pilot with one available message, the decision may be “Can our rep handle replies from this audience?” Keep one cohort, record how many eligible accounts enter, how many are reached, how many reply and whether replies receive timely attention. Agree on what would warrant a second batch, a revision or a pause. A single cohort can answer the operational question but cannot tell the team whether different wording would perform better.

Return a one-page test brief with the selected question and its basis, a rep sequence with exits, the measurement definition and the decision at readout. Include the treatment differences for a comparison, or the cohort and operating limits for a pilot. Include a counts example if the team might disagree about attribution. Deliver the plan as a draft.

[Practice with two contacts per account and unequal deliveries](examples/practice.md).

## Try it on your work

The audience, offer, outreach capacity and result you want to measure.

> Plan a first outbound test we can read. Specify who enters, what counts as a result, when to stop and what this design can tell us.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `plan-outbound-test.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

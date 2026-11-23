---
name: plan-outbound-test
description: "Plans an outbound campaign as a test: who it targets, why they'd act, the sequence, what you'll measure and when you'll stop. Use for planning a cold outreach campaign, an outbound experiment, or \"we want to start prospecting into X.\""
---

# Plan an outbound experiment

Use this when a team must decide which approach to repeat. A request for five email subject lines alone belongs with a copywriter. Use the supplied segment, reachable accounts, offer, proof, channels, suppression list and reply capacity. Missing suppression or ownership information can leave a plan useful for review but pending for launch.

## Set the decision before writing the sequence

1. Name three plausible reasons the buyer would act. Tie each to a dated observation, a buyer statement or a stated hypothesis. Select the reason with the strongest available evidence. Record the runner-up.
2. Write the comparison as one sentence. Define the assignment unit, mutually exclusive A/B treatments, shared audience, sent-from identity, timing, maximum touches and offer. Assign all contacts at the same company together when they can influence the same decision. Reconcile the eligible count after exclusions and deduplication. Save assignment before the first touch.
3. Define the primary outcome as an observable event. Write the numerator, denominator, counting unit, observation window and what happens to bounces, late replies, multiple replies and referrals. Keep message delivery, positive replies and held calls as distinct events. Choose the primary denominator before assignment. When email delivery can differ between arms, also show positive accounts / all assigned eligible accounts and positive accounts / accounts with at least one delivered email. Show the two counts for each arm. The first retains delivery effects; the second helps interpret what happened among reached accounts and may select a different population. If delivery is unknown, mark that measure unavailable.
4. Specify each trigger, channel, time, owner and exit. Cap daily entry against real reply-handling capacity. A human reply exits the automated sequence for classification. Apply recorded opt-outs and suppression across variants before further touches.
5. Record the cutoff for reading results and the decision rule in advance. If traffic cannot discriminate a difference the buyer considers meaningful, call the read exploratory. With no agreed threshold, propose one for sign-off or report the observed difference without a winner. Record any safety or capacity stops separately from a success decision. A stopped or contaminated test needs its own note.

## Handoff

Return a one-page test brief with the evidence for the selected hypothesis, an A/B table that exposes every difference, a rep sequence with exits, the measurement definition and the decision at readout. Include a counts example if the team might disagree about attribution. Deliver the plan as a draft.

[Practice with two contacts per account and unequal deliveries](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

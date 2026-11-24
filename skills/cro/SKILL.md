---
name: cro
description: "When the user wants more conversions from a page or form, or asks why a page is not converting, what to change first, or whether a field or element should be added or removed: landing pages, pricing pages, lead forms, or a URL shared for feedback. For the signup flow itself, see signup. For activation after signup, see onboarding. For the test design, see ab-testing. For the words on the page, see copywriting."
metadata:
  version: 0.1.0
---

# Conversion rate

You find out why a page is not converting and what to change first. The output is a short ordered list with one thing to do this week, not a checklist of best practice.

## Bring

| What | Minimum to start | What makes the answer good |
| --- | --- | --- |
| The page | URL or the copy and layout | A screenshot at desktop and mobile width |
| The numbers | Current conversion rate and what counts as a conversion | The denominator: sessions, form starts, qualified leads |
| The traffic | Where visitors come from | Volume per source, so a change in mix can be ruled out |
| After the click | What happens next | Completion rate for the step that follows |

## What comes back

1. A diagnosis in order of likely impact, with the evidence for each item.
2. One change to make this week, and why that one first.
3. Two or three tests worth running, each with the metric and the guardrail.
4. What not to touch, because changing it would confound the measurement.

## The trap, and the check

**The trap.** Treating the click as the conversion. A page can double its form starts while the qualified-lead rate falls, because the new headline attracts the wrong buyer. The second version of the trap is a mix shift reported as a lift: paid traffic grew, which converts differently, and the blended rate "improved" without the page changing.

**Check.** Write the full path as a chain with a rate at each step: arrival → start → submit → accept → activate. Compare each step with its own baseline, using counts as well as rates. Split by source and device across both periods. Reweight the earlier rates by the current traffic mix to estimate the effect of mix alone. If the event definition or tracking changed, reconcile analytics with completed bookings or CRM records before recommending a page edit.

## Read the company context first

Read the context and applicable house rules from the user’s working project or attachments. If no context file is available, use the supplied material, flag unknowns and ask only for facts that change the result. Apply `custom/_house.md` across jobs, `custom/cro.md` for this job and `custom/tools.md` for available tools. Approved company context governs facts and permissions.

Read `.agents/close-context.md` or `.agents/product-marketing.md`. The qualification rule tells you which conversions are worth having, the proof register tells you what can be shown, and the house positions rule out claims you would otherwise be tempted to test.

## How to do the job

1. **Identify the page type and its one job.** Homepage, landing, pricing, feature, form. A page with two jobs converts on neither.
2. **Work in this order**, because it is the order in which problems actually cost money:
   - **Value proposition clarity.** Can a cold reader say what this is and who it is for after five seconds? Test by reading only the hero out loud.
   - **Headline and first screen.** Specific beats clever. The headline should be recognisable to the traffic source that sent them.
   - **Button and its destination.** The label must describe what happens next. Trace the actual path.
   - **Proof placement.** Evidence next to the claim it supports, not collected in a logo strip.
   - **Objections.** Price, fit, effort, risk. Answer the one the sales team hears most.
   - **Friction.** Fields, steps, load, mobile. Every field costs conversions; keep only the ones sales uses in the first call.
3. **Check the post-click step.** A perfect page feeding a broken form is a form problem.
4. **Choose one change.** State the mechanism: what belief or obstacle it changes, and which step it should move.
5. **Set the read.** Metric, guardrail, minimum sample, and what would make you revert.

## Output format

**Diagnosis:** the chain, with the weakest step named.

| Step | Current rate | Read |
| --- | --- | --- |
| arrival → start | | |
| start → submit | | |
| submit → accepted | | |

**Do this week** — one change, the mechanism, the expected effect on one named step.

**Worth testing**

| Test | What it changes | Metric | Guardrail |
| --- | --- | --- | --- |

**Do not touch** — the elements that would confound the read, and why.

**What I could not check** — the measurement gaps, stated plainly.

## Page notes

- **Homepage**: separate the ready buyer from the researcher, then give each one path. Most homepage "conversion" problems are routing problems.
- **Landing page**: message match with the ad or email that sent them, one action, no navigation.
- **Pricing**: help the buyer choose between plans before asking them to choose a plan. Name who each tier is not for.
- **Forms**: ask for what sales uses in the first call and nothing else. If a field is only for routing, consider enriching it instead of asking.
- **Feature pages**: the job, the removed work, the evidence. Not the architecture.

## Questions that change the answer

1. What counts as a conversion, and who decides whether it was a good one?
2. What share of traffic is paid, and did that share change in the period you are comparing?
3. What happens in the sixty seconds after the click?

## Company hooks

- House rules: `custom/cro.md`, applied after this file. Use it for banned patterns, required disclaimers, and any element that must never be tested.
- If your analytics definitions differ from the defaults here, record them in the context document and cite them instead of restating them.

## Related skills

- **copywriting**: the diagnosis is right and the page needs rewriting.
- **ab-testing** (planned): the change is worth testing rather than shipping.
- **signup** and **onboarding**: the leak is after the page, not on it.

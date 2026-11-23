---
name: compare-vendor-proposals
description: "Compare vendor quotes, bids and renewals on equivalent volume, service, term and currency; expose fees, binding commitments and missing must-haves. Use to choose or negotiate among documented proposals."
---

# Compare vendor proposals

Start with the quotes or pasted pricing clauses. Pull out the billing period, included units, minimum term and exclusions before asking the buyer for anything. Where usage or term is unknown, show the fixed commitment and the cost as a function of the missing quantity. For example, “$400/month including 100 orders, then $2 per extra order” becomes `400 + 2 × max(orders − 100, 0)` per month. Compare over any shared period the proposals support and ask for the usage, start date or requirement that would actually change the choice. With only one quote, give its exposure and the terms to request from the next bidder. Give proposals short identifiers and section or page locators. Separate vendor text, buyer assumptions and your calculations. If no priorities are supplied, avoid inventing preference weights.

1. Give each must-have a row with status *met*, *excluded* or *unconfirmed*, with the clause that supports it. A cheaper bid that has an unresolved mandatory feature stays conditional.
2. Normalize units, tier rules, billing cadence, service level, currency and taxes where the quotes allow it. Apply tiers to each relevant month when billed monthly; a yearly average can hide overages. Distinguish a marginal tier from an all-units repricing. When terms are ambiguous, calculate both readings or request clarification.
3. Show line-item formulas for committed minimums, included volume, true-ups, setup, mandatory add-ons, usage, credits and escalation where applicable. Show period cost, cash due during the period from the billing schedule, and the full non-cancellable commitment as different figures. If payment timing is unspecified label cash timing unknown. Keep unknown fees visible; show known subtotal and conditions on ranking.
4. Compare at expected volume and at a decision-changing volume or boundary. Solve for a tie only within the pricing tiers and term where the formula is valid. Check at least one quantity on each side. Show currency conversion only with a supplied dated rate.
5. Return a comparison table, calculations keyed to clauses, one recommendation the evidence allows and the smallest set of vendor questions whose answers can change it. Include owners for unanswered questions. Honor explicit hard requirements before preferences.

[Compare an annual prepayment and a monthly overage quote](examples/practice.md).

## Try it on your work

One or more quotes. Include expected usage and must-haves if known.

> Compare total cost, cash timing and commitments on the same assumptions. Which vendor qualifies, and what unanswered question could change the choice?

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

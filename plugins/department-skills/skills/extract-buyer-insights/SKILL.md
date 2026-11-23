---
name: extract-buyer-insights
description: "Pulls what buyers actually said out of call transcripts or notes, separating their words from the seller's and from your interpretation. Use for call analysis, voice of customer, win/loss notes, or \"what are customers telling us.\""
---

# Extract buyer insights from calls

Analyze what buyers said about a specific job, decision or concern. Work from identifiable transcripts or notes and account mappings. Separate internal research from clearance to publish any quote.

## Code the evidence

1. Assign each call, account and utterance an ID, speaker and locator (timestamp, turn or note line). Preserve exact words for quotes. Label paraphrased meeting notes as notes. For unattributed text, keep speaker or account unknown.
2. Classify evidence as **buyer-originated**, **seller suggestion with buyer response**, or **analyst inference**. Record disagreement, prompts and tentative assent. Silence is missing evidence. Do not elevate a seller-led “sure” into a confirmed buyer priority.
3. Group equivalent buyer meanings into named themes. State the eligible account denominator and count distinct supporting account IDs once. Show contradictory accounts and evidence of a different workflow separately. An unmapped call can illustrate a remark but cannot establish another distinct account.
4. Distinguish a question about a feature from evidence of a missing capability, budget or purchase intent. Flag possible expansion only when a buyer identifies new need, scope or decision-maker. Attach the quote and the shortest question that would confirm ownership or impact.
5. When sources disagree, preserve the difference by entity, role or moment. Small samples support observations about the supplied accounts. Do not convert counts into a market forecast.

## Deliver

Lead with a short brief in the buyer's language. Include a theme table with support count/denominator, distinct account IDs, verbatim or paraphrased evidence and counterexamples. Add explicitly labeled inferences, expansion questions and a small ledger of ambiguous or excluded quotes with reasons. Recompute counts from unique IDs and spot-check every quotation against its origin before delivery.

[Practice with repeat calls, seller-led assent and a possible regional expansion](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

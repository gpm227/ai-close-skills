# Practice a pipeline review

**Request.** “What changed in September? Show open pipeline only, as of Sep 30, 2026. Flag overdue/missing next steps. No exchange rate or stage-age threshold is supplied.”

Two snapshots from the same CRM filters, Aug 31 and Sep 30 (all monetary amounts in thousands):

| Deal | Currency | Opening stage / value | Closing stage / value | Owner / next step at Sep 30 |
| --- | --- | --- | --- | --- |
| D1 | USD | Discovery 40 | Proposal 55 | E / Oct 3 review |
| D2 | USD | Proposal 70 | Won 80 | F / signed Sep 18 |
| D3 | USD | absent | Discovery 30 | unassigned / blank |
| D4 | USD | Discovery 10 | absent | unknown |
| E1 | EUR | Proposal 20 | Proposal 20 | R / Sep 26 review |

Stage rules: Discovery and Proposal are open; Won is closed. D2's signed booking value is known. CRM creation record H3 dates D3’s creation to Sep 6. D4 has no history export.

## What changed in the pipeline

| USD open bridge | Signed change (thousands) | Evidence |
| --- | ---: | --- |
| Opening | 120 | D1 + D2 + D4 |
| New open | +30 | D3 |
| Continuing amount change | +15 | D1 |
| Won removal at opening exposure | −70 | D2; separately booked at 80 |
| Unexplained exit | −10 | D4; request CRM history |
| Closing | 85 | D1 55 + D3 30 |

No arithmetic residual: 120 + 30 + 15 − 70 − 10 = 85. D4's reason is unresolved despite the reconciled total. D1 advanced to Proposal; its stage move adds nothing else to total open value. EUR open stayed at 20.

| Closing stage | USD count / value | EUR count / value |
| --- | --- | --- |
| Discovery | 1 / 30 | 0 / 0 |
| Proposal | 1 / 55 | 1 / 20 |

**Decisions.** Sales lead assigns D3 and secures a dated next step. R confirms whether the Sep 26 E1 review happened and sets the next action. CRM owner provides D4 history before classifying its exit. No stage-age or forecast inference is warranted from these inputs.

## Different case

“Only the closing snapshot is available and the company wants weighted pipeline. No stage probabilities are supplied.” Return Sep 30 gross stage exposure by currency and the current exceptions. Explain which dates, historical snapshot and probability schedule would support movement and weighted estimates. A candidate result that adds USD and EUR, classifies D4 as lost, or claims a pipeline growth rate fails.

## Walk into a pipeline meeting with one CRM export

“Which open proposals need attention today?” This September 30 export joins contacts to opportunities. All amounts are the parent opportunity amount in USD.

| Opportunity ID | Contact | Stage | Amount | Owner | Next step |
| --- | --- | --- | ---: | --- | --- |
| O-7 | A | Proposal | 40,000 | Lee | Oct 3 review |
| O-7 | B | Proposal | 40,000 | Lee | Oct 3 review |
| O-8 | C | Proposal | | Jin | |
| O-9 | D | Proposal | 0 | Jo | Oct 2 scoping |

Proposal has three distinct open deals. Two have amounts on record, totaling USD 40,000. O-8's missing amount makes the full stage value unknown. O-7's two contact rows refer to one USD 40,000 opportunity. O-9 has a recorded zero. At today's meeting ask Jin to confirm O-8's value and identify a next action and date. This snapshot supports that decision without making a claim about pipeline growth.

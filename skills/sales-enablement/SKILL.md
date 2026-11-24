---
name: sales-enablement
description: "When the user wants reps to run a conversation without them: a call plan, objection responses, a leave-behind, a deck for a specific meeting, or an audit of assets nobody uses. Covers what each asset is for, which stage it belongs to, and what to stop sending. For the offer being sold, see offers. For the page the buyer saw first, see copywriting."
metadata:
  version: 0.1.0
---

# Sales enablement

You build the material that lets someone else have the conversation. The test is not whether the asset is good. It is whether a rep who has never met the account can run the next call from it.

## Bring

| What | Minimum to start | What makes the answer good |
| --- | --- | --- |
| The conversation | Call notes or a recording | Two or three calls across won, lost and stalled |
| The buyers | Who is in the room and what each decides | The financial and technical approver's actual objections |
| Current assets | What reps already send | Which ones get opened, and which get asked for |
| Stage definitions | What has to be true to advance | The evidence a rep must collect at each stage |

## What comes back

1. A call plan for the next conversation: what to open with, what to learn, what to agree, and how to end.
2. An objection table: the objection in the buyer's words, the response that works, and the evidence it needs.
3. One leave-behind, sized to what the buyer will read after the call.
4. A stop-sending list: the assets that answer questions nobody asked.

## The trap, and the check

**The trap.** Producing collateral instead of enabling a decision. The deck grows because every function adds a slide, and the rep presents a company tour while the buyer is trying to work out whether this will take three weeks or three months. The second version is the objection response that wins the argument and loses the deal: a clever rebuttal to a concern that was actually a request for evidence.

**Check.** Hand the asset to a rep who has not spoken to the account and ask them to run the next call. If they need you in the room, the asset is not finished. Then check every objection row: does the response end in evidence, a question, or a concession? A response that ends in a claim is not enablement.

## Read the company context first

Read the context and applicable house rules from the user’s working project or attachments. If no context file is available, use the supplied material, flag unknowns and ask only for facts that change the result. Apply `custom/_house.md` across jobs, `custom/sales-enablement.md` for this job and `custom/tools.md` for available tools. Approved company context governs facts and permissions.

Read `.agents/close-context.md` or `.agents/product-marketing.md`. The proof register governs what a rep may say, the qualification rule governs who should be in the room, and the offer's exclusions are often the fastest way to end a stalled deal honestly.

## How to do the job

1. **Map the decision, not the funnel.** Who signs, who blocks, who benefits, who has to change their week. Each of those needs different material.
2. **Write the call plan around one agreement.** The end of the call is a specific next commitment, not "send me some information".
3. **Harvest objections verbatim.** Ten calls will produce five repeating concerns. Write them in the buyer's words; the polished version loses the tell that lets a rep recognise it live.
4. **Answer with evidence, then a question.** "Here is the pilot result from a team your size. What would need to be true for this to be worth a trial?" A concession is a last resort, not a technique.
5. **Build one leave-behind.** The thing the buyer forwards to the person who was not on the call. One page: the problem, the mechanism, the proof, the price shape, the next step.
6. **Audit what exists.** Ask which assets were sent in the last twenty deals. Everything else goes on the stop-sending list.
7. **Give the rep the exit.** The strongest asset often tells the rep when to walk away.

## Output format

**The decision being made** — who decides, and what they need to believe.

**Call plan**

| Minute | What happens | What to learn |
| --- | --- | --- |

**Objections**

| Objection, in their words | What is really being asked | Response | Evidence needed |
| --- | --- | --- | --- |

**Leave-behind** — the one page, written out.

**Stop sending** — the assets to retire, and what replaces them.

## Questions that change the answer

1. Which objection, if you heard it first, would tell you to walk away?
2. Who forwards your material internally, and to whom?
3. What does a rep need to have collected before the deal can be forecast?

## Company hooks

- House rules: `custom/sales-enablement.md`, applied after this file. Put your stage definitions, CRM fields and approval language there.
- If your team uses a specific deck or one-pager template, attach it. It outranks the shapes suggested here.

## Related skills

- **offers**: the objection is really about what is being sold.
- **cold-email**: the conversation has not started yet.
- **customer-research** (planned): the objections are not yet understood well enough to answer.

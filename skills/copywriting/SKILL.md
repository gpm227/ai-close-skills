---
name: copywriting
description: "When the user wants to write or rewrite page copy (homepage, landing, pricing, feature, about), or asks which headline, promise or message to lead with, or hands over a draft that needs to land better. Diagnoses the starting point first and changes only what it calls for. Every claim must trace to a source. For line edits to finished copy, see copy-editing. For emails, see emails. For what is being sold, see offers."
metadata:
  version: 0.1.0
---

# Copywriting

You write page copy that a buyer can act on. The measure is not whether it sounds good in isolation. It is whether a stranger understands the offer, believes the proof, and knows the next step.

## Bring

| What | Minimum to start | What makes the answer good |
| --- | --- | --- |
| The page's job | The one action you want | What happens immediately after that action |
| The reader | Who arrives and what they already know | Where they came from: ad, search, email, sales call |
| The offer | What they get, what it costs, what is excluded | The alternative they are comparing you to |
| Proof | Any number, customer or demonstration you can publish | Source, date and permission for each |

If there is no proof, the copy gets smaller and more concrete. It does not get louder.

## What comes back

1. The copy in blocks, in the order it appears on the page.
2. An annotation beside each block: what it is doing and why that choice.
3. Two alternative headlines with the argument each one makes.
4. A claims ledger: every factual claim, its source, and any claim you declined and what would unlock it.

## The trap, and the check

**The trap.** The model replaces the marketer's judgement with its own taste. It improves the vocabulary, softens the specificity, adds a benefit nobody claimed, and returns something smoother and weaker. The second half of the trap is invented precision: "cut reporting time by 60%" when nobody measured it.

**Check.** Read the draft against the input and ask two questions. Which words did I change that were a choice rather than an error? Which sentence would the founder have to defend in a meeting and could not? Undo the first, delete the second.

## Read the company context first

Read the context and applicable house rules from the user’s working project or attachments. If no context file is available, use the supplied material, flag unknowns and ask only for facts that change the result. Apply `custom/_house.md` across jobs, `custom/copywriting.md` for this job and `custom/tools.md` for available tools. Approved company context governs facts and permissions.

Read `.agents/close-context.md` (or `.agents/product-marketing.md`, or the `.claude/` equivalents) before asking anything. Use the customer language, proof register and house positions from it. Check its Learnings before proposing an angle; do not re-propose what has already been tested and rejected.

## Diagnose the starting point

Decide which situation you are in before writing. Most bad AI copy comes from treating every request as a blank page.

| Situation | What you were given | What you may change |
| --- | --- | --- |
| **Blank** | A one-line ask, or company-speak with no point of view | Build the argument. Latitude on angle, none on facts |
| **Voice present** | A rough draft that already has an opinion and its own words | Keep the argument and the vocabulary. Fix the buried lead, the vague line, the structure |
| **Point edit** | "Fix this headline" | That headline, plus the minimum around it to make it fit. Return the rest untouched |

Say which one you are in, with the evidence, in one line. Then write.

When the voice is present, read taste out of the input: their vocabulary is a voice choice, where they spent words is a priority choice, what they left out is a scope choice. A writing sample beats the default voice when the two conflict.

## Drafting protocol

1. **Write the one sentence the page exists to say.** If you cannot, the page has no job yet. Everything else supports that sentence.
2. **Lead with the decision, not the context.** The reader is deciding whether to keep reading. Earn the second sentence in the first.
3. **Order by the buyer's questions, not the company's structure.** What is it, is it for me, what does it cost, what happens if it fails, what do I do now.
4. **Make one claim per section, and support it in the same section.** Proof in a separate logo bar is decoration.
5. **Match the button to its destination.** "Book a call" that opens a form is a broken promise. "See pricing" that scrolls to a contact form is worse.
6. **Cut the throat-clearing.** The first paragraph of most drafts is an introduction to the second paragraph.

## Claims discipline

Every factual sentence gets one of three treatments:

- **Keep**, with a source in the claims ledger.
- **Soften**, to what is defensible: "teams like yours" becomes "the four teams in our pilot".
- **Decline**, with the unlock: "I can say this once we have a measured median, and the number of accounts it was measured across."

A declined claim is a deliverable. Say it plainly instead of writing around it.

## No AI tells

Never write:

- "It's not X, it's Y." Once is a device. Twice is a tic.
- "No X. No Y. No Z." The three-beat negation.
- "In today's fast-moving landscape", "seamlessly", "empower", "unlock", "elevate", "game-changer".
- A tricolon in every paragraph.
- The em dash pileup that turns one idea into four clauses.
- Anaphora pretending to be insight: "Less guessing. More shipping."

Keep these rare: rhetorical questions, "imagine if", one-word sentences for rhythm.

Before delivering, read the copy and count the sentences that would survive being read aloud to a colleague without embarrassment. That ratio is the real quality score.

## Output format

**Starting point:** A / B / C, with the evidence.

**The page, in blocks**

> **Hero**
> Headline / subhead / button
> *Why: states the outcome and the mechanism; button matches the demo form.*

**Headline alternatives** — two more, each with the argument it makes and the risk it carries.

**Claims ledger**

| Claim | Source | Status |
| --- | --- | --- |
| | | kept / softened / declined |

**Left out on purpose** — anything you cut and why, so the user does not re-add it.

## Copy by page type

- **Homepage**: one sentence for a cold reader, a path for the buyer who is ready, and a path for the one who is not. Do not try to close.
- **Landing page**: complete argument on one screen set. No navigation if you can help it. One action.
- **Pricing**: answer "which plan is right for me" before "what does it cost". Name who each plan is not for.
- **Feature**: the job it does, the work it removes, the evidence it works. Not the architecture.
- **About**: why this team is the one to do it. Not a timeline.

## Questions that change the answer

1. What happens in the sixty seconds after someone clicks the primary button?
2. What do buyers say when they almost bought and did not?
3. Which claim would you be uncomfortable defending to a customer who complained?

## Company hooks

- House rules: `custom/copywriting.md`, applied after this file. Use it for banned phrases, required disclaimers, and the sign-off route.
- Approved proof lives in the context document's proof register. Do not cite anything that is not there.
- If your team writes in a house style guide, attach it. It outranks the style rules here.

## Related skills

- **copy-editing** (planned): the copy exists and needs tightening rather than rebuilding.
- **offers**: the copy is fine and the offer is the problem.
- **cro**: the page converts badly for a structural reason rather than a copy reason.

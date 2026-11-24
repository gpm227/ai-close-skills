---
name: product-marketing
description: "When the user wants to create or update the company context doc, or asks what belongs in it, or whether their positioning, ICP, offer or proof is clear enough to write from: first setup, a repositioning, a new segment, or a pile of customer calls nobody has distilled. Use before any other skill on a new account. For the offer itself, see offers. For buyer language from interviews, see customer-research."
metadata:
  version: 0.1.0
---

# Company context

You build and maintain the one document every other skill reads. Its job is to stop the user re-explaining their business in every chat, and to give every later answer something to be checked against.

Canonical path: `.agents/close-context.md`. Read `.agents/product-marketing.md` and the `.claude/` equivalents if they exist, because other skill libraries use those names, and offer to move the content to the canonical path rather than duplicating it.

If the user works in chat with no repository, the document is still the deliverable. They paste it at the start of a conversation or attach it as a file, and every other skill asks for it.

## Bring

| What | Minimum to start | What makes the answer good |
| --- | --- | --- |
| Public material | A site, a deck, a pricing page, or the last launch post | At least one page written for buyers rather than investors |
| Sales reality | Two or three closed-won and closed-lost reasons | Call notes or recordings, quoted verbatim |
| Delivery reality | What you actually do, in what time, with what team | Cost per delivery and current capacity |
| Money | List price or price range | Margin, discount floor, and what you refuse to discount |

Missing rows are the work. Ask for them one at a time, not as a form.

## What comes back

1. The context document, complete enough that another skill can draft without asking a question it should already know.
2. A version number and a changelog line, because a document every skill reads needs a paper trail.
3. A short list of what you could not establish, and the single source that would settle each item.

## The trap, and the check

**The trap.** A context doc written in adjectives. "We are the trusted partner for ambitious teams" feels true, changes no decision, and cannot be used to accept or reject a sentence. A language model will happily help write another 500 words like it. The second version of the trap is invented specificity: the model fills a missing proof point with a plausible number, and every later skill quotes it as fact.

**Check.** Read each line and ask: could a writer use this to reject a draft? If not, delete the line. Then mark every claim as one of three things: a fact with a source, a decision with an owner, or an open question. No line may be a claim with no source.

## Read the company context first

Read the context and applicable house rules from the user’s working project or attachments. If no context file is available, use the supplied material, flag unknowns and ask only for facts that change the result. Apply `custom/_house.md` across jobs, `custom/product-marketing.md` for this job and `custom/tools.md` for available tools. Approved company context governs facts and permissions.

In a chat without file access, return the approved Markdown as `close-context.md` for the user to save in their project.

This skill writes that context. If a document already exists, read it, summarise where it stands, and ask which sections to change. Do not regenerate the whole document to change one section.

## How to do the job

1. **Draft from artifacts before asking questions.** Read the site, the deck, the pricing page, the last three launches, and any call notes. Draft every section from what is already written down. Present it with the gaps marked, then ask: what is wrong, and what is missing?
2. **Collect language, not descriptions.** The most valuable content is the buyer's own words: how they describe the problem, what they call the alternative, what they say when they almost bought and did not. Pull quotes from calls and emails. A polished paraphrase is worth less than a clumsy quote.
3. **Write the qualification rule, not the ICP description.** "Mid-market B2B SaaS" is a category. A usable rule reads: in, if they run paid acquisition and have a marketing hire; out, if they are agency-led or under 20 seats; evidence, a live job posting or a public pricing page. Write it so someone can apply it to a list without you.
4. **Capture the offer as it is sold, not as it is described.** What the buyer gets, what is excluded, the term, the price, the risk reversal, and the next step. If sales says something different from the pricing page, record the gap. That gap is usually the most useful line in the document.
5. **Build the proof register.** Every number, logo and quote, with its source, its date, and whether you have permission to publish it. A proof point with unknown permission is not usable in public copy. Say so in the row rather than letting a later skill guess.
6. **Take voice from writing that performed.** Use copy that shipped and worked, plus the founder's own emails, rather than adjectives chosen in a meeting. Three to five attributes, each with a real line as the example.
7. **Set the house positions.** The rules that apply to every future draft: claims you will not make, words you never use, the price you will not quote below, the competitor you will not name. This section is where the company's judgement lives.
8. **Confirm, version, save.** Show the finished document, take corrections, then set the version and a changelog entry that names what changed and why.

## Output format

```markdown
# Company context

**Version:** v1
**Last updated:** YYYY-MM-DD
**Owner:** [who approves changes]

## What we sell
**One line:**
**The job it does:**
**Category:** (what shelf the buyer puts us on)
**Delivery model and price band:**

## Who buys
**Qualification rule**
- In:
- Out:
- Evidence required:
**Buying roles:**
| Role | What they decide | What they worry about |
| --- | --- | --- |

## The problem and the alternative
**Why the current approach fails:**
**What it costs them:**
**Switching forces:** push / pull / habit / anxiety

## Competitive position
| Alternative | What it is | Where it falls short |
| --- | --- | --- |

## Differentiation
**What we do that others do not:**
**Why that matters to the buyer:**
**Why customers say they chose us:** (verbatim)

## Offer as sold
| Element | What it says |
| --- | --- |
| Included | |
| Excluded | |
| Term | |
| Price | |
| Risk reversal | |
| Next step | |
**Gap between the page and the sales call:**

## Proof register
| Claim | Number or quote | Source | Date | Permission |
| --- | --- | --- | --- | --- |

## Customer language
**Problem, verbatim:**
**Us, verbatim:**
**Words to use:**
**Words to avoid:**

## Voice
| Attribute | Means | Does not mean | Example line |
| --- | --- | --- | --- |

## House positions
**Claims we will not make:**
**Never-say list, with the reason:**
**Price floor:**
**Competitors we do not name:**

## Goals
**Business goal:**
**Conversion action:**
**Current numbers:**

## Learnings
*What shipping taught us. Newest first, about 20 rows maximum.*
| Date | Learning | Evidence | Applies to | Status |
| --- | --- | --- | --- | --- |

## Changelog
- v1 (YYYY-MM-DD) — Initial context.
```

## Learnings

The changelog records how the document changed. Learnings record what the work taught you: which angle won, which offer fell flat, which correction the founder gave twice.

An entry earns a place when it would change a draft: "Price-anchored headlines beat outcome headlines on the pricing page, +18% trial starts, 2,400 visitors per arm." It does not earn a place when it is a single anecdote or a note to self.

Set a status of `active`, `watch` or `retired`. Retire rather than delete, so nobody re-tests a settled question. Any skill that finishes a test may propose a row; add it only when the user approves, with a version bump.

## Questions that change the answer

1. What did the last five buyers say they were using before you?
2. Which claim do you make in sales that you could not publish?
3. What is the delivery cost or time constraint that limits who you can take?
4. What would you refuse to do for money?

## Company hooks

- House rules: `custom/product-marketing.md`, applied after this file. Use it for fixed section names your team expects, and for the approval route on changes.
- If you maintain several products or regions, keep one context document per product and name them `close-context.<product>.md`. Say in each which one a skill should read.
- Put anything you would not publish in `custom/`, not in the context document, if the document is shared with contractors.

## Related skills

- **offers**: once the delivery reality and price band are known, build the offer itself.
- **customer-research** (planned): when the gap is buyer language rather than company facts.
- **competitors** (planned): when the gap is the competitive table.

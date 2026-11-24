---
name: cold-email
description: "When the user wants to write or fix cold outreach: a first email, a follow-up sequence, subject lines, or a sequence that is not getting replies. Covers one verifiable reason to write, one ask, stop conditions, and deliverability basics. For LinkedIn messages, see social. For qualifying the list first, see prospecting. For replies that arrive, see sales-enablement."
metadata:
  version: 0.1.0
---

# Cold email

You write outreach that a busy person can answer in one line. The measure is replies from the right people, not open rates.

## Bring

| What | Minimum to start | What makes the answer good |
| --- | --- | --- |
| The recipient | Role and company | One verifiable, recent reason to write to this person |
| The offer | What you want them to consider | What the first step costs them in time |
| Proof | One relevant result or customer | Same segment, same size, same problem |
| Sending setup | The domain and mailbox you send from | Whether the domain is warmed, and who else sends from it |

## What comes back

1. Three emails: the opener, one follow-up with a new angle, and one closing email that ends the sequence.
2. Two subject lines per email, both lowercase and short.
3. Stop conditions: who to remove, what reply ends the sequence, how long to wait.
4. A do-not-send list for this segment, because the best outreach is sometimes none.

## The trap, and the check

**The trap.** Personalisation theatre. Line one compliments the company's recent funding round, line two explains what you do, line three asks for thirty minutes. The recipient can tell that the first line was generated from a database column, and the ask has nothing to do with the trigger. The second version of the trap is a sequence that asks for a meeting three times in different words.

**Check.** Read the email aloud and ask: does line one prove I looked at something real, or does it prove I had their company name? Does the ask follow from the reason I gave? If the reason disappeared, would the email still make sense? If yes, the reason is decoration.

## Read the company context first

Read the context and applicable house rules from the user’s working project or attachments. If no context file is available, use the supplied material, flag unknowns and ask only for facts that change the result. Apply `custom/_house.md` across jobs, `custom/cold-email.md` for this job and `custom/tools.md` for available tools. Approved company context governs facts and permissions.

Read `.agents/close-context.md` or `.agents/product-marketing.md`. Use the qualification rule to decide who not to email, the customer language for the problem phrasing, and the house positions for claims you cannot make.

## How to do the job

1. **Find the reason before the words.** A trigger: a job posting that implies a project, a product change, a public commitment, a competitor's outage, a new market. If there is no trigger, the email is a newsletter.
2. **Write the first line about them, specifically.** One sentence, verifiable, no flattery. "You opened a Denver warehouse in March and are hiring two operations managers" beats "love what you're building".
3. **Connect to a problem in their words.** One sentence. Not your category, not your mechanism. The problem as their peer would describe it.
4. **One ask, sized to the relationship.** A question is cheaper than a meeting. "Is this on your list this quarter?" gets answers. "Do you have 30 minutes?" gets silence.
5. **Make the proof optional and specific.** One line, same segment. If you do not have it, leave it out rather than generalise.
6. **Short.** 60 to 90 words. No attachments, no images, one link at most, and none in the first email if you can avoid it.
7. **Plan the end.** Three emails maximum unless they reply. The third says you are closing the loop, and means it.

Return the sequence as a draft. Sending or scheduling requires the user’s explicit approval of the recipients and copy.

## Output format

**Why this person, now:** one line naming the trigger and its source.

**Email 1** — subject options, body, one ask.

**Email 2 (day 4)** — new angle, not a reminder. Reference the first email in one clause at most.

**Email 3 (day 11)** — close the loop. State that you will stop, and what would make you useful later.

**Stop conditions** — who to exclude, what counts as a no, when to stop.

**Do not send if** — the conditions under which this sequence should not go out at all.

## Deliverability, briefly

Plain text, no tracking pixels, one link maximum, a warmed domain, and a mailbox that a person actually reads. A reply asking "who is this" still costs you the domain's reputation. Volume without a trigger is how domains get burned.

## Questions that change the answer

1. What changed for this company in the last thirty days?
2. What is the smallest useful first step you could offer?
3. Who must never receive this, and why?

## Company hooks

- House rules: `custom/cold-email.md`, applied after this file. Put banned phrases, required opt-out wording, and any legal footer rules there.
- If your team tracks sequences by name, record the naming convention in the context document so variants stay attributable.

## Related skills

- **prospecting** (planned): the list is not yet qualified.
- **copy-editing** (planned): the draft exists and needs tightening.
- **sales-enablement**: a reply arrived and the next step is a conversation.

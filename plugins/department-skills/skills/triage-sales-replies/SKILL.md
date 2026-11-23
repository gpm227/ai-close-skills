---
name: triage-sales-replies
description: "Sorts replies to outbound emails (interested, not now, wrong person, unsubscribe, question) and drafts the right response. Use for triaging replies, sorting an inbox of prospect responses, or \"what do I do with these replies.\""
---

# Triage sales replies

Turn inbound replies into an accountable action queue. Read the latest authored message and its thread, identifying sender, recipients, dates, quoted history and automated text. Use the team's routing taxonomy, approved answers and suppression scope when supplied. Preserve original message IDs.

## Route each intent

1. Separate the newest speaker's words from quoted or forwarded text. Detect auto-replies and delivery failures before classifying human intent. An out-of-office contact for emergencies is not a sales referral. For a non-delivery notice, identify the failed address from the diagnostic. Assign a permanent unknown-mailbox failure to the delivery owner for address correction. For a temporary delivery delay, check the mail system's retry status before anyone resends. Hold an ambiguous notice for the delivery owner. Keep address failure distinct from a person or company opting out. If the same export contains a notice twice, reconcile using its message ID.
2. Record a primary category and all material secondary intents: removal, referral, timing, question, objection or interest. For a multi-person or company-wide removal, identify the target and stop the affected follow-up while the owner verifies scope. A quoted previous removal still belongs to the original requester.
3. Route removal to the designated owner **before** any sales action. Keep requested, queued and confirmed states distinct. Call suppression completed only when there is authorized system evidence. No draft goes to a person who requested removal. A referral does not supply permission, an endorsement, a verified role or contact information.
4. For a timing request record the stated date, window and timezone when available. Leave an ambiguous window in the buyer's words. For a question use approved facts or assign the precise question for verification. Do not manufacture an answer to keep a conversation moving.
5. Draft only when a response is warranted. Label each owner action proposed until a source shows it was submitted or completed. When a mail notice confirms its own automatic retry, attribute that state to the mail system. The handoff can assign address correction even when nobody has opened a correction ticket.

## Deliver the queue

For each message give the thread or reply ID, sender, precise intent, target person or account, owner, action, timing, disposition, supporting phrase and draft if appropriate. If a source is missing, flag the narrow verification needed. Verify one primary row per inbound ID and all additional actions for multi-intent replies. Return removal requests first so the operator can act before a sales follow-up.

[Practice with mixed intent, an absence message and an account-wide removal](examples/practice.md).

## Try it on your work

Reply messages with identifiers and the preceding outbound message when available.

> Give each reply a disposition and next action. Draft replies where appropriate and flag opt-outs, delivery notices and ambiguous cases.

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

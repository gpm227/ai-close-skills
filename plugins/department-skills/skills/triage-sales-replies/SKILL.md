---
name: triage-sales-replies
description: "Sorts replies to outbound emails (interested, not now, wrong person, unsubscribe, question) and drafts the right response. Use for triaging replies, sorting an inbox of prospect responses, or \"what do I do with these replies.\""
---

# Triage sales replies

Turn inbound replies into an accountable action queue. Read the latest authored message and its thread, identifying sender, recipients, dates, quoted history and automated text. Use the team's routing taxonomy, approved answers and suppression scope when supplied. Preserve original message IDs.

## Route each intent

1. Separate the newest speaker's words from quoted or forwarded text. Detect auto-replies and delivery failures before classifying human intent. An out-of-office contact for emergencies is not a sales referral.
2. Record a primary category and all material secondary intents: removal, referral, timing, question, objection or interest. For a multi-person or company-wide removal, identify the target and stop the affected follow-up while the owner verifies scope. A quoted previous removal still belongs to the original requester.
3. Route removal to the designated owner **before** any sales action. Keep requested, queued and confirmed states distinct. Call suppression completed only when there is authorized system evidence. No draft goes to a person who requested removal. A referral does not supply permission, an endorsement, a verified role or contact information.
4. For a timing request record the stated date, window and timezone when available. Leave an ambiguous window in the buyer's words. For a question use approved facts or assign the precise question for verification. Do not manufacture an answer to keep a conversation moving.
5. Draft only when a response is warranted. Separate draft from send. A triage request alone ends at the queue; the output must never imply that contact, scheduling or CRM action already occurred.

## Deliver the queue

For each message give the thread or reply ID, sender, precise intent, target person or account, owner, action, timing, disposition, supporting phrase and draft if appropriate. If a source is missing, flag the narrow verification needed. Verify one primary row per inbound ID and all additional actions for multi-intent replies. Return removal requests first so the operator can act before a sales follow-up.

[Practice with mixed intent, an absence message and an account-wide removal](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

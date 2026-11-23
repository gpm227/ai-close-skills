---
name: design-workflow-automation
description: "Design a sales or marketing automation with source-to-destination mapping, replay-safe writes, failure routes, tests and a cutover plan. Use for CRM syncs, lead routing, form handoffs, n8n, Zapier or Make."
---

# Design a GTM automation

Establish the triggering business event, intended outcome, system of record, ownership, volumes, latency and authorized destinations. Get representative redacted records, input schema and tool/node versions. Distinguish the authority to design or test a flow from approval to activate it. Credentials appear only as references to the platform's credential store.

1. Describe the event sequence and the exact success condition including which side effects belong to the job. Give each field its source, type, normalization, required/default behavior and destination. Record validation failures before destination writes. Route missing required identities, conflicting IDs and unsupported schema versions to review.
2. Separate identities. A stable source **event ID** follows the same event through retries. A stable **business object ID** locates the destination record. Each side effect has its own deduplication key (e.g. source event ID + effect name). A fresh attempt ID is for logs only. Prefer immutable provider IDs over mutable email addresses.
3. Specify the destination's unique constraint, atomic upsert or idempotency support and what happens when simultaneous workers see the same key. If multiple effects are required, record each completion durably. For a timeout after submission, check destination receipts or use its idempotency guarantee. When acceptance is unknown and duplicate effects would matter, hold for reconciliation. A boolean set before or after an external call alone cannot guarantee exactly-once delivery.
4. Distinguish transient throttling/timeouts (bounded backoff and retry), permanent invalid inputs (review), and authorization/configuration failures (pause and alert the owner). Record attempt ID, event ID, step, status and destination receipt, with appropriate data minimization. Specify replay boundary, failure queue, incident owner, and how to stop unattended writes.
5. Deliver node-by-node spec or importable workflow plus a field map and acceptance table. Produce importable JSON only for a known installed platform/version, verify import in an isolated environment if available and state whether tested. Cover duplicate/concurrent delivery, changed record, out-of-order update, malformed input and lost acknowledgment after a write. Model expected counts with fixture IDs. Live activation requires the system owner's decision and monitoring destination.

[Design and check a two-effect CRM handoff](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

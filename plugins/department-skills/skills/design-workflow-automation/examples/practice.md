# Design a form-to-CRM handoff

**Request.** “A submitted demo request should upsert its company contact and create exactly one follow-up task per submission. Do not send email. The form supplies source, event_id, contact_id, sequence and email. CRM supports unique external keys for contacts and tasks, atomic upserts, and retrieval by key. Another deployment owns the actual connections.”

**Inputs.** Event E1: source=form-A, contact_id=P7, sequence=10, email=lee@example.test. Event E2: same source/contact, sequence=11, email=lee.new@example.test. Source guarantees strictly increasing sequence per contact. Assume CRM supports conditional contact updates by stored sequence.

## Worked design

| Step | Mapping or operation | Expected evidence |
| --- | --- | --- |
| Validate | Require source + nonempty event/contact IDs, email and integer sequence; no fallback ID | Invalid record in review queue; zero CRM writes |
| Contact upsert | External key = form-A/P7; email = supplied email; write a newer sequence atomically, equal/older leaves contact unchanged | CRM contact ID and stored sequence |
| Task upsert | External key = form-A/E1/follow-up or form-A/E2/follow-up, keyed to the submission; link to retrieved contact | One task ID per submission |
| Finish | Mark each effect and final status against the source event; log attempt IDs separately | Event ID, task and contact receipts |

Owner: sales operations. Transient CRM failures: retry with bounded backoff, e.g. three attempts respecting service guidance; then alert owner and queue unresolved event. Capture the destination receipt before marking an effect complete. Reconcile missing acknowledgments by unique key. The owner can pause intake and keep unprocessed submissions queued. Credentials come from the workflow platform. With no confirmed installed platform/version, deliver this mapping and a supported-node list to confirm; mark import and live run untested.

| Test input | Required outcome |
| --- | --- |
| E1 delivered twice/concurrently | One contact, one task for E1 |
| E2 after E1 | Same contact, updated email/sequence 11, a second task |
| Older E1 redelivered after E2 | Contact stays at sequence 11; still two tasks |
| CRM writes E2 task, response is lost | Lookup/upsert same task key; two tasks total |
| E3 omits contact_id | Record quarantined; no new CRM writes |

## Different case

“The CRM can only append tasks, cannot search them, and timed out after writing. May we replay?” Return the event's ambiguous status and stop the task replay. Ask the destination owner for a receipt or a safe idempotent interface. Retrying an unobservable non-idempotent effect can duplicate it. The spec may be delivered now; this effect remains blocked for automatic recovery.

# Diagnose a failed follow-up workflow

**Request.** “Our workflow v3 reported a 504 on create-task. E16, E17 and E18 retried; finance wants to know which are safe to replay.” Expected: upsert contact and create one CRM task per event with external key event ID + /task. CRM supports lookup and unique upsert by that key.

| Redacted source | Evidence |
| --- | --- |
| Good E15, steps 1–3 | Parse OK, contact C8 upsert 200, task E15/task returns T90 |
| E16, steps 1–3 | Parse OK, contact C8 upsert 200, task E16/task returned 504 |
| E17, steps 1–3 | Parse OK, contact C9 upsert 200, task E17/task returned 504 |
| E18, steps 1–3 | Parse OK, contact C10 upsert 200, task E18/task timed out |
| Destination receipt R16 | Exact E16/task exists as T91, linked to C8 |
| Destination receipt R17 | Authoritative complete lookup after the queue drained: E17/task absent |
| Destination receipt R18 | Lookup service unavailable; no destination evidence |

## Worked recovery ledger

| Event | Contact | Task | Disposition |
| --- | --- | --- | --- |
| E16 | C8 applied | T91 applied | Record T91 and finish; skip both writes |
| E17 | C9 applied | Confirmed absent | One canary upsert of E17/task linked to C9; verify one task |
| E18 | C10 applied | Unknown | Reconcile after lookup recovers; leave quarantined for now |

First recorded divergence is the task acknowledgment at step 3. Its upstream cause is unproved. An HTTP 504 can coexist with a destination write, as R16 shows. Proposed fix: persist the individual effect state and reconcile/upsert by stable key on ambiguous acknowledgments; retain original error and timestamps. This will prevent blind replay without pretending to fix the gateway.

CRM owner verifies E17 as the canary before any batch. Stop on missing or duplicate receipt, mismatched contact or a second timeout. After recovery there should be one expected task per E16/E17/E18 and no extra contacts; show actual counts and open cases. These are expected results, not a report that replay ran.

## Different case

“The destination is healthy; step 5 says ‘contact missing.’ Earlier trace P2 shows the new form sent `email_address`, while v3 maps only `Email` into an empty email. P3 consequently skipped contact creation.” Identify the first visible divergence at mapping P2. Correct/version the mapping; validate required input before new writes and test old and new payloads. Inventory any later effects before replay; do not resubmit an entire batch based on step 5's message.

---
name: diagnose-workflow-failure
description: "Finds why a sales or marketing automation failed, proposes the smallest fix, and plans a safe replay. Use when a Zapier, n8n, Make or CRM automation broke, skipped records, or did the wrong thing."
---

# Diagnose a failed GTM automation

Plain AI guesses at the cause and tells you to rerun it. The rerun sends the same email to 300 people a second time.

## You'll need

- **The run log or execution trace.**
- **What should have happened.**
- **A record that failed,** and one that worked if you have it.

## Steps

1. Find the first step where the output differs from what it should have been.
2. Compare that step's input and output to a run that worked.
3. Name the cause: bad data, wrong field mapping, expired login, or a temporary outage.
4. Propose the smallest fix.
5. Before any replay, list what already happened downstream (emails sent, records created) so the replay doesn't do it twice.

## What you get back

What failed and why, the fix, and a replay checklist: which records, in what order, and what to check before and after.

## The trap

Error at step 5: "Contact not found." The obvious fix is step 5. The real problem is step 2, which mapped `Email` to `email_address` after someone renamed the form field. Step 5 just inherited a blank.

## Check it

- The diagnosis names the first bad step, not the step that threw the error.
- The replay plan says which records already got emails or updates.
- The fix is tested on one record before the batch.

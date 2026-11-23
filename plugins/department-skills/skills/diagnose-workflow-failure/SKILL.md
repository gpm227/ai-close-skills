---
name: diagnose-workflow-failure
description: "Find the first evidenced divergence in a failed CRM or marketing automation and produce a bounded replay plan that preserves completed side effects. Use for missing records, wrong mappings, skipped tasks or ambiguous timeouts."
---

# Diagnose a failed GTM automation

When the report is just “the form was submitted and the lead never appeared,” start with one submission reference, its approximate time and time zone, and the place the lead was expected. Ask the source owner to locate that submission in history and the destination owner to check the record or receipt by the same stable reference. These two read-only observations establish which trace to request next. With logs available, obtain the expected step behavior, affected event IDs, deployed version and redacted traces for a failing and known-good case if possible. Preserve the original trace. If a flow continues to repeat incorrect writes, recommend pausing the affected route with its owner.

1. Trace one logical event across all attempts, using stable source, object and effect IDs. Compare each step's actual inputs and outputs with its expected output on that deployed version. The first *observed* divergence anchors the diagnosis. If an upstream trace is missing, state the causal uncertainty and identify what would distinguish hypotheses.
2. Build an effect ledger for every affected event: step, destination key, expected effect, observed receipt, status (confirmed applied / confirmed absent / unknown), action. A timeout, missing local log or HTTP error is insufficient proof a destination rejected a request. Reconcile downstream records under a stable key and check for duplicate or partial writes.
3. Propose the smallest correction with versioned evidence: mapping, input, credentials, dependency or timing. Separate recovery of the existing backlog from prevention for future inputs. Do not change the skill or system when the evidence shows the issue is a bad input or incomplete trace.
4. Design a replay at the earliest safe boundary for each event. Skip confirmed completed effects, retry confirmed missing effects with stable keys and quarantine ambiguous non-idempotent effects. Name the operator, scope, stop condition and expected counts. An approved operator should try one appropriate case first and verify the destination before expanding. A request for diagnosis yields a plan; record execution only when it actually occurs.
5. Deliver the causal timeline with trace references, effect ledger, candidate fix, replay sequence and a post-check that reconciles expected versus actual effects and detects duplicates. If cause is unknown, offer the smallest read-only observation that would settle it.

[Diagnose a timeout with three different recovery states](examples/practice.md).

## Try it on your work

The expected result and what you observed, plus any record IDs, event logs or source and destination snapshots.

> Find the earliest failure the evidence supports. Show what already succeeded, what is safe to retry and what we must verify first.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `diagnose-workflow-failure.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

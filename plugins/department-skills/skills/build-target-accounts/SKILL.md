---
name: build-target-accounts
description: Apply a supplied ICP and exclusion list to source records and produce an evidence-backed account list for outreach preparation.
---

Obtain the approved profile, account and location records, the exclusions, and their as-of dates. Preserve the owner's geographic and size definitions. Join on stable identifiers where possible. Flag ambiguous company matches. Count distinct eligible sites at the level named in the rule. Keep institution-wide counts distinct from counts within the service area.

Return one row per account with ID, name, eligible-site count when known, disposition, reason, evidence reference and any next research question. Use eligible, excluded or needs evidence. An established hard exclusion takes precedence over an unknown criterion. Missing evidence cannot justify eligibility. Mark estimates explicitly. Reconcile the input accounts against the three dispositions and surface duplicates and unmatched rows. Deliver the list for campaign preparation.

### Worked example

For a fictional provider the approved rule is 5–20 sites in State A, inclusive, with existing customers excluded. North has five documented A sites and confirmed noncustomer status. East has seven total and only three in A, with a complete location roster. West has seven total and a partial roster. South is a confirmed customer with an unknown site count. Expected dispositions: North eligible, East excluded, West needs evidence, South excluded. The counts reconcile to four accounts. A duplicate North site row must leave North's count at five.

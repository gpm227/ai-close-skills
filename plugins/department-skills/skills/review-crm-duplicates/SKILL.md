---
name: review-crm-duplicates
description: "Finds duplicate contacts or companies in a CRM export and proposes which record to keep, field by field. Use for dedupe, merge planning, CRM cleanup, or \"we have the same company in here three times.\""
---

# Review CRM duplicate candidates

Produce a proposed merge plan from a contact or company export. Preserve original identifiers and values. Ask for stable record IDs if absent. Obtain the entity grain, authoritative fields, survivor policy, protected records and relationship exports. If the CRM or evidence cannot support safe application, deliver a review queue.

## Resolve identity before choosing fields

1. Compare normalized copies of names, email, domains and phone numbers. Keep the raw values, record IDs and source references. Compare like entities: parent versus subsidiary, corporate versus branch and person versus shared mailbox are distinct identity questions.
2. Build the candidate set across available nonblank identifiers, such as upstream ID, normalized address or phone, or name plus employer. Inspect a pair once even when several match keys find it. Blank or placeholder values cannot link records. Preserve rows with no usable identifiers in a separate incomplete-data count. A verified unique upstream ID is strong evidence. A shared queue, switchboard, franchise domain or similar name supplies a clue only. State why records refer to the same person or entity, a distinct one, or an unresolved match.
3. Assign **merge proposal**, **review** or **keep apart**. Place conflicting identity evidence, protected records, consent flags, material field conflicts or competing open-deal ownership in review. Keep any suppression effective. Matching A/B and B/C does not establish a single A/B/C entity: verify agreement across every member before proposing a cluster.
4. For a merge proposal, select the survivor under the team's rule, otherwise prefer the most recently updated record when dates are comparable and identity is clear. Pick fields independently from entity identity. Use authoritative/recent nonempty data; distinguish a row's modification date from a field's verification date. Keep current nonempty values when the alternative is empty. Preserve original display values, activity links, deals and external IDs or flag any association that requires reconciliation.

## Deliver a reversible proposal

Give one row per candidate pair or validated cluster, candidate IDs, evidence, disposition, reason, survivor and proposed retired IDs. Provide a field map with previous value, proposed value, source and why for each changed field. List protected relationships and exact unresolved conflicts. Reconcile the input into unique records investigated, records with usable identifiers but no candidate match, and records with insufficient identity data. A record can appear in several pairs and still counts once. Report unique surviving/retiring IDs separately from candidate-pair counts. Each retired ID can appear in only one proposal.

Document the CRM's verified recovery method if known. Otherwise flag recovery as unknown and specify the raw records, relationship snapshots and field crosswalk to retain before any application. Record IDs alone cannot recreate lost history. List assessment never authorizes applying a merge.

[Practice a three-pair review with a shared mailbox and a suppression conflict](examples/practice.md).

## Try it on your work

A CRM export with record IDs and available identity fields, such as company, email or domain.

> Which records appear to be the same entity? Show the evidence, which fields to keep and which pairs need someone to check before merging.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `review-crm-duplicates.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

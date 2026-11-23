---
name: review-crm-duplicates
description: "Finds duplicate contacts or companies in a CRM export and proposes which record to keep, field by field. Use for dedupe, merge planning, CRM cleanup, or \"we have the same company in here three times.\""
---

# Review CRM duplicate candidates

Produce a proposed merge plan from a contact or company export. Preserve original identifiers and values. Ask for stable record IDs if absent. Obtain the entity grain, authoritative fields, survivor policy, protected records and relationship exports. If the CRM or evidence cannot support safe application, deliver a review queue.

## Resolve identity before choosing fields

1. Compare normalized copies of names, email, domains and phone numbers. Keep the raw values, record IDs and source references. Compare like entities: parent versus subsidiary, corporate versus branch and person versus shared mailbox are distinct identity questions.
2. Generate candidates from corroborating identifiers, then inspect each pair. A verified unique upstream ID is strong evidence. A shared queue, switchboard, franchise domain or similar name supplies a clue only. State why records refer to the same person or entity, a distinct one, or an unresolved match.
3. Assign **merge proposal**, **review** or **keep apart**. Place conflicting identity evidence, protected records, consent flags, material field conflicts or competing open-deal ownership in review. Keep any suppression effective. Matching A/B and B/C does not establish a single A/B/C entity: verify agreement across every member before proposing a cluster.
4. For a merge proposal, select the survivor under the team's rule, otherwise prefer the most recently updated record when dates are comparable and identity is clear. Pick fields independently from entity identity. Use authoritative/recent nonempty data; distinguish a row's modification date from a field's verification date. Keep current nonempty values when the alternative is empty. Preserve original display values, activity links, deals and external IDs or flag any association that requires reconciliation.

## Deliver a reversible proposal

Give one row per candidate pair or validated cluster, candidate IDs, evidence, disposition, reason, survivor and proposed retired IDs. Provide a field map with previous value, proposed value, source and why for each changed field. List protected relationships and exact unresolved conflicts. Report unique surviving/retiring IDs separately from candidate-pair counts. Each retired ID can appear in only one proposal.

Document the CRM's verified recovery method if known. Otherwise flag recovery as unknown and specify the raw records, relationship snapshots and field crosswalk to retain before any application. Record IDs alone cannot recreate lost history. List assessment never authorizes applying a merge.

[Practice a three-pair review with a shared mailbox and a suppression conflict](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

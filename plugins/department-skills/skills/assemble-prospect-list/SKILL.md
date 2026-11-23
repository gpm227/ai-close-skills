---
name: assemble-prospect-list
description: "Builds a list of companies and contacts that match your rules, with a source for every row. Use for prospect lists, lead lists, \"find me companies like X,\" or contacts to reach at target accounts."
---

# Build a prospect list

Create a dated company and contact list from approved sources and an existing buyer profile. Use the user's allowed data sources, target roles, serviceability rules, suppressions and as-of date. Never construct an address or imply that sourcing a record grants permission to contact it.

## Qualify accounts, then identify people

1. Translate the eligibility rules into reproducible source filters. Record export date, columns, join key and manual checks. Keep a stable account ID and resolve ambiguous shared domains, franchises or parent-company matches before accepting a record.
2. Screen all account exclusions, including current customers, open deals and any company-level suppressions. Separate confirmed exclusions from incomplete evidence. An unavailable exclusion source yields a research draft with the missing check identified.
3. For qualified accounts, match people by stable person ID or corroborated identity and employer. Check person-level suppressions and explicit departures before selecting any channel. Avoid attaching a namesake or a former employee to the company.
4. Record the source of each role and address, the actual evidence date and when it was checked. A research visit today does not refresh an old directory's underlying employment date. Mark unconfirmed roles older than 12 months as stale (or use the owner's stated freshness standard). Unknown dates or conflicting roles belong in the review queue. Do not assign an email to a different person, infer a deliverability status, or guess a naming pattern.
5. Keep an otherwise qualified company even if it has zero confirmed contacts. A confirmed contact may have a blank email. Distinguish a missing channel from a missing employment check.

## Deliver the two linked tables

Company columns: account ID, name, domain, hard-rule evidence, source locator, date checked, disposition. Contact columns: account ID, person ID if available, name, role, sourced address if available, role and address source/date, date checked and freshness. List exceptions separately with source IDs, reason and next verification. Report distinct companies, current contacts and held records separately; verify every contact joins to one eligible company and none matches a confirmed suppression. Keep filters and as-of date with the result so another rep can rebuild it.

[Practice with company and person suppressions, stale employment and an absent address](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

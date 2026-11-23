---
name: extract-site-data
description: "Extract a source-linked CSV from supplied public pages or snapshots and reconcile page coverage, duplicates and unknown values. Use for public directories, published prices, locations or listings."
---

# Extract a table from public pages

Confirm allowed domains/paths or supplied snapshots, the inclusion rule, fields, row identity and reporting date. If a page requires a login, record it as inaccessible and request an authorized export if it is needed. Do not infer a complete directory from the first visible page.

1. Inspect a representative page. Specify the row grain (e.g. one physical branch per location ID), field meanings and units, link/detail-page authority, and which attributes can legitimately be blank. Track discovered pages as pending, read, failed or excluded with a reason. Follow in-scope pagination until an endpoint, observed cycle or documented access limit. Record what fixes the scope; if discovery is partial, label coverage partial.
2. Extract each observation with its exact source URL and observation date, and retain a row locator such as a listing ID or heading. When processing supplied snapshots, identify the supplied file as evidence and distinguish its capture date from today's processing date. Keep conflicting observations linked to both sources. Prefer the agreed authoritative page, otherwise leave the disputed value blank and record the question.
3. Deduplicate by the agreed key across and within pages. An unavailable key or two similar names cannot justify merging. Keep an exception row or unresolved log. Count duplicate observations individually. Blank means “not published in the inspected sources”; record explicit zero, closure or “by appointment” as published.
4. Export UTF-8 CSV using a CSV writer with quoted text and escaped embedded quotes/newlines. For spreadsheet-safe text, detect a leading formula marker (`=`, `+`, `-`, `@`) after optional whitespace, or a leading tab/CR/LF, and prefix the original text with an apostrophe. Keep verified numeric fields typed, including genuine negatives. Record this export transformation when a literal value changes representation.
5. Deliver the CSV, a page-status log with failure reasons, a conflict/duplicate note and a short count reconciliation. Count **pages** and **records** independently: in-scope discovered pages = read + failed + pending; extracted observations = retained unique rows + repeated observations + unresolved/discarded observations. Give field-level missing counts. A readable page may contain zero, one or many records.

For a reproducible export, prepare the inspected observations using [the input example](examples/observations.json) and run `python3 scripts/export_rows.py observations.json NEW_DIRECTORY` from this skill directory. It writes `records.csv` and `coverage.json`. Supply observed values as strings or null and declare numeric columns explicitly. The helper uses the first occurrence for identical keys, blanks disputed values, records their source observations, and separates rows lacking identity. Resolve source priority before export only when the brief establishes it. It reads supplied observations locally. If the environment cannot run Python, apply the same reconciliation and deliver the CSV and log directly.

[Practice on supplied directory snapshots](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

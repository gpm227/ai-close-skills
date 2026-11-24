# Extract a directory with uneven coverage

**Request.** “Return one row per location ID from the three listed pages. Columns: ID, name, phone, source URL, observed date. Use the first occurrence for equivalent duplicates. The supplied page text was captured June 12, 2026.”

| Snapshot | URL | Visible text/status |
| --- | --- | --- |
| Page 1 | https://directory.example/p1 | B1, Oak Yard, 555-0101; B2, =North Annex, phone field empty |
| Page 2 | https://directory.example/p2 | B1, Oak Yard, 555-0101; B3, South Studio, 555-0103 |
| Page 3 | https://directory.example/p3 | Page unavailable; no records observed |

## Run the export

From the skill directory use `python3 scripts/export_rows.py examples/observations.json directory-output`. Compare `records.csv` with the output below, and verify the independent page and listing counts in `coverage.json`. Use a fresh destination on repeats.

## Worked CSV

```csv
"id","name","phone","source_url","observed_date"
"B1","Oak Yard","555-0101","https://directory.example/p1","2026-06-12"
"B2","'=North Annex","","https://directory.example/p1","2026-06-12"
"B3","South Studio","555-0103","https://directory.example/p2","2026-06-12"
```

For B2 the apostrophe is a spreadsheet safety transformation; the source name begins with an equals sign. Coverage log: p1 and p2 read, p3 failed (page unavailable), none pending. Three pages in scope. Four observed listings = three retained rows + one equivalent B1 duplicate on p2. One retained phone field is missing. Coverage is partial, including the count of all branches across the directory.

## Different case

“p3 now loads and lists B1 with a different phone, with no date or authority distinguishing the copies. The same page also lists ‘Oak Yard’ at a different address with no ID.” Keep one B1 row, record the two conflicting locations/cell values and leave phone unresolved unless a source priority is approved. Preserve the no-ID observation in the exceptions log; name similarity does not establish identity. A correct reconciliation accounts for it and the conflicting observation without silently manufacturing a fourth ID. If browsing is unavailable, the supplied snapshots suffice for this case.

---
name: extract-site-data
description: "Pulls a table of information from public web pages (locations, prices, staff, listings) into a CSV with the source on every row. Use for scraping, collecting data from websites, building a list from a directory, or \"pull all the locations from this site.\""
---

# Extract a table from public pages

Plain AI fills in blanks from memory, drops rows it couldn't load without saying so, and hands you a CSV that runs formulas when you open it.

## You'll need

- **The pages or site,** and which pages are in scope.
- **The columns you want,** and what each one means.
- **What makes a row unique** (address, URL, ID).

## Steps

1. Read one page first and confirm the fields mean what you think.
2. Pull every in-scope page you can reach. Record the URL and date on every row.
3. If a value isn't on the page, leave it blank. Never fill it in.
4. Remove duplicates using the unique key.
5. Keep a separate list of pages that failed to load.
6. Export CSV with text fields quoted. If a cell starts with =, +, - or @, prefix it with a single quote so spreadsheets don't run it.

## What you get back

The CSV and a short coverage note: pages found, pages read, pages failed, rows with missing fields.

## The trap

A location page has no phone number. The obvious move is to use the head office number from the contact page. Now 40 rows have the same number and look complete. Leave it blank.

## Check it

- Every row has a source URL and date.
- Row count plus failed pages equals pages in scope.
- No value appears that isn't on its source page.

# Practice with a partial month

**Request.** "How did orders change through May 18, 2026?" The CSVs contain complete local reporting days and one count of new orders per day. All records are synthetic.

## Run both completed examples

From the skill directory:

```sh
python3 scripts/compare.py examples/a/daily.csv --metric orders --cutoff 2026-05-18
python3 scripts/compare.py examples/b/daily.csv --metric orders --cutoff 2026-05-18
```

For A: “In examples/a/daily.csv, May 1–18 had 180 orders versus 180 on April 1–18, a 0% change.” All of April totals 300 and would produce a misleading 40% decline. For B: “In examples/b/daily.csv, May 1–18 had 144 orders versus 180 on April 1–18, down 36 orders (20%).”

| Case | Current start | Current end | Prior start | Prior end | Current | Prior | Change |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| A | 2026-05-01 | 2026-05-18 | 2026-04-01 | 2026-04-18 | 180 | 180 | 0 |
| B | 2026-05-01 | 2026-05-18 | 2026-04-01 | 2026-04-18 | 144 | 180 | -20 |

Compare the parsed JSON with [A's expected result](a/expected.json) or [B's expected result](b/expected.json). A missing row must produce a nonzero exit and no JSON. Removing a covered day must never convert a decline into an apparent improvement.

## Different case

“Report January 1 revenue. The complete daily export has December 1 at 0 USD and January 1 at 52.50 USD.”

```csv
date,revenue_usd
2025-12-01,0
2026-01-01,52.50
```

Use cutoff 2026-01-01 and metric revenue_usd. Return $52.50 versus $0, an absolute increase of $52.50, and `"change_pct": null`. If the December row disappears, withhold the comparison and identify December 1 as missing. For a March 31 cutoff in a leap year, end the prior window on February 29 and disclose 31 versus 29 days.

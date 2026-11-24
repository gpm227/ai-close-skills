# Qualify six accounts from a site roster

This is a fictional exercise with two CSV inputs. Give the skill [accounts.csv](accounts.csv) and [sites.csv](sites.csv) plus the request below. On a manual run, keep leading zeros in site IDs.

## Request

Use Colorado and Arizona as the service territory. Qualify companies with two to three distinct **territory** sites inclusive. Exclude suppressed accounts. I need a full decision ledger and a separate list that contains only eligible companies.

## Run

From the installed skill directory:

```sh
python3 scripts/qualify.py examples/accounts.csv examples/sites.csv --states CO,AZ --scope territory --minimum 2 --maximum 3 --decisions-file decisions.csv --eligible-file eligible.csv
```

Both output paths must be new. A run failure produces no usable decision ledger. Fix the input and use fresh output paths.

## Decision key

| ID | Decision | Why or next research question |
| --- | --- | --- |
| A | eligible | Two distinct territory sites. The repeated A/01 row counts once. |
| B | excluded | Two sites company-wide; one in territory. Verified complete. |
| C | needs evidence | Two sites qualify, but was suppression actually checked? |
| D | excluded | Confirmed suppression. No site totals are needed to decide. |
| E | needs evidence | Two observed in territory. Could omitted sites put the count above three? |
| F | needs evidence | One territory site; does the second site fall inside the territory? |

The decision ledger contains six IDs exactly once. Totals are 1 eligible, 2 excluded and 3 needing evidence. The eligible file contains only A. Verify the account IDs, source rows and observed counts. Download both files to check their contents.

## Edge prompt

Keep the same files and change the size rule to **all company sites**, with at least one verified site in CO or AZ. B and F now join A as eligible. F has two company sites regardless of the missing state, and its first site establishes territory presence. C and E still need evidence; D stays excluded. An unrecognized account ID on a site row must stop the run and identify the offending row.

## Published-count exercise

**Input.** Qualify operators with 2–3 active Colorado depots inclusive. The owner accepts an official operator directory's current count. The 8 May suppression export lists G and H as cleared. G's 5 May directory entry, D7 paragraph 2, says “We operate three active Colorado depots.” H's 6 May entry, D8 paragraph 1, says “Three depots nationwide. Our headquarters is in Denver.” Neither directory gives individual site records.

**Expected ledger.**

| Account | Published evidence | Coverage | Disposition |
| --- | --- | --- | --- |
| G | 3 active Colorado depots, D7 ¶2, 5 May | Full operator-reported Colorado count | Eligible. The published 3 meets the ceiling; suppression is cleared. |
| H | 3 nationwide, D8 ¶1, 6 May | National total; Colorado depot count unknown | Needs evidence. Ask how many active depots operate in Colorado. A headquarters may not be a depot. |

The eligible-only file has one ID, G. No site CSV is created. In both rows the distinct sites personally inspected, roster completeness and duplicate checks are unavailable. If G had said “including three Colorado depots” in a partial listing, treat three as a lower bound; a fourth would break the ceiling.

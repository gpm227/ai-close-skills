---
name: build-target-accounts
description: "Applies your ideal customer profile and exclusion list to a set of accounts and says which ones sales should pursue, with the reason and evidence for each. Use for target account lists, account qualification, or \"which of these should we go after.\""
---

# Build a target-account list

Produce a complete account decision ledger and a separate eligible-only file. Start from an approved profile, an account register, dated location evidence and all applicable suppression or exclusion sources. Keep source IDs as text.

## Apply the approved rule

1. Resolve whether the size band counts all company sites or only sites in the service territory. Confirm endpoints and how territory presence is established. Headquarters, contact location and number of local sites answer different questions. Show both interpretations and ask which applies if this changes an account decision.
2. Choose the calculation from the evidence actually provided.

   - **Published counts.** Use an account-level ledger. Capture the source's exact number or range, unit (stores, offices or other), count scope, geography, as-of date, coverage (all, selected, estimated or unknown) and locator. Qualify directly when the approved source explicitly establishes the applicable rule, including any separate territory-presence requirement. If a national total cannot settle a territory count, carry it as a national total and ask for the territory figure. Ranges and partial lists support only decisions true across the possible values; do not add overlapping counts.
   - **Site rows.** Use the runner below only for independently identified sites actually present in the source and a rule it can express. Never expand an aggregate into invented IDs, addresses, states or input rows. An exhaustive published total can establish the count without establishing that you have a complete site roster. For account-level evidence, set row-level fields and duplicate checks to “not available” or leave them blank; never report zero duplicates from uninspected rows.
   - **Mixed inputs.** Keep each account's evidence type. Process real site rows separately when useful, then reconcile account-level decisions with the published-count ledger. If two sources describe the same sites, compare scope and dates; do not sum them or silently give either priority.

   For genuine row input, preserve original filenames, stable IDs, dates and row locators in a crosswalk. The account columns are `account_id,name,excluded,roster_complete`. Set each flag to `yes`, `no` or `unknown`. Set `excluded=no` only after confirming every applicable hard gate and suppression check. An incomplete mandatory check stays `unknown`. Record each confirmed exclusion's original rule and source. Site columns are `account_id,site_id,state`. Normalize geography to consistent codes and leave absent state blank. Conflicting joins require source resolution.
3. For inclusive bands requiring at least one verified site in territory, run the bundled Python 3 script. Choose new output files. Replace the example flags with the actual rule.

   ```sh
   python3 scripts/qualify.py accounts.csv sites.csv --states CO,AZ --minimum 2 --maximum 3 --scope territory --decisions-file decisions.csv --eligible-file eligible.csv
   ```

   Use `--scope company` for a company-wide size band plus territory presence. For differently defined rules, including multiple counts or a headquarters test, apply those exact rules separately. If execution is unavailable, calculate manually and provide the same ledger and eligible-only CSV. Never claim the runner checked a condition it cannot express.
4. A confirmed exclusion or an already-exceeded maximum is decisive despite other gaps. A partial roster below the minimum cannot establish a failure. Missing geography can change either bound. If unresolved flags could affect eligibility, hold the account and give the precise missing evidence. Reject an orphan site ID or a repeated site ID with contradictory geography before delivering a prospecting file.

## Deliver and reconcile

Retain each account ID once with the actual evidence type, count and scope, evidence coverage, as-of date, one disposition, decisive rule, source locator and any research question. Keep published totals separate from individually observed site counts. Report decision totals for every account and duplicate counts only for the actual site rows examined. Confirm the eligible-only file contains exactly the eligible IDs and zero held or suppressed accounts. Treat normalized outputs as working files until the original source citations and additional rules are reconciled. On a failed run, return the specific blocking input row and repair needed. List delivery ends at these files.

[Try both site-roster and published-count examples](examples/practice.md).

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

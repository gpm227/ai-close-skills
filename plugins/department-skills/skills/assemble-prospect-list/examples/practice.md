# From a cleared account to a usable contact row

All rows are fictional. Use 15 May 2026 as the as-of date and treat the listed exports as the entire approved source set.

## Input

- Q1, account register from 12 May. A17 Basin Controls, basin.example, qualified and clear. B22 Wren Supply, wren.example, qualified but marked current customer. C13 Cove Service, cove.example, territory unverified.
- T1, team directory from 30 April 2026. A17’s director of operations is Lee Park. No email is displayed.
- T2, contact export last checked 5 January 2025. Rowan Oates, operations director at A17, rowan@basin.example.
- T3, account list from 7 May 2026. Jules Vale, buyer, B22. Jess Vale, buyer, C13.
- T4, person-level suppression export from 14 May 2026. Rowan Oates, A17, associated with the address in T2. These are the only supplied suppressions.
- Approved role is operations director. Build the two research tables for future manual review.

**Request.** Show the eligible companies and current contacts. Include every exception by source ID and explain how to reproduce the selection.

## Decision key

The company table has one row, A17 (Q1, 12 May). The contact table has one row, Lee Park (T1, 30 April), with an empty email, current as of 15 May. Record “no email supplied” in the research queue. Rowan is suppressed and excluded even if their address looks deliverable. B22 is excluded as a customer. C13 is held until territory is verified. Neither produces a contact row. Cite source and verification date separately for company and contact decisions.

The output must distinguish account-level and person-level checks. A confirmed role with a missing address does not authorize guessing one or sending a message.

## Edge prompt

Remove T4. Add a current directory explicitly stating Rowan has left Basin, while T2 still lists them there. Keep the conflicting employment evidence with both dates, exclude Rowan from current contacts, and do not transfer their former address to Lee. If the entire suppression source is unavailable, label the output a research draft pending suppression verification.

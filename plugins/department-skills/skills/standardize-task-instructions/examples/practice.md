# Build an SOP from an accepted report

**Source material.** Owner rule O1: “Weekly unit sales, one row per store in store-ID order. If more than one store is in scope, add All stores only if every required store submitted a count. Keep missing distinct from zero.” Owner rule O2: “Input is one weekly count per required store; duplicate submissions need validation.” Accepted output for W20 with required A and submitted A=4: table A, 4. The client used a blue heading; the owner has given no color requirement.

**Request.** “Write instructions our coordinators can run every Friday. Show how a new coordinator would call them.”

## Worked SOP

1. Obtain the week label, required store IDs and each submitted (week, store ID, unit count) record. Scope records to the requested week. Escalate duplicate in-scope store counts for reconciliation, and retain out-of-scope IDs in a note.
2. Return columns `store_id | units` in store-ID order. Empty submissions are listed as `missing`; a numeric zero is retained. For multiple required stores, append `All stores` only when each has one confirmed count. List the missing or disputed store ID and the required follow-up when a total is withheld. Do not infer a required heading color.
3. Check every required ID is represented once. When a total exists, recompute it from the visible rows.

**Invocation.** “Prepare W21 with required stores A, B and C. Received A=0, C=9; B has not submitted.”

**Expected artifact.**

| store_id | units |
| --- | ---: |
| A | 0 |
| B | missing |
| C | 9 |

Ask B's coordinator for its W21 count; withhold the combined total. Original A=4 case must still produce A=4 and no All stores. Keep O1 and O2 in the operating guide, distinct from the choice of header color.

## Different case

“Required B, A. Submission order B=7, A=2. A second file also shows A=3.” Candidate should surface both conflicting A values, preserve B=7 and withhold the total pending reconciliation. After an authorized correction to A=3, rerun: A=3, B=7, All stores=10. These are expected values. A real trial record must identify who ran it, instruction revision and actual output.

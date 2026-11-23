# Plan a contact merge without losing consent or relationships

All IDs describe fictional records. Use stable employee IDs as the strongest signal. The team keeps the record attached to the open deal. The CRM's merge reversibility is unknown.

## Input

| CRM ID | Employee ID | Contact | Address | Deal | Opt-out | Updated | Direct phone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 | Z9 | Noor Vale | noor@clay.example | O77 | No | May 1 | — |
| C2 | Z9 | Noor Vale | NOOR@clay.example | — | No | May 3 | 555-0101 |
| C3 | X2 | Paz Bell | ap@clay.example | — | No | May 1 | — |
| C4 | X3 | Gil Venn | ap@clay.example | — | No | May 1 | — |
| C5 | K1 | Ed Wynn | ed@kiln.example | — | Yes | May 1 | — |
| C6 | K1 | Ed Wynn | ED@kiln.example | — | No | May 2 | — |

**Request.** Return the merge plan with evidence, suggested survivor and field sources. Keep an audit record sufficient to check the proposed changes.

## Decision key

| Pair | Disposition | Decision |
| --- | --- | --- |
| C1/C2 | Merge proposal | C1 survives by the open-deal rule. Keep O77 and preserve activity links. Populate direct phone from C2. Use normalized email for comparison only. Record both original values. |
| C3/C4 | Keep apart | Two employee IDs and names share the accounts-payable address. |
| C5/C6 | Review | Same person evidence plus conflicting opt-out flags. Keep the suppression effective. No automatic survivor or loser. |

Three candidate pairs, one proposal. The losing record C2 is the only proposed retired ID. Specify original records, field/relationship snapshots and a recovery path verified for this CRM before actual application. IDs alone cannot restore lost activity or undo a merge. No records change during the review.

## Edge prompt

A third export links C2 to a similar name C7 at a different company using a recycled phone. Does the C1/C2 decision imply a three-record merge? Check every member and conflicting identifiers before making a cluster proposal. Distinguish a suspect candidate link from evidence of identity.

Add C8 and C9 with only their CRM IDs, and C10 with a unique upstream ID and direct email. The six original records still yield three pairs. C8 and C9 need identifying data. C10 has identifiers but no candidate match. Reconcile nine records as six reviewed, two incomplete and one unmatched.

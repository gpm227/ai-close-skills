# Triage a failing skill report

**Request.** “Run R41 was flagged wrong. Fix whatever produced the error.”

**Frozen standard C1** (team lead, REV3): Percent change is null when the previous window totals zero. **R41 receipt:** skill v1.4.2; inputs current 52, prior 0; original output `{"change_pct":null}`. **Evaluator Q7:** “fail: expected 0, saw null”. **Reproduction on v1.4.2:** same input, same output. All data is synthetic.

## Worked change request

| Question | Finding / disposition |
| --- | --- |
| Artifact versus C1 | Pass: R41 returned `null` when prior was zero |
| Checker versus C1 | Fail: Q7 expected numeric 0; correct the evaluator's zero-base expectation |
| Skill disposition | Keep v1.4.2 as is; no behavioral evidence supports changing it |
| Proposed evaluator regression | Prior 0 and current 52: null must pass; numeric 0 must fail |
| Preservation | Prior 20 and current 20: zero must pass; null must fail |
| Release owner | Reporting lead reviews exact checker diff and observed results before approving |

The supplied reproduction is observed evidence for the original skill. Candidate evaluator outputs, a post-release run, and business outcome are unknown until observed. A proposed test list alone cannot earn a passing candidate verdict.

## Different case

“C1 still applies. R42 is attributable to v1.4.2 but its preserved output is `{"change_pct":0}` for 52 versus 0. The checker correctly expected null. A fresh old-version run reproduced the mistake.” Investigate which instruction/runner produced zero. On confirming a skill gap, propose `If the prior total is zero, return null`, cover the failed 52/0 input, and reserve a different case (e.g. a different metric/month and zero comparison base) outside the editing session. Verify ordinary 20/20=0 still passes. Report separate actual old/candidate artifacts, checker judgment, owner release decision and served-version proof. If the exact output cannot be attributed, label it unknown and reproduce before editing.

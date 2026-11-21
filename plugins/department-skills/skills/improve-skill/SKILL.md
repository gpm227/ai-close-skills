---
name: improve-skill
description: Investigate an automatic check failure or employee-reported mistake and prepare a tested change for the department lead to review.
---

Start from a run ID, released skill version, actual output, and source evidence. Preserve the machine verdict and the employee's optional feedback independently. A missing vote carries no verdict. If the inputs are insufficient, ask the reporter for the smallest missing item.

Reproduce the behavior on the original release. Identify whether the input, standard, instructions, or evaluator caused the discrepancy. Ask the team lead to resolve ambiguous policy. Select the smallest general correction. Add a regression from the development case. Keep the second employee's test case out of the improvement session.

Draft a private change request with the old and new behavior, the exact rule changed, regression results, risks, and proposed version. The team lead decides whether to release. After approval and distribution, have a second employee try unseen input in a fresh session and record the version and actual result. General improvements may be proposed for the public library with new shareable examples.

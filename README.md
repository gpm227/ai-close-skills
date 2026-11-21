# AI Close Skills

Pick the job you need to do. Open the linked skill and give your AI workspace the instructions and the inputs it asks for.

- [Reporting](#reporting) — Find out whether orders rose or fell over comparable dates.
- [Outbound](#outbound) — Decide which accounts to pursue and write the page those buyers will see.

## Reporting

**Are orders down this month?** On May 18, the order count is 180. Comparing it with all 300 orders in April suggests a 40% drop. Compare April 1–18 with May 1–18 and both periods have 180 orders. The line to put in the report is **“Orders are flat through the 18th.”**

1. Open [Period Report](plugins/department-skills/skills/period-report/SKILL.md) and copy the instructions into a fresh conversation.
2. Attach the [daily orders](proof/a/daily.csv) and ask, “How did orders change month over month through May 18, 2026?”
3. Check the two date ranges, the order counts and the percentage change. The expected result is 180 orders in each period and a 0% change.

To verify the model’s output, save its JSON object as `actual-a.json` and run the [checker](proof/check.py) from a local copy of the repo.

```sh
python3 proof/check.py a actual-a.json
```

The checker identifies fields that differ from the expected answer and exits with a nonzero status on failure. Try the [second export](proof/b/daily.csv) to check another case.

## Outbound

| Job | Skill | What you get |
| --- | --- | --- |
| Decide what makes an account a fit. | [Define the ideal customer profile](plugins/department-skills/skills/define-icp/SKILL.md) | Eligibility rules, exclusions and the evidence needed to make a decision. |
| Decide which accounts sales should pursue. | [Build a target-account list](plugins/department-skills/skills/build-target-accounts/SKILL.md) | One row per account with a decision, the reason and the supporting record. |
| Write the landing page for an offer. | [Write conversion copy](plugins/department-skills/skills/write-conversion-copy/SKILL.md) | A headline, supporting copy and a call to action that matches what happens after the click. |

**Which accounts qualify?** Try the worked example in [Build a target-account list](plugins/department-skills/skills/build-target-accounts/SKILL.md). The offer covers companies with 5–20 sites in one state and excludes current customers. Give the model the four account records from the example and check its decisions.

| Account | Evidence | Expected decision |
| --- | --- | --- |
| North | Five verified sites in the state. Confirmed noncustomer. | Eligible. Five meets the lower limit. |
| East | Complete roster shows seven sites overall and three in the state. | Excluded. Only three sites count. |
| West | Seven sites overall. The location roster is incomplete. | Needs evidence. The eligible site count is unknown. |
| South | Confirmed current customer. Site count unknown. | Excluded. Customer status settles the decision. |

All four accounts should appear once. Give the model a duplicate site row for North and check that its count stays at five.

The [outbound catalog](CATALOG.md) lists 21 skills. The three linked above are available now. The other 18 are planned.

## Use a skill with your team

When the team finds a recurring mistake, use [Improve a Skill](plugins/department-skills/skills/improve-skill/SKILL.md) to turn the example into a proposed correction and a regression test. The [private deployment guide](company/DEPLOY.md) includes an installer, release verification, rollback instructions, and a local feedback recorder. Start there to put the skills under company ownership.

For help implementing a workflow in your company, visit [AI Close](https://aiclosehq.com/).

## Contribute a case

A useful contribution can be as small as one example where the answer looked reasonable and would have led someone to the wrong decision.

- **Found a failure?** [Open an issue](https://github.com/gpm227/ai-close-skills/issues/new) with a shareable input, the output you got, the result you expected, and why the difference matters.
- **Have a skill your team uses?** Open a pull request with the instructions, an example someone else can run, and a way to tell whether it worked. Use synthetic or cleared examples so others can reproduce the work.
- **See a gap in the catalog?** Tell us what someone is trying to get done, what they start with, and what they need in hand when they finish.

## Where this shows up

| Industry | Example |
| --- | --- |
| Marketing agencies | Before a client review, use [Reporting](#reporting) to check whether the order trend in the monthly update holds over matching dates. |
| Quick-service restaurants | Use [Reporting](#reporting) with one restaurant’s daily orders to see how that location is doing through the same day last month. |
| B2B service providers | Before assigning accounts to sales, use [Outbound](#outbound) to check which prospects have enough locations inside the territory the team serves. |

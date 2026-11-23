# AI Close skills

[All 37 Skills](CATALOG.md) · [Reporting](CATALOG.md#reporting) · [Sales](CATALOG.md#sales) · [Outbound](CATALOG.md#outbound) · [Marketing](CATALOG.md#marketing) · [Brand](CATALOG.md#brand) · [Operations](CATALOG.md#operations)

Pick a job and download its ZIP. In an eligible ChatGPT workspace, open **Plugins → Skills → Create → Upload from your computer** and select the ZIP. After installation, start a fresh chat with your material. The catalog shows what to bring and what you will get. The skill instructions and the bundled `SETUP.md` give you a request you can copy. [OpenAI’s installation and sharing instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

**Try it with two vendor quotes.** Attach the quotes and tell ChatGPT how much you expect to use each month and which requirements are mandatory. Ask, “Which quote should we take? Show the total for our expected use, when we pay, and the unanswered question that could change the choice.” If you have no quotes handy, the practice case includes both offers and a worked decision. [Download Compare vendor proposals](chatgpt/compare-vendor-proposals.zip?raw=true) · [Open the practice case](plugins/department-skills/skills/compare-vendor-proposals/examples/practice.md)

**Try it with a deck or website.** Attach your overview or supply the site and ask for an editable brand guide for a new writer or designer. The skill ties usable rules to your materials and lists the decisions the owner still needs to make. If you commission a design later, use those rules for the handoff. [Download Build a brand system](chatgpt/build-brand-system.zip?raw=true) · [Read the instructions](plugins/department-skills/skills/build-brand-system/SKILL.md)

[See an approved brand system applied to a service enquiry](examples/landing-page/build-reference.md).

For recurring team work, the [deployment guide](company/DEPLOY.md) covers ChatGPT for everyday jobs, Claude Design for commissioned brand and design work, and Claude Research for competitive analysis.

## See it work: reporting

The May 18 sample can produce a misleading 40% drop if an analyst compares a partial month with all of April.

That calculation compares 180 orders from May 1 to 18 with all 300 orders in April. Compare April 1 to 18 instead and both months have 180. **Orders are flat through the 18th.**

1. Install [Compare this month with last month](chatgpt/period-report.zip?raw=true) and open a fresh chat.
2. Attach the [daily orders](proof/a/daily.csv) and ask: "How did orders change month over month through May 18, 2026?"
3. You should get 180 orders in each period and a 0% change.

To check it automatically, save the JSON the model returns as `actual-a.json` and run:

```sh
python3 proof/check.py a actual-a.json
```

The checker lists any field that's wrong and exits nonzero on failure. Try the [second export](proof/b/daily.csv) for another case.

## See it work: sales

The rule: 5 to 20 sites in one state, current customers excluded. Give the model these four accounts with [Build a target-account list](plugins/department-skills/skills/build-target-accounts/SKILL.md).

| Account | What's known | Right answer |
| --- | --- | --- |
| North | Five verified sites in the state. Not a customer. | Eligible. Five meets the floor. |
| East | Seven sites total, three in the state. Complete list. | Excluded. Only three count. |
| West | Seven sites total. Location list incomplete. | Needs evidence. |
| South | Current customer. Site count unknown. | Excluded. Customer status decides it. |

Every account should appear once. Add a duplicate site row for North and its count should stay at five.

## Run it across a team

Start with one employee and a known result. When another employee needs to repeat the job, use the same version and check their result against the [skill acceptance standard](QUALITY.md).

- [Improve a skill](plugins/department-skills/skills/improve-skill/SKILL.md) turns one caught mistake into a tested fix.
- The [deployment guide](company/DEPLOY.md) puts the Skills in your company's own repository, with an installer, release checks, rollback and a feedback log.

## What has been tested

The [standalone review](proof/quality/standalone-review.md) records the inputs, output and first-use findings for each download. The [trial record](proof/quality/README.md) contains the actual outputs from 36 unseen catalog jobs and a separate brand-system test using a deck and a website capture. Two initial misses and their corrected runs are included. The [quality standard](QUALITY.md) explains how to score another case.

## Contribute

The most useful contribution is one example where the answer looked right and would have led someone to the wrong decision.

- **Found a mistake?** Open an issue in this repository with the input, what you got, what you expected, and why it matters.
- **Have a Skill your team uses?** Open a pull request with the instructions, an example someone else can run, and a way to tell if it worked. Use fake or cleared data.
- **Missing a job?** Tell us what someone is trying to get done, what they start with, and what they need at the end.

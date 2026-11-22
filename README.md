# AI Close Skills

Instructions that make ChatGPT and Claude do the job right, starting with the mistakes they make when you just ask.

Every Skill names one job, what to hand the AI, what comes back, the trap plain AI falls into, and how to check the result. Copy one into a chat and go.

**[All 36 Skills](CATALOG.md)** · [Reporting](CATALOG.md#reporting) · [Sales](CATALOG.md#sales) · [Outbound](CATALOG.md#outbound) · [Marketing](CATALOG.md#marketing) · [Brand](CATALOG.md#brand) · [Operations](CATALOG.md#operations)

## See it work: reporting

Ask ChatGPT how orders are doing on May 18 and it will tell you they fell 40%. They didn't.

It compared 180 orders from May 1 to 18 with all 300 orders in April. Compare April 1 to 18 instead and both months have 180. **Orders are flat through the 18th.**

1. Open [Compare this month with last month](plugins/department-skills/skills/period-report/SKILL.md) and paste it into a fresh chat.
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

A free Skill gets one person to a good answer. To get the whole team there:

- [Improve a skill](plugins/department-skills/skills/improve-skill/SKILL.md) turns one caught mistake into a tested fix.
- The [deployment guide](company/DEPLOY.md) puts the Skills in your company's own repository, with an installer, release checks, rollback and a feedback log.

Want it installed and maintained for you? [AI Close](https://aiclosehq.com/) does that.

## Contribute

The most useful contribution is one example where the answer looked right and would have led someone to the wrong decision.

- **Found a mistake?** [Open an issue](https://github.com/gpm227/ai-close-skills/issues/new) with the input, what you got, what you expected, and why it matters.
- **Have a Skill your team uses?** Open a pull request with the instructions, an example someone else can run, and a way to tell if it worked. Use fake or cleared data.
- **Missing a job?** Tell us what someone is trying to get done, what they start with, and what they need at the end.

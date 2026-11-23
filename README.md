# AI Close Skills

Bring an account list, a draft, an approval log or a daily export. Choose a job below and run it with your own rules in ChatGPT.

| Job | Download for ChatGPT | Try it with example inputs | What you get |
| --- | --- | --- | --- |
| Qualify target accounts | [Download skill](chatgpt/build-target-accounts.zip?raw=true) | [Two CSVs and the territory rule](examples/accounts/) | One decision per account and a separate eligible-only file |
| Review copy before it ships | [Download skill](chatgpt/review-brand-work.zip?raw=true) | [Draft, approved copy and substantiation](examples/brand/request.md) | Clean copy for the designer, changes tied to rules, and the release decision |
| Audit control evidence | [Download skill](chatgpt/audit-control-evidence.zip?raw=true) | [Policy and sampled payments](examples/audit/request.md) | A test for every sampled record, source references and an exception register |
| Compare month-to-date performance | [Download skill](chatgpt/period-report.zip?raw=true) | [Daily orders](proof/a/daily.csv) | Matched periods, both totals and the measured change |

### Use a skill in ChatGPT

1. Download one skill above. In ChatGPT, open **Plugins → Skills → Create → Upload from your computer** and select the downloaded skill. Complete the scan and install if prompted. Workspace access and upload permissions vary.
2. Open a new conversation, attach the inputs, and describe the job. For the reporting example, ask “Compare orders through May 18, 2026 with last month.” The supplied example returns 180 orders in each window and 0% change.
3. To use it with colleagues in the same workspace, open the skill's menu and choose **Share**. Partners in another eligible workspace can download their own copy. If Skills is unavailable, open the source from the catalog and attach the instructions and any scripts to a chat with file analysis; this is a manual run.

[OpenAI's ChatGPT installation and sharing guide](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) · [Browse all 37 jobs and downloads](CATALOG.md)

The four jobs above have example inputs and acceptance checks. The remaining 33 are packaged workflow instructions. Their partner outcomes still need testing.

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

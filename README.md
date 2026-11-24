# AI Close Skills

What are you working on? Pick a job, bring the files you have, and try it in ChatGPT or Claude.

[Sales](#sales) · [Marketing](#marketing) · [Operations](#operations) · [Reporting](#reporting) · [Analytics](#analytics)

[Browse all 43 skills](SKILLS.md) · [Install](#install) · [Set up your team](company/DEPLOY.md)

## Sales

> I have a call tomorrow. What do we know about this account, and what should I ask?

Bring the account notes and the last conversation. Get a call plan with questions, evidence to bring up and a next step for the buyer. If you’re still choosing whom to call, start with the customer profile.

[Prepare a sales call](plugins/department-skills/skills/prepare-sales-call/SKILL.md) · [Define your ideal customer](plugins/department-skills/skills/define-icp/SKILL.md) · [All sales skills](SKILLS.md#sales)

## Marketing

> Here’s our deck and website. What should the next designer keep consistent?

Turn the material you already have into a brand guide with rules for copy, type, color and imagery. If you’re working on a page instead, bring the draft and the claims you can back up.

[Build a brand guide](plugins/department-skills/skills/build-brand-system/SKILL.md) · [Rewrite a page](skills/copywriting/SKILL.md) · [All marketing skills](SKILLS.md#marketing)

## Operations

> One vendor bills monthly. The other wants a year up front. Which quote fits us?

Attach both quotes, expected usage and your must-haves. See the cost on the same terms, when the cash is due and what to ask before you sign. You can also turn a recurring task into instructions a colleague can follow.

[Compare vendor proposals](plugins/department-skills/skills/compare-vendor-proposals/SKILL.md) · [Document a recurring task](plugins/department-skills/skills/standardize-task-instructions/SKILL.md) · [All operations skills](SKILLS.md#operations)

## Reporting

> Are orders down this month, or are we comparing half a month with a full one?

Bring daily totals and the date you want to report through. Get comparable periods, the change and any missing dates. For a pipeline meeting, use two deal snapshots to show what opened, closed or moved.

[Compare monthly totals](plugins/department-skills/skills/period-report/SKILL.md) · [Report pipeline changes](plugins/department-skills/skills/review-sales-pipeline/SKILL.md) · [All reporting skills](SKILLS.md#reporting)

## Analytics

> Fewer people completed our form. Where did we start losing them?

Bring visits, form starts and submissions for each period, split by traffic source if you have it. See which step changed and what to check first. For interview data, trace a recurring theme back to the calls where it appeared.

[Find the drop-off](skills/cro/SKILL.md) · [Analyze customer interviews](plugins/department-skills/skills/extract-buyer-insights/SKILL.md) · [All analytics skills](SKILLS.md#analytics)

## Install

**ChatGPT.** Open the [skill directory](SKILLS.md) and choose a job. If it has a Markdown file, attach that file and your material in a fresh chat. If it has a ZIP, upload it through Skills in a supported workspace, or unzip it and attach the instructions and any supporting files the job needs. [ChatGPT setup](company/DEPLOY.md#run-one-job-in-chatgpt)

**Claude Code.** Add the marketplace once. The first plugin includes the 37 department skills. The second adds six skills for company briefs, offers, copy, outreach, sales calls and conversion analysis.

```text
/plugin marketplace add gpm227/ai-close-skills
/plugin install department-skills@department-workflows
/plugin install aiclose-skills@department-workflows
```

**Other agents.** Install one skill by name. This command gets the monthly reporting skill:

```sh
npx skills add gpm227/ai-close-skills --skill period-report
```

## For your team

[Add your house rules](CUSTOMISING.md) · [Deploy and update skills](company/DEPLOY.md) · [Suggest a change](CONTRIBUTING.md) · [Contact Greg](mailto:greg@aiclosehq.com)

[MIT license](LICENSE). The marketing collection adapts the taxonomy of [Corey Haines’ marketing skills](https://github.com/coreyhaines31/marketingskills).

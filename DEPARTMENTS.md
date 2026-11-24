# AI Close department skills

This guide covers the 37 skills available as individual ChatGPT downloads. You can also [browse the full library by job](SKILLS.md). Use them when you need to decide which vendor to hire, give a designer a brief, get a sales rep ready for a call, or figure out why a campaign went quiet. Each skill tells the assistant what to ask for, what to deliver, and how to check its work.

## Table of Contents

1. [How it works](#how-it-works)
2. [Commercial Services](#commercial-services)
3. [Getting started](#installation)
4. [Workflows](#workflows)
5. [Skills by area](#skills-by-area)
   - [Sales](CATALOG.md#sales)
   - [Marketing](CATALOG.md#marketing)
   - [Operations](CATALOG.md#operations)
   - [Reporting](CATALOG.md#reporting)
   - [Analytics](CATALOG.md#analytics)
6. [When a result misses the mark](#when-a-result-misses-the-mark)
7. [License](#license)

## How it works

Say you have two quotes for the software that runs your support desk. One vendor bills monthly. The other wants a year up front. You need to know which one to sign.

Give **Compare vendor proposals** the quotes, your expected monthly volume, and the features you need. At 500 cases a month, one vendor would charge $9,600 over the year. The other wants $8,400 up front. Your team requires single sign-on, and only the first vendor includes it in writing. Before taking the cheaper offer, ask the second vendor, “Is single sign-on included at this price for the full year?”

You can check the arithmetic and the missing term yourself. Then try the same skill on the two quotes sitting in your inbox. [Download the skill](chatgpt/compare-vendor-proposals.zip?raw=true) · [See both quotes and the cost breakdown](plugins/department-skills/skills/compare-vendor-proposals/examples/practice.md)

## Commercial Services

AI Close builds and installs custom skills for teams. If a recurring job depends on one person knowing how to do it, we can work with that person, test the skill on a real example, and help the rest of the team use it. Tell Greg what the job is and what a good result looks like. [greg@aiclosehq.com](mailto:greg@aiclosehq.com)

## Installation

### ChatGPT

Choose a job in the [catalog](CATALOG.md) and download its ZIP. In a workspace with Skills enabled, open **Plugins → Skills → Create → Upload from your computer** and select the ZIP. Start a fresh chat, name the skill, and attach your own material. Each download includes an example and a first request you can copy.

### Try a skill without installing it

Unzip the download, attach `SKILL.md` and your input to a chat, and include any example, reference, or script the job calls for. [First-run instructions](company/DEPLOY.md#run-one-job-in-chatgpt)

### Team setup for ChatGPT or Claude

Keep the skills and your company’s rules in a private repository. The guide walks the person setting it up through sharing a ChatGPT skill or connecting the repository to a Claude organization, then checking which version a coworker receives. [Company deployment guide](company/DEPLOY.md#share-a-company-release)

## Workflows

You can use any skill on its own. When a job spans several skills, carry the work you approved into the next step.

| What you need to get done | How the skills fit together |
| --- | --- |
| Reach the right customers | [Qualify your account list](plugins/department-skills/skills/build-target-accounts/SKILL.md). Pick an eligible prospect, [brief the rep](plugins/department-skills/skills/brief-an-account/SKILL.md), then [draft the first email and follow-ups](chatgpt/draft-outbound-email.zip?raw=true). |
| Launch a new service | Start with [what you can promise and prove](plugins/department-skills/skills/substantiate-offer/SKILL.md). Use the approved offer to [write the landing page](chatgpt/write-conversion-copy.zip?raw=true) and [give sales a one-sheet](plugins/department-skills/skills/build-marketing-one-sheet/SKILL.md). |
| Hand off the brand to a new writer | Turn your existing deck or website into [an editable brand guide](chatgpt/build-brand-system.zip?raw=true). Use it to [review the writer’s first draft](plugins/department-skills/skills/review-brand-work/SKILL.md) and point to the rule behind each edit. |
| Run the weekly sales meeting | [Review the open deals](chatgpt/review-sales-pipeline.zip?raw=true). Add last week’s export to see what moved. For a deal that needs a conversation, [prepare the next call](plugins/department-skills/skills/prepare-sales-call/SKILL.md) from the account notes. |

## Skills by area

Choose an area for the inputs, outputs and download links.

[Sales](CATALOG.md#sales) · [Marketing](CATALOG.md#marketing) · [Operations](CATALOG.md#operations) · [Reporting](CATALOG.md#reporting) · [Analytics](CATALOG.md#analytics)

## When a result misses the mark

Keep the input, the answer you got, and the answer you would have accepted. **Improve a skill** uses those three pieces and the original instructions to find what went wrong. If the instructions need changing, test the edit on the original case and on a case that already worked. The person who owns the job decides whether to share the revision.

[Improve a skill](plugins/department-skills/skills/improve-skill/SKILL.md) · [See the trial inputs, results, and corrections](proof/quality/README.md) · [Update or roll back a team release](company/DEPLOY.md#update-or-roll-back)

## License

[MIT License](LICENSE) · Copyright © 2026 AI Close contributors.

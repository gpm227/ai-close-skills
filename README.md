# AI Close skills

Marketing skills for people who have to sell something. Every skill ends in an artifact you can use: a page, an offer, a sequence, a call plan. None of them ends in a document about the work.

Built for revenue teams working with ChatGPT, Claude or a coding agent. One shared understanding of your business, then one instruction file per job.

## Contents

1. [Use a skill in ChatGPT or Claude](#install)
2. [What each marketing skill delivers](#what-you-get-every-time)
3. [Choose a job](#start-with-the-job-in-front-of-you)
4. [Set up your company context](#it-learns-your-business-once)
5. [Marketing skills by area and release status](#what-is-in-this-release)
6. [Department skills, downloads and team deployment](#works-alongside-the-department-library)

## Install

**ChatGPT.** Open a project. Attach the `SKILL.md` for the job and the material listed under **Bring**. Start with [company context](skills/product-marketing/SKILL.md) if you expect to run several jobs. Save the approved result as `close-context.md` and add it to your project files. For a single job, start directly with that skill. A first request for [copywriting](skills/copywriting/SKILL.md) is “Rewrite this page for a clinic manager. The action is to request a demo. Use only the attached proof and show me which claims you left out.”

**Claude Code.** Add the public marketplace once and install the marketing plugin. Run the commands inside Claude Code.

```text
/plugin marketplace add gpm227/ai-close-skills
/plugin install aiclose-skills@department-workflows
```

**Other agents with a skills folder.** Install a single marketing skill by name. For example:

```sh
npx skills add gpm227/ai-close-skills --skill copywriting
```

## What you get every time

| Part | What it does |
| --- | --- |
| **Bring** | The four or five inputs the job needs, and what separates a usable answer from a thin one |
| **What comes back** | The artifact, item by item, in the order you will use it |
| **The trap** | The specific wrong answer a plain request produces, with an example |
| **The check** | A test you can run on the answer in under a minute |
| **Company hooks** | Exactly where your own rules, prices and proof override the defaults |

The trap and the check are the point. An answer you cannot grade is an answer you cannot ship.

## Start with the job in front of you

**A page that is not converting.** Give `cro` the URL, the conversion rate and the traffic mix. It writes the path as a chain with a rate at each step, names the weakest one, and gives you a single change for this week plus the read that would tell you it worked.

**Copy that sounds like everyone else's.** Give `copywriting` the draft, the page's one job and the proof you can publish. It keeps your argument, fixes the buried lead, and returns a claims ledger listing what it declined to claim and what would unlock it.

**An offer nobody is buying.** Give `offers` the delivery reality, the buyer's alternative and your price floor. It returns the offer as a table, including the exclusions, plus the test of whether you could honour the guarantee ten times in a row.

[Browse the 53 marketing jobs and their release status](SKILLS.md).

## It learns your business once

Run `product-marketing` first. It reads your site, deck, pricing page and call notes, then writes `.agents/close-context.md`: what you sell, who qualifies, how you are different, what you charge, which proof you may publish and which claims you refuse to make.

The other marketing skills look for that file or an attached copy before asking for inputs. You stop re-explaining your business, and the answers start matching the business.

Then add your own rules in `custom/`. Banned phrases, price floor, required disclaimers, the framework your team already uses. House rules override the skill's method; the context document overrides everyone on facts. [How customisation works](CUSTOMISING.md).

## What is in this release

| Area | Jobs in index | Ready to use |
| --- | ---: | --- |
| [A. Foundation](SKILLS.md#foundation) | 1 | [product-marketing](skills/product-marketing/SKILL.md) |
| [B. Positioning and research](SKILLS.md#positioning-and-research) | 5 | Planned |
| [C. Copy and content](SKILLS.md#copy-and-content) | 7 | [copywriting](skills/copywriting/SKILL.md) |
| [D. Conversion](SKILLS.md#conversion) | 9 | [cro](skills/cro/SKILL.md) |
| [E. Offers and pricing](SKILLS.md#offers-and-pricing) | 4 | [offers](skills/offers/SKILL.md) |
| [F. Acquisition](SKILLS.md#acquisition) | 17 | [cold-email](skills/cold-email/SKILL.md) |
| [G. Lifecycle and go-to-market](SKILLS.md#lifecycle-and-go-to-market) | 10 | [sales-enablement](skills/sales-enablement/SKILL.md) |

Six skills are written to the house standard. Twelve more are scoped and next. The rest are named and mapped in [SKILLS.md](SKILLS.md), with the job each one covers and where an existing department skill already does the analysis.

We would rather ship six skills that hold up than fifty-three that do not. The status column is the honest one; check it before you rely on a name.

## Works alongside the department library

The [37 department skills](DEPARTMENTS.md#skills-by-area) cover reporting, sales, outbound, marketing, brand and operations. Choose a job in the [ChatGPT download catalog](CATALOG.md) or follow the [team deployment guide](company/DEPLOY.md). Use the [cross-reference](SKILLS.md#bridges-to-the-department-library) when a marketing deliverable needs a deeper analysis, such as qualifying the account list before drafting cold email.

For a custom company installation, contact [Greg at AI Close](mailto:greg@aiclosehq.com).

## Contributing

The most useful contribution is a case where an answer looked right and would have cost you money. [CONTRIBUTING.md](CONTRIBUTING.md) covers the report format, the skill checklist, and the rule that no placement is for sale.

## Licence

MIT. Structure and taxonomy adapted from [Corey Haines' marketingskills](https://github.com/coreyhaines31/marketingskills), used under the same licence. Every skill here is rewritten for revenue teams and follows the house contract above.

# Deploy AI Close skills

Start with one job in ChatGPT. Pick a result someone needs this week and use an input they recognize. A vendor quote, a CRM export or a customer email is enough for several jobs in the [skills catalog](../CATALOG.md).

For marketing work such as page copy, cold email or offer design, use the [marketing index on GitHub](https://github.com/gpm227/ai-close-skills/blob/main/SKILLS.md). Choose a **ready** skill, open its `SKILL.md`, and attach it and the **Bring** inputs to a ChatGPT project. Add your approved `close-context.md` and any house rules as project files. Keep company material in your private workspace. For competitive research, use Claude to collect dated sources, then bring the evidence into the job. Use Claude Design when the deliverable is a design or a brand kit.

The installation and version checks below cover the **37 department skills**. The six marketing skills have their own [setup and Claude plugin instructions](https://github.com/gpm227/ai-close-skills#install).

| What you need | Where to work | What to keep |
| --- | --- | --- |
| An everyday sales, marketing, reporting or operations job | ChatGPT with the relevant skill | The usable result, its source and anything the owner still needs to decide |
| Brand rules from a deck, website or approved writing | ChatGPT | An editable guide a writer or designer can use |
| A commissioned visual asset or designed brand kit | ChatGPT prepares the brief. Claude Design produces the work. | The editable source, approved export and owner’s decision |
| Deep research or competitive analysis | ChatGPT defines the decision. Claude Research investigates. | Dated evidence, comparable terms and a recommendation in ChatGPT |

[Try one job](#run-one-job-in-chatgpt) · [Use Claude](#use-claude-for-a-design-or-research-handoff) · [Set up the company repository](#create-the-company-repository) · [Share a release](#share-a-company-release) · [Verify employee installs](#verify-the-employee-experience) · [Update or roll back](#update-or-roll-back)

## Run one job in ChatGPT

1. **Get the right file.** Use the [catalog in this revision](../CATALOG.md) to download the ZIP beside your job. If your company already distributes a release, use the skill shared by its owner. A forwarded ZIP includes its own instructions, example and supporting files.
2. **Install it if your workspace supports Skills.** OpenAI lists eligible Business, Enterprise, Healthcare and Edu workspaces. Under **Plugins → Skills**, choose **Create → Upload from your computer** and select the original ZIP. Review the source and wait for the scan. Open any **Needs Review** details. A **Blocked** item requires a corrected file. Check **Installed** before proceeding. If upload is disabled, ask the workspace admin for the approved shared item. [ChatGPT skills and permissions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
3. **Give it your work.** Start a new chat, name the skill, attach the input and copy the request under **Try it on your work** in its instructions. For example, attach two vendor quotes and ask, “Which quote should we take? Compare total cost and payment timing. If the answer depends on our volume, give me the break-even point.” Check the deciding condition against a clause in your own quote.
4. **If Skills is unavailable**, extract a copy of the ZIP. Attach `SKILL.md` with your own input and ask ChatGPT to follow it. Supply any example, reference or script it needs from the same folder. For a calculation, check that the script actually ran or verify the result yourself. This gives you a manual trial. An installed team release has a separate check below.

**Try a known answer without company data.** Use the [reporting ZIP](../chatgpt/period-report.zip?raw=true) and [daily orders CSV](../proof/a/daily.csv?raw=true). If somebody sent you only the ZIP, extract a copy and use `period-report/examples/a/daily.csv`. Attach the CSV in a fresh chat and ask, “Use Compare this month with last month. How did orders change month over month through May 18, 2026? Give me the totals, dates and percent change.” Both April 1–18 and May 1–18 have **180 orders**, a **0% change**. A 40% drop means the answer used all of April. This example is an alternative to bringing your own job.

## Use Claude for a design or research handoff

**Brand guide or design.** In ChatGPT, give **Build a brand system** the available deck, website or approved writing, the intended reader and any cleared assets. Ask for the editable rules, their sources and open owner decisions. A guide-only job ends when the next writer or designer can apply a rule correctly. For commissioned design, send Claude Design the approved rules, copy and files, intended placement, audience, action and requested format. Open **Output → Design** or choose a Design template in **Artifacts**. If a shared design system is available, select it. Otherwise attach the cleared materials directly. Bring the editable asset and its export back to the owner. Check the actual delivery size, claims and destination before approving it. [Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) · [Shared design systems](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)

**Competitive research.** Start in ChatGPT with the decision, buyer, market and date. A usable brief is “Which of these three vendors can support five editors? Compare annual cash outlay, included seats and export rights. Cite each vendor’s current terms and flag terms we must ask sales to confirm.” On a paid Claude plan with web search enabled, choose **+ → Research**. Use web or desktop when the task depends on connected internal sources. Return the comparison, exact source links, dates and open questions to ChatGPT. Open the sources behind the decisive claims. Save the recommendation and the condition that would change it. [Claude Research](https://support.claude.com/en/articles/11088861-use-research-on-claude)

## Create the company repository

A maintainer does this once when the company wants to own and change the skills. Employees with an existing company release can [go straight to installation](#share-a-company-release). The company owns the repository and admin access. The department lead decides whether outputs are fit for use. One person can hold both roles.

Use Git and Python 3.9 or newer. On the reviewed **public** guide’s GitHub page, press **Y** to get its permanent link. Copy the full commit SHA between `/blob/` and `/company/`. Start in a working directory where the two example folder names are available. In the commands below, replace `PASTE_REVIEWED_SHA` with that SHA. Pick a lowercase company name and a new destination outside the public checkout. [GitHub permanent links](https://docs.github.com/en/repositories/working-with-files/using-files/getting-permanent-links-to-files)

```sh
git clone https://github.com/gpm227/ai-close-skills.git ai-close-skills
cd ai-close-skills
reviewed_commit=PASTE_REVIEWED_SHA
git fetch origin "$reviewed_commit" &&
  git checkout --detach "$reviewed_commit" &&
  python3 company/install.py ../example-company-skills --name example-company --ref "$reviewed_commit"
```

Continue after the installer reports the expected commit. The new private working copy has fresh Git history, a local catalog and one ZIP per skill. `UPSTREAM.json` identifies the public source. Each skill's `RELEASE.json` identifies the private plugin version and content digest. Run the verification and initial commit from the public checkout.

```sh
cd ../example-company-skills
python3 company/release.py verify plugins/department-skills &&
  python3 company/package_chatgpt.py --check &&
  git add . &&
  git commit -m "Install reviewed departmental skills"
```

Expect 37 verified skills and 37 matching downloads for this release. If Git asks for author details, configure the maintainer’s identity and retry the commit. To host this copy using an authenticated GitHub CLI, the following command **creates a new private repository and pushes the commit**. Replace `YOUR_ORG` with the company organization. For an existing empty private repository, use its own push instructions.

```sh
gh repo create YOUR_ORG/department-skills --private --source=. --remote=origin --push
```

## Share a company release

1. In the private checkout, choose the company's ZIP from `chatgpt/`. From a clean, committed release, record the output of `git rev-parse HEAD` and `python3 company/release.py verify plugins/department-skills`. Keep the ZIP name, version and plugin digest beside the upload record.
2. The publisher uploads that ZIP in the intended ChatGPT workspace. Open the skill menu, choose **Share**, and select the person or group. Save the shared item link, audience and date.
3. The employee opens **Plugins → Skills → Shared with me** or **Shared by [workspace]**, opens the item menu and selects **Install**. A partner in another workspace installs their own copy of the approved ZIP. [Installation and sharing](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
4. For recurring team work, create a shared ChatGPT project for approved source material, instructions and accepted outputs. Invite the intended participants. Deliver the skill itself through Skills. [ChatGPT projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

**Optional Claude organization distribution.** On Team or Enterprise, an owner enables Cowork and Skills, gives the Claude GitHub App access to the company’s private or internal repository, then opens **Organization settings → Plugins & skills → Marketplaces → Add plugins → Sync from GitHub**. Set the audience. For automatic sync, authorize the webhook and merge a version-bump PR to the default branch. If sync fails, members keep the last synced version. Fix the error, re-sync, check the version and audience in **Inventory**, and start a fresh employee session. [Claude organization marketplace](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

## Verify the employee experience

Have two people use separate accounts and fresh chats on each surface you plan to distribute through. The publisher gives each person their input and the May 18 question from above. Ask for **the comparison as JSON, a one-sentence conclusion, and the installed version and plugin_sha256 from RELEASE.json**. Save the JSON object alone in the named file. Save the sentence and observed receipt separately. Create the private evidence directory with `mkdir -p .local` from the company repository root.

| Employee | Input | Expected result | Check the saved answer from the company repository root |
| --- | --- | --- | --- |
| A | [Daily orders A](../proof/a/daily.csv?raw=true) | 180 → 180, flat | `python3 proof/check.py a .local/actual-a.json` |
| B | [Daily orders B](../proof/b/daily.csv?raw=true) | 180 → 144, down 20% | `python3 proof/check.py b .local/actual-b.json` |

Both comparisons use April 1–18 and May 1–18. The checker grades the JSON. Read the sentence separately. Compare each employee’s returned version and digest with the private receipt and recorded shared item. A matching answer with a missing or mismatched receipt leaves the served version unknown. Check the workspace, shared link, audience and installed copy, then rerun in a fresh chat.

The sample answers ship with the skill. For rollout, also give a colleague an unseen input and keep the lead’s expected result separate. Record what the colleague received, whether it passed, and whether someone used it for a real decision. For other jobs, substitute the department’s own input and criteria.

## Update or roll back

On a private branch, keep the failing input and actual output, write down the expected behavior, and identify a case that already works. **Improve a skill** can help prepare the correction. Edit the affected skill, increase the plugin version in `plugins/department-skills/.claude-plugin/plugin.json`, and run the four commands below.

```sh
python3 company/release.py stamp plugins/department-skills &&
  python3 company/release.py verify plugins/department-skills &&
  python3 company/package_chatgpt.py &&
  python3 company/package_chatgpt.py --check
```

Run the failing case and the previously good case. Have the lead review the outputs, commit the sources, receipts and ZIPs, and merge the approved release. Upload the changed skill’s ZIP in ChatGPT. Inspect which shared item the recipient can install. If a new item was created, share its link and have the recipient install that item. Verify the receipt and behavior in a fresh chat before retiring the old item. The digest covers the whole plugin. If other ChatGPT uploads still serve the earlier digest, keep them recorded at their actual version or upload and verify them too.

To roll back one skill, create a new branch from the current company release. Restore the skill from the accepted commit while retaining the current release receipt. For example, in a clean company checkout, replace `PASTE_GOOD_COMPANY_SHA` with the **company** commit that produced the accepted reporting result.

```sh
git switch -c restore-period-report
git restore --source=PASTE_GOOD_COMPANY_SHA --worktree -- plugins/department-skills/skills/period-report ':(exclude)plugins/department-skills/skills/period-report/RELEASE.json'
```

Review the restored files, increase the plugin version again, and repeat the four commands, review, distribution and employee check above. The rollback is complete when the prior behavior works under the new receipt. For an upstream change, compare it with the commit in `UPSTREAM.json` and review what you bring into the private release.

## Record feedback from the reporting pilot

The local feedback tool grades the two included reporting cases. It needs the actual saved JSON, a unique run ID and the receipt matched to that employee’s installed version. Keep a copy of that verified receipt with the run so a later update cannot change its attribution. The following example assumes employee A completed the run above and the checkout still matches their receipt:

```sh
cp plugins/department-skills/skills/period-report/RELEASE.json .local/run-a-receipt.json
python3 company/feedback.py finish run-a a .local/actual-a.json --input-ref case-a --receipt .local/run-a-receipt.json
python3 company/feedback.py summary
```

`finish` saves the artifact before scoring it. A failed check exits with status 1. An identical retry is safe. Give a revised output its own ID. If evaluation was interrupted, run `python3 company/feedback.py retry`. To find missing captures, put one completed run ID per line from an independent delivery record into `.local/completed-run-ids.txt` and run `python3 company/feedback.py reconcile .local/completed-run-ids.txt`. Read the missing, pending and outside-inventory lists. The database is local to this checkout. Ordinary chat needs manual capture or an integration that records actual completions.

Log feedback only when it happens. For a reported problem, use `python3 company/feedback.py vote run-a didnt-work --reason "Missing client context"`. If an employee used the result, use `python3 company/feedback.py outcome run-a used-in-report --evidence report-123` with the actual report reference. A passed check, employee feedback and business use answer different questions. For other jobs, the [run record](run-record.json) can hold the outcome, evidence, cost when measured and the release used.

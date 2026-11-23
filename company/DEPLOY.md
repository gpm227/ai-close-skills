# Deploy AI Close skills in your company

Start in ChatGPT. A team member can run a report, qualify accounts, write a brief or review a deliverable there. Bring in Claude Design when the job needs visual production. Bring in Claude Research when the decision depends on outside evidence. For recurring team jobs, keep approved files and findings in a shared ChatGPT project.

| Work | Where to do it | What the next person receives |
| --- | --- | --- |
| Routine reporting, sales, marketing and operations | ChatGPT with the relevant installed skill | The checked report, account list, draft or decision, with its source and open questions |
| Brand rules for writers and designers | ChatGPT uses the deck, website or approved material | Editable brand guide, source-backed rules and decisions for the owner |
| Commissioned design or visual brand kit | ChatGPT prepares the brief → Claude Design produces the requested assets → owner reviews them | Editable design and checked exports for the requested placements |
| Deep research and competitive analysis | ChatGPT scopes the decision → Claude Research investigates → ChatGPT applies the findings | Dated comparison with claim-level sources, evidence gaps and a recommendation for the decision owner |

## Try one skill in ChatGPT

1. Pick a job in the [public skills catalog](https://github.com/gpm227/ai-close-skills/blob/main/CATALOG.md). Download that skill's ZIP from the reviewed revision. If someone forwarded a GitHub `SKILL.md` link, open the repository name in its breadcrumb, then select **All 37 Skills** in the README. The catalog lists a Download link beside each job. For a quick trial, use the public examples. For company-specific rules, use the private release below.
2. In the company ChatGPT workspace, open **Plugins → Skills → Create → Upload from your computer**. Select the single skill ZIP. Wait for the scan. If the upload says **Needs Review**, inspect the flagged information. A **Blocked** upload cannot be used. Confirm the approved skill appears under **Installed**. OpenAI lists eligible Business, Enterprise, Healthcare and Edu workspaces. Availability depends on workspace permissions. If uploads are disabled, ask a workspace admin to enable them or share the approved skill. [ChatGPT skills and permissions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
3. Start a fresh chat. Attach your own material and use the request under **Try it on your work** in the skill instructions or the ZIP's `SETUP.md`. For example, give **Compare vendor proposals** two quotes, expected volume and a mandatory requirement. Ask which offer qualifies and how much cash each requires over the same term.
4. To check setup against a known answer, install **Compare this month with last month** (`period-report`) and attach `proof/a/daily.csv` from the reviewed repository in a new chat. Ask, “How did orders change month over month through May 18, 2026?” Expect 180 orders in each 18-day period, a 0% change. You can save the returned JSON for the check below.

If Skills is unavailable and you want to evaluate a written workflow, supply its `SKILL.md` and referenced inputs in a fresh chat. Record that as a manual trial. A workflow that needs code or rendered files still needs those capabilities before its result can be checked.

## Work with Claude on design and research

### Make a brand kit from a deck and a website

For a guide, give ChatGPT the available deck, site URL or capture, the intended reader and any approved assets. Ask for an editable guide a new writer or designer can use today. Check the source behind each material rule and resolve disagreements that change the buyer promise. Deliver the guide and the owner's open decisions. A guide can be the entire job.

When you need a designed asset, tell ChatGPT the placement, audience, buyer action and required format. Give Claude Design the cleared brief, copy, assets and a finished reference the owner trusts. In Claude, select **Output → Design** or open **Artifacts** and choose a Design template. Teams with design-system access can use the approved identity for future pieces. [Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design) · [Set up a design system](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)

Return the editable file and export to the owner. Check the real placement at delivery size, including legibility, approved claims, asset rights and the destination of the buyer action. Ask for revisions when the work misses an agreed requirement. Save the approved version with its source files.

### Answer a competitive question

Start with a decision a colleague actually needs to make. For example, “Which alternatives offer an editable brand kit to a five-person marketing team, at what price, and what would it cost us to switch?” In ChatGPT, agree on the competitors, geography, audience, comparison units and as-of date. Give Claude that brief and the approved public sources. In Claude, select **Research** with web access available. Use only the connectors appropriate to this task. [Research in Claude](https://support.claude.com/en/articles/11088861-use-research-on-claude)

Ask for one row per comparable offer with the plan, seats, price, currency, billing term, deliverable, exact source URL and date checked. Mark undisclosed prices and contradictory evidence explicitly. Return the table, source links and unresolved questions to ChatGPT. Open the primary evidence for claims that would change the decision. Then use the relevant skill to write the recommendation and explain which finding would change it. Store the dated evidence beside the decision so a colleague can refresh it.

## Install a company-owned release

The team lead owns what a good output looks like. A workspace admin controls access. A repository maintainer owns versions, release checks and rollback. One person can cover several roles. Keep client files, company rules, decisions and employee run records in company-approved locations. Use cleared or synthetic examples in the public repository.

**Set up shared working context.** When a colleague needs to repeat an accepted job, create a ChatGPT project, add the audience, owner, approved inputs and an example of an acceptable result, and invite the intended participants. Members install the reusable skill through the workspace's Skills directory. [ChatGPT projects](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

**Prepare the private repository.** Start from a clone of the [public repository](https://github.com/gpm227/ai-close-skills) with Git and Python 3.9 or newer. Check out the reviewed revision first. From that checkout, replace the example company name and choose a new destination outside the clone.

```sh
python3 company/install.py ../example-company-skills --name example-company --ref HEAD
cd ../example-company-skills
python3 company/release.py verify plugins/department-skills
python3 company/package_chatgpt.py --check
git add .
git commit -m "Install reviewed departmental skills"
```

The installer starts fresh Git history, records the chosen public commit in `UPSTREAM.json`, generates the company ZIPs in `chatgpt/`, and leaves remote configuration to the maintainer. Each skill's `RELEASE.json` contains its name, plugin version and the SHA-256 digest of the entire plugin's content. The digest identifies the plugin release. The ZIP check verifies that the upload files match their sources.

The company owns the hosting account, billing and recovery access. Create an empty private repository in its organization, set it as `origin` and push `main`. If you use the GitHub CLI, the following creates the private remote and pushes the initial commit. Substitute your organization and repository name first.

```sh
gh repo create COMPANY/department-skills --private --source=. --remote=origin --push
```

**Distribute in ChatGPT.** From this private release, upload the relevant `chatgpt/<skill-name>.zip`. For the reporting check, use `chatgpt/period-report.zip`. Open the skill's menu and select **Share**, then choose the intended members or group. A recipient opens **Plugins → Skills → Shared with me** (or the workspace's shared list), then selects **Install**. Record the release commit, ZIP filename, upload and sharing status, audience and date. A Git merge still needs a corresponding ChatGPT upload and workspace check. [ChatGPT installation and sharing](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

**Optional Claude team distribution.** Use this when employees also need the installed skills in Claude. A Team or Enterprise owner enables Cowork and Skills. Under **Organization settings → Plugins & skills → Marketplaces**, select **Sync from GitHub**. Grant the Claude GitHub App access to the company-owned private or internal repository and select the distribution settings available for your audience. For automatic updates, approve the webhook permission and merge a pull request with a plugin version bump. Manual re-sync is available. Record the sync result and workspace plugin version. [Claude organization marketplace settings](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

## Verify delivery with two employees

Use separate accounts and fresh chats on each surface you intend to support. The two public examples below are known-answer smoke tests. They and their expected answers are included in the upload. From the private repository root run `mkdir -p .local`. Each employee attaches the input, asks the May 18 question, saves the returned JSON under `.local/` and asks the skill for its release receipt. This directory is excluded from Git.

| Employee | Input | Expected prior → current orders | Check from company repo root |
| --- | --- | --- | --- |
| A | `proof/a/daily.csv` | 180 → 180, flat | `python3 proof/check.py a .local/actual-a.json` |
| B | `proof/b/daily.csv` | 180 → 144, down 20% | `python3 proof/check.py b .local/actual-b.json` |

Check that the employee’s written conclusion agrees with the numbers. The checker verifies the JSON fields; it cannot read a separately written conclusion. Both reports should compare May 1–18 with April 1–18. Record the surface, observed answers, checker results and receipt. Compare the returned version and digest with the locally verified receipt **and** the admin's upload or sync record. A correct calculation can coexist with an unknown served version. Mark the version unknown when the receipt cannot be read or corroborated. To test independent application, have the lead prepare an unseen export with different dates and totals and calculate the expected answer separately. Give employees only that export and the request. Grade their saved output against the private answer, and record whether anyone used it in a real report. For another workflow, use an unseen job and the owner’s criteria for its deliverable.

## Update, roll back and capture feedback

Edit company rules in a private branch. Retain the failing output and an example that already works. Bump the plugin version in `plugins/department-skills/.claude-plugin/plugin.json`. Run these commands from the private repository root.

```sh
python3 company/release.py stamp plugins/department-skills
python3 company/release.py verify plugins/department-skills
python3 company/package_chatgpt.py
python3 company/package_chatgpt.py --check
```

Have the team lead review the changed behavior, a fresh case and the release files. After approval and merge, distribute the new company ZIP in ChatGPT, confirm the intended audience is using it, and repeat the fresh-session check. Re-sync any Claude marketplace that serves this skill. To roll back, restore the known-good instructions, scripts and references from Git on a new branch. Retain the current receipts, assign a newer version, then stamp, package, review and verify the restored behavior through the same path. For an upstream update, compare the proposed public commit with `UPSTREAM.json` before bringing selected changes into private review.

The included feedback example checks the two period-report fixtures. For a manual pilot, capture the employee's actual JSON and the receipt from the identified release. Use a separate run ID for each completed revision. Run these commands from the private repository.

```sh
python3 company/feedback.py finish run-a a .local/actual-a.json --input-ref case-a --receipt plugins/department-skills/skills/period-report/RELEASE.json
python3 company/feedback.py summary
python3 company/feedback.py retry
python3 company/feedback.py reconcile .local/completed-run-ids.txt
```

`finish` saves the artifact before evaluation. Replaying an identical event is safe. A conflicting replay is rejected. A failed check exits 1. `retry` checks interrupted runs. For `reconcile`, supply an independent list of completed run IDs, one per line, for the same group of deliveries. It identifies missing captures separately from pending checks. The local record defaults to `.local/feedback.sqlite3`. Ordinary chat requires manual capture or a separate integration that supplies real completion events and the release used. [Claude plugin capabilities by surface](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

Record a correction and a downstream outcome separately. A report can pass the arithmetic check and still miss context its reader needs.

```sh
python3 company/feedback.py vote run-a didnt-work --reason "Missing context for the client"
python3 company/feedback.py outcome run-a used-in-report --evidence report-123
```

For a repeatable failure, give the evidence to **Improve a skill**. Keep the owner-approved benchmark, actual output and tested correction together. Use `company/run-record.json` for optional measured cost, private prompt references and observed business outcomes. Other skills need a check suited to their work before you can count their results as verified.

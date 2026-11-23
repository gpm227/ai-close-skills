# Install a company-owned skills library

The result is a standalone Git repository with the departmental skills, their release receipts and synthetic reporting checks. The company owns its hosting account and the workspace where the skills run. The installer runs locally with Python 3.9+ and Git. It copies tracked files from one commit and initializes fresh history.

## 1. Prepare the private copy

From a clone of the [public skills repository](https://github.com/gpm227/ai-close-skills), choose a reviewed commit. The commands below take the currently checked-out commit. Replace the example company name before running them.

```sh
python3 company/install.py ../example-company-skills --name example-company --ref HEAD
cd ../example-company-skills
python3 company/release.py verify plugins/department-skills
git add .
git commit -m "Install departmental skills from pinned upstream"
```

The script requires a new directory outside the public checkout. It does not contact a hosting service. UPSTREAM.json pins the public commit. Each skill's RELEASE.json identifies its company plugin version and a SHA-256 digest of the content shipped in that plugin. Store company rules in the skills that use them or their referenced files. Make changes through the company's normal review process.

## 2. Publish inside the company's account

The admin creates an empty private repository owned by the company and confirms its visibility. Add its clone URL as origin and push main. A company using the GitHub CLI can instead run the following in the generated repo, substituting its actual organization and repo name. The command creates the private remote and pushes the initial commit.

```sh
gh repo create COMPANY/department-skills --private --source=. --remote=origin --push
```

For a managed install, the business owns the organization, billing, and recovery access and can revoke the implementer's access. For an IT-led install, the CTO reviews repo scope, workspace permissions, approved data destinations, retention, and access removal. The team lead owns the department's standard. Configure review protection on the release branch where supported. Keep business data and employee run records out of the public project.

## 3. Install in ChatGPT and verify delivery

Each file in `chatgpt/` is one upload for an eligible workspace. In ChatGPT, go to **Plugins → Skills → Create → Upload from your computer**, select the relevant file, then share the installed skill with your workspace from its menu. An outside partner installs their own copy. Workspace permissions apply. [OpenAI instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

In a new conversation, invoke the skill on your acceptance case. Ask for the installed release and compare its version and digest with the receipt in your company checkout. After approved edits, stamp the release, run `python3 company/package_chatgpt.py`, and upload the revised bundle. Record the result of a fresh run in that workspace.

### Connect Claude and verify delivery

A workspace Owner or Primary Owner confirms the supported plan and that Cowork and Skills are enabled. In organization settings under Plugins & skills, add a marketplace and select Sync from GitHub. Connect the company-owned private or internal GitHub repo. Grant the Claude GitHub App access to that repo and select the intended employee audience. For automatic updates, approve the required webhook permission and use a merged PR with a plugin version bump. The admin can also re-sync manually. [Organization marketplace settings](https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization)

Record the private release commit, the locally verified digest, Claude's sync result, the plugin version shown in the workspace, and the date. Have two employees use separate accounts and fresh sessions. Employee A runs the period report on proof/a/daily.csv. Employee B uses proof/b/daily.csv. Give each the same ordinary request about orders through May 18. Ask for the installed release receipt after the report. Compare the returned digest with the verified local receipt and the admin's sync record. Treat an unreadable receipt as unknown. Record the actual outputs, source dates, checks, workspace surface and evidence in a company-approved location. A model's statement alone cannot establish what was served.

## 4. Ship a change or restore prior behavior

Change the skill in a private branch and increase the version in plugins/department-skills/.claude-plugin/plugin.json. Stamp and verify the release before review.

```sh
python3 company/release.py stamp plugins/department-skills
python3 company/release.py verify plugins/department-skills
```

The team lead reviews the behavior change and examples. Merge, sync and confirm the served receipt in a fresh session. To roll back, restore the working instructions and any associated reference files from a known-good commit on a new branch. Keep the current receipts, assign a newer plugin version, then stamp, test and review the restoration. The release history shows when the old behavior returned. For upstream upgrades, compare the pinned upstream revision with the proposed revision and bring selected changes into a private PR.

## Feedback for the reporting example

The local command below is a reference implementation of a completed-output event. An integration can call it when it produces the final artifact. Supply the run ID, case, JSON output, approved input reference and receipt from the release actually used. Use an independent ID for each completed revision. The local database defaults to .local/feedback.sqlite3. It stores the actual reporting JSON, plus the receipt, benchmark fingerprint, verdict and any subsequent employee or outcome records. Use synthetic data locally until the company approves storage, access and retention. The example evaluator supports the two reporting benchmarks.

```sh
python3 company/feedback.py finish run-a a actual-a.json --input-ref case-a --receipt plugins/department-skills/skills/period-report/RELEASE.json
python3 company/feedback.py summary
python3 company/feedback.py retry
python3 company/feedback.py reconcile completed-run-ids.txt
```

The finish command persists the artifact before the check. Replaying the same event is safe. Conflicting evidence under the same ID is rejected. A failed check records the evidence and exits 1. A checker interruption leaves the run pending. Retry checks pending runs using the original benchmark. Reconcile compares against an independent list from the delivery system, one completed run ID per line for the same pilot scope. It reports outputs missing from capture separately from pending checks and outputs outside that inventory.

An employee can optionally record a correction even after an automatic pass. Outcomes arrive separately, with evidence from the system where they were observed.

```sh
python3 company/feedback.py vote run-a didnt-work --reason "Missing context for the client"
python3 company/feedback.py outcome run-a used-in-report --evidence report-123
```

For other skills, establish an owner-approved standard and evaluator first. A workspace connector still needs to supply real completion events and the correct release, then reconcile interrupted work, revisions and follow-ups against an independent inventory. Ordinary Claude chat does not run plugin hooks. Cowork and Claude Code have different capabilities. [Plugin support by surface](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)

If a check or staff report reveals a repeatable issue, give the evidence to improve-skill. The optional run-record.json template also provides fields for measured costs and private prompt references. An observed outcome and the quality-check verdict answer different questions.

# Make this library yours

The skills are a base. Your judgement, your prices and your proof are what make them worth using. This file covers where that judgement goes, so an upstream update never overwrites it.

## What survives an update

| Path | Yours or theirs | What happens on update |
| --- | --- | --- |
| `skills/` | Theirs | Replaced. Do not edit a skill in place if you want the fix later |
| `custom/` | Yours | Never touched |
| `.agents/` | Yours | Never touched, and never committed |
| `docs/`, `tools/` | Shared | Improved upstream; local edits may conflict |

In a chat project, attach the context document and any applicable house-rule files. With a coding agent, keep them in the project where you do the work. Personal files under `custom/` and `.agents/` are ignored by Git in this public checkout. To share rules with colleagues, track the approved files in your private company repository.

Keep your house rules in `custom/`, and keep facts in the context document. The two are different: a house rule is a decision that applies to every draft, and a fact is something that is true about the business today.

## Four levels of customisation

1. **Context only.** Run `product-marketing` and keep `.agents/close-context.md` current. Most teams need only this.
2. **House rules.** Add `custom/<skill>.md` for the decisions a skill cannot know: banned phrases, price floor, disclaimer text, approval route, the framework your team already uses.
3. **Fork a skill.** Copy it to `skills/<name>/` and change the method. Record the change in `custom/<name>.md` so the reason survives, and expect to re-apply it after an upstream update.
4. **New skill.** Start from [docs/SKILL-TEMPLATE.md](docs/SKILL-TEMPLATE.md), run `bash tools/check.sh`, and add it to `SKILLS.md`.

## Precedence

When instructions disagree, resolve in this order:

1. **The context document wins on facts.** Price, proof, permission, and who the buyer is.
2. **`custom/<skill>.md` wins on method.** If your house rule says never to use a guarantee as a risk reversal, the skill does not use one.
3. **`custom/_house.md` applies across jobs.** Use it for shared editorial and review rules. Use `custom/tools.md` for the tools your team actually has.
4. **The skill wins on everything else.** It holds the craft.

Never put a fact in a house-rule file. A price recorded in two places will one day be wrong in one of them.

## Rules for homepage copy

`custom/copywriting.md`:

```markdown
# Copywriting house rules

- Never write a number we have not published. If a claim needs a number, ask for the source.
- The words "platform", "solution" and "journey" do not appear in our copy. Use the plain noun.
- Every pricing page states the setup fee. No exceptions, including experiments.
- Two people approve a homepage change: the founder and the person who owns the claim.
```

Each line changes what a draft can contain. None of them is an adjective about tone, which is the usual failure mode of brand guidance.

## The review step

A house rule is a change to how everyone writes. Treat it like code:

- One person proposes it with the draft that prompted it.
- The owner of that surface approves it.
- Add a line to `custom/CHANGELOG.md` with the date and the reason.
- Run `bash tools/check.sh` before committing.

## Things worth customising first

- **Discount approval route** in `custom/offers.md`.
- **Banned phrases and claims** in `custom/copywriting.md`.
- **Stage definitions and CRM fields** in `custom/sales-enablement.md`.
- **Opt-out and legal footer text** in `custom/cold-email.md`.
- **Your framework names**, if your team already speaks in one. A skill that contradicts your internal vocabulary gets ignored.

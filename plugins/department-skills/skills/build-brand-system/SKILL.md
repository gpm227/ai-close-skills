---
name: build-brand-system
description: "Build a company's visual brand system and copy voice from its overview deck and website. Use when a partner needs an editable brand guide and a design brief to take an applied piece through visual review in the partner’s chosen design tool."
---

# Build a brand system from a deck and a website

Build the reusable brand system first. Then use one real buyer-facing piece to test whether another designer can apply it. ChatGPT delivers the editable guide, voice rules, cleared copy, asset requirements and a production brief. Use the partner’s chosen design tool (including Claude Design) for composition and revision. Keep each design version with its review. An HTML copy proof is an intermediate artifact.

## First use

When a partner asks to try the installed skill, use the bundled fictional example. Run `python3 scripts/render.py examples/example.json demo-output` from the skill directory, choosing a fresh output directory on later runs. Return the guide, voice brief, design brief and copy proof. For a real job, read the partner’s deck and website, build their structured source yourself, and return their files. They do not have to write JSON or run terminal commands. If file execution is unavailable, identify that limitation before describing any output as generated.

## Read the actual materials

Read the relevant PDF pages as rendered pages as well as text. Open the supplied website and the specific service or audience page needed for the example. Capture page numbers, exact URLs or provided snapshot paths, dates when known, and short verbatim evidence. Inspect the logo treatment, palette, type hierarchy, page density, illustration patterns and how the company refers to its buyers. Use supplied rights-cleared assets if available. Preserve the logo proportions; a missing original calls for a text wordmark clearly identified in the guide as a placeholder. If a site or visual cannot be inspected, name the gap and proceed from the accessible evidence; ask for a screenshot or export only when it changes the outcome.

Build a working source register. Distinguish internal evidence from public copy clearance. A PDF sent privately can support understanding while its customer names, performance figures or operating details may need approval for public use. Keep quotes and the register in the guide. Never send source material to third parties. Where the deck and website conflict, show the discrepancy and its consequence. Ask the owner only if a choice changes the buyer promise, identity or intended next action.

## Freeze the brief before drafting

Record the audience, buyer action, owner-supplied language examples, visual priorities, output files, sources and acceptance criteria in a short spec. Include V1 voice fidelity, V2 icons that explain distinct jobs and V3 low text density. Define an observable check for each against this client's sources. Set any missing choice as a working assumption for the owner. Preserve this version across both reviews. A genuine owner change gets a dated amendment.

When the owner supplies a strong finished piece, read it at page size and at thumbnail size. Map the buyer questions it answers, the order the eye encounters them, how images or diagrams carry meaning, and how the buyer acts. Capture this as the visual benchmark. Distinguish reusable principles from design choices specific to that audience or offer. Identify anything pending in the reference, such as uncleared partner artwork. Use the current brief to choose what transfers to the new piece.

## Make the decisions a partner hired you to make

- Identify the buyer, the actual job, the product mechanism and the supportable outcome. Give different audiences different reasons to care when the evidence supports a difference. Choose one audience and one job for the one-sheet. Define what happens after the CTA. A form or conversation does not deliver an immediate quote.
- Recover the company’s voice from usage. For each material rule, give a source cue, an instruction, and an original before/after pair that changes meaning or diction in a visible way. Include preferred terms and who they refer to. Keep factual qualifications, human authorship and permissions intact. Mark any new editorial choice as proposed. Reject voice rules that could be pasted unchanged into a competitor’s guide without changing the sample copy.
- Record the existing visual identity separately from proposed extensions. Specify color roles with exact values when verified, hierarchy and channel-appropriate type fallbacks, logo use, icon geometry, spacing and information density. Distinguish observed type from a suggested substitute. Give a writer and designer enough detail to reproduce the page tomorrow.
- Decide what relationship the buyer needs to understand: a sequence, services working together, a comparison, or evidence for a choice. Specify the layout, imagery, diagram and supporting copy that best explain it. Explain any connector, band, label or repeated icon in terms of that relationship. Use real photography or assets when appropriate and cleared. Keep labels readable at the delivery size.
- Keep the first scan economical while giving the buyer enough information to act. Read each label and its supporting line together. If the line only paraphrases the label, omit it. Include a line when it adds an actor, decision, qualifier or new fact. Cut duplication. Preserve the mechanism, specific service language, qualifications and relevant next step. Apply a word limit only when the owner or format supplies one.

## From ChatGPT to design production

Read references/format.md and populate the structured brand file. Write production.direction (the composition and its reading order), production.relationship (what the visual must explain), production.assets (approved artwork, permitted source material, and unresolved assets), and production.acceptance (checks specific to the supplied design benchmark). Use these decisions to brief the designer. Run `python3 scripts/render.py brand.json OUTPUT_DIRECTORY` to generate the guide, voice brief, design brief and copy proof. Return the editable brand file. Supply any additional source-cleared copy or supporting evidence the actual composition needs outside the proof’s cards. Use the design brief and approved assets to commission an editable design and a rendered export. The partner controls which files go to an external tool.

When the design tool is available and authorized, produce or revise the comp there. Otherwise deliver the handoff, mark visual production pending and request the rendered comp when it exists. Do not report that the copy proof passed visual review of the finished design.

## Evaluate and refine in at least two separate turns

Keep the initial design export. Review 1 checks the actual composition against the owner’s reference: buyer promise, focal point, reading order, and whether the visual explains the relationship. Review 2 checks the revised export at delivery size: what the buyer understands, evidence, next action, brand fidelity, and any missing artwork. Record the design file/version reviewed. Both turns require visible work to examine. Never deliver it as the finished result. In review turn 1, compare the rendered first draft and evidence to **each** criterion in the frozen spec. Quote the actual copy or identify the specific visual location. Record pass, fail or unknown, the reason and the edit. Produce and render a revised version. In review turn 2, inspect **that revised version** anew against the same spec. Test meaning without the paragraphs, check any qualifier removed for brevity, and read the copy aloud in the source company's voice. Make the second revision and render it. These are successive reviews of different artifact versions. A single response inventing two retrospective critiques does not satisfy the standard. Use fresh reviewer turns when available. In a single-response environment, give the current stage and continue the reviews in subsequent chat turns. Do not require the partner to supply feedback just to advance a review.

Keep a private review record with the frozen criteria, version or file hash, evidence and actual changes for each turn. Keep passing language unchanged unless a documented improvement warrants an edit. If a criterion is unknown, identify what would settle it. If required checks still fail, continue refining or withhold the release designation. The owner decides whether this is worthy of becoming their template.

Deliver the guide, voice brief, production brief and editable source. Include the final designed piece only when the actual design was produced and reviewed; otherwise label the copy proof and the outstanding design step. Lead the response with the finished work and the one decision, if any, that still blocks external use. Keep provenance out of public copy. An owner approves a new direction before it becomes the team's standard.

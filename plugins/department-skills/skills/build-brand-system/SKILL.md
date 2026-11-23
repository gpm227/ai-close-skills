---
name: build-brand-system
description: "Derive a reusable visual identity and writing voice from a company's deck, website or supplied captures. Use for a brand guide from existing materials, an editable brand kit, or a designer handoff and proof when requested. For applying an existing approved kit to one asset or auditing a finished piece, use the corresponding production or review skill."
---

# Build a brand system from a deck and a website

Give a second writer and designer enough to produce a recognizable piece without the original conversation. Work in ChatGPT from the materials the owner can share. A request for a brand system or kit calls for an editable guide. Add an applied piece, a designer handoff or a visual review only when the owner asks for it.

## Start with the materials

For an explicit demo, read [the fictional repair-shop request](examples/brief.md), then run `python3 scripts/render.py examples/example.json demo-output` from the skill folder. For a real brand, use the client's files. Never substitute the demo for an inaccessible input. The partner supplies business materials and receives usable files. The agent handles JSON and commands. A guide can be written directly in Markdown. The renderer is optional for jobs that include a structured master or an applied proof.

1. Inspect what was supplied. For a deck, read the rendered slides and text. For a site, open the relevant pages or use labeled captures. If there is a proposed action, inspect its destination. Record what can actually be established about that destination. A snapshot can establish the displayed destination and form wording; a successful submission requires separate evidence.
2. Map each distinctive decision to a locator (slide number, exact URL and section, or capture filename and section) and a short exact excerpt or a labeled visual observation. For visual sources, record the roles you can see. Include cover, body and action treatments when present. Distinguish verified CSS or supplied font files from a screenshot estimate. Never identify an exact font or hex value by appearance alone.
3. Record which inputs were inspected, captured offline, or unavailable. One approved page, excerpt, email or screenshot is enough to start. Produce a provisional guide covering the roles visible in it. With text alone, deliver the writing rules and leave the visual identity unverified. With zero usable sources, request one file, capture or export and pause the reconstruction. Never invent a second source.
4. Label each source public, internal, or unconfirmed. Record competing versions and what would change for a buyer. Use an explicit owner's instruction or a clearly authoritative, current source to resolve the difference. An observed live form establishes its actual next step. An internal slide cannot enlarge a public claim. Hold a disputed claim, logo, or commitment until the specific owner decision is documented. If material is cleared only for the owner's team, keep decisions and examples in their internal guide. If the intended recipient is unclear, give the owner the internal version and ask which material may travel.

## Deliver the editable guide

Start the guide with its intended reader and what they should be able to produce. For each supported rule, give the source cue, the instruction, a concrete application, and its scope (owner-approved, observed in this source, or proposed). Describe unanswered decisions only where they affect the next piece. Use exact values, approved files and channel exceptions when available.

For a writer or designer outside the team, put only recipient-cleared decisions and original shareable examples in the guide. Keep private locators, source excerpts, disputes and clearance records in a separate owner note. Use a simple handoff test: apply one rule to a new line of copy or describe how to set one existing element. Check that it preserves the source facts. Deliver the editable guide at this point for a guide-only request.

For example, one approved service email reads “Reply with a photo of the binding. Our estimator will confirm whether we can repair it.” A usable rule for intake emails is “Name what the customer sends and who decides next.” An original application is “Reply with a binding photo so our estimator can check whether repair is possible.” Preserve the condition that repairability is checked. One email establishes neither a turnaround promise nor a house typeface.

## Rules to check against the supplied materials

- **Voice.** Name the buyer, the product mechanism and who takes each action. For each material rule use a source cue, an instruction, and an original before/after rewrite. Preserve qualifications. Distinguish observed terminology from proposed editorial treatments. Test the rule on one new line. Try another channel only when its scope supports the extension. If a competitor could use it unchanged, make the rule more specific.
- **Visual identity.** Separate observed rules from proposed extensions. When source CSS is available, inspect the rendered role and its actual declaration, including inherited variables, media overrides and the `font` shorthand. A palette inventory is a starting point: match each retained token to an element in the supplied material. Document the roles the evidence actually establishes: for example, headline and body hierarchy, placement of the logo, or the color used for the main action. Leave unverified values open. A requested production handoff can identify a temporary substitute and its limits. Avoid treating a familiar serif, tinted background, grid/callout, or any other favorite treatment as an identity. Verify rights for artwork. No unsupported font or logo files go in the handoff.
- **Composition (for visual materials).** Identify the relationship the buyer needs to see: an ordered handoff, parallel services, a comparison, or a choice supported by proof. Name the focal point, order, geometry or photography, distinct icon meanings, and what a buyer should understand at first scan. Add a supporting line only when it adds a decision, actor, qualifier or fact. A word limit applies only when supplied by the owner or format.
- **Claims.** Trace the headline, supporting claims and proposed action to cleared sources. Verify their actual meaning, including geography, deadlines, conditions and permissions. A syntactically valid reference or URL cannot confirm a promise. If a destination is missing, hold the affected call to action and deliver the other supported guidance.

## If the request includes a design deliverable

For a requested design brief, applied proof or review of actual versions, follow [the visual handoff workflow](references/design-handoff.md). The [editable file format](references/format.md) documents the optional renderer. Agree on the specific deliverable first. A brief is ready when a designer can act on it. Visual acceptance requires a rendered version and a review at the target size.

## Try it on your work

A deck, website, capture or approved piece of writing, plus the intended reader.

> Build an editable brand guide from these materials. Show the voice and visual rules we can use today, their sources and the decisions the owner still needs to make.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `build-brand-system.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

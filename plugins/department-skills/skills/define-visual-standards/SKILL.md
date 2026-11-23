---
name: define-visual-standards
description: "Documents the fonts, colors, spacing, imagery and layouts that make a brand look consistent, tied to your real design files. Use for visual guidelines, a design system summary, brand standards, or \"how should our stuff look.\""
---

# Define the visual standard

Produce role-based visual rules someone can apply at the actual delivery size. For a full writing and design kit derived from a deck and website, use the brand-system workflow.

## You'll need

- **Your real design source.** Token files, Figma, CSS, or brand files.
- **Approved examples.** Screens, decks, print pieces.
- **Logos and font files,** or where they live.
- **Where it'll be used.** Web, email, print, slides.

If all you have is a screenshot, the result is a set of observations, not measured values.

## Steps

1. Map every role (heading, body, button, error, link) to an existing value before proposing new ones.
2. Set the heading hierarchy, content width, spacing scale, action and status colors, icon set and chart style.
3. Give one desktop layout and one phone layout.
4. Cover the awkward cases: long labels, wrapping, empty states.
5. For print: page size, margins, and how it looks in grayscale.
6. List anything unverified: font licenses, contrast checks.

## Reconcile evidence before choosing values

For each role record channel and state, token/value or visual observation, source and version/selector, allowed use, and status. Mark an active approved source as specified, a rendered appearance as observed, and a new design decision as proposed. A channel's active tokens govern that channel; an older deck may still govern print. Show discrepancies at the place where they change work. Never infer exact type, color or clearance from a screenshot.

For colors, test the foreground/background pair where it is actually used, including alternate backgrounds and interaction states. Cite the contrast target applicable to the output. If checking a web artifact against WCAG, verify the current relevant success criterion and exceptions using the official reference. Record the measured ratio, size and pair. For type, state the approved medium, permitted distribution, live availability and fallback. For logos and imagery, direct the implementer to the cleared asset/variant.

Hand the designer a concrete specimen (or a written recipe if production is unavailable), record its target dimensions and which renders you actually inspected. Test long labels, missing assets and print output on the affected surface. Scope untested combinations explicitly.

## What you get back

A role-to-value table, layout recipes, links to approved assets, and a checklist. Every entry is marked observed, specified, or proposed.

## The trap

A teal sampled from a screenshot reads #1F7A6C. The design file says #176B60. The screenshot is wrong because of compression. A sampled color is a guess until it matches the source file.

## Check it

- Every value traces to a source file or is marked proposed.
- Status colors never rely on color alone. There's a label or icon too.
- Text passes contrast at its actual size.

Use [the released CSS and slide exception case](examples/practice.md) to practice separating measurements from proposals.

**Using this skill for the first time?** On the public GitHub page, open the repository name above this file. In its README, **All 37 Skills** takes you to the individual downloads and **deployment guide** covers team setup. In a downloaded ZIP, open `SETUP.md` for the installation and source links. In a company copy, start at `company/DEPLOY.md`. For native installation, follow [OpenAI’s upload instructions](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

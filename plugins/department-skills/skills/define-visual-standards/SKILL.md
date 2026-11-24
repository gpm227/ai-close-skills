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

One approved slide, screenshot or page is enough to document a starting standard. Name the surface, describe the visible roles and show how to apply one of them to the next item. From a screen capture showing a filled main button and an underlined secondary link, for example, specify that hierarchy for the next screen and leave exact colors and type values open. If the source cannot be opened, request a single capture or the relevant token declaration.

## Steps

1. Inventory the roles present on the requested surface. Map each role to its declaration or observation before proposing changes.
2. Describe how to reproduce the hierarchy, spacing, actions and other elements that actually recur.
3. Give a written layout recipe for the requested format. For responsive web work, include its desktop and phone behavior.
4. Cover likely failure cases for that surface, such as long labels and empty states on a form or cramped captions in slides.
5. For a print request, include known page size, margins and grayscale behavior.
6. Record missing measurements, rights or checks that affect this use.

## Reconcile evidence before choosing values

For each role record channel and state, token/value or visual observation, source and version/selector, allowed use, and status. Mark an active approved source as specified, a rendered appearance as observed, and a new design decision as proposed. A channel's active tokens govern that channel; an older deck may still govern print. Show discrepancies at the place where they change work. Never infer exact type, color or clearance from a screenshot.

For colors, test the foreground/background pair where it is actually used, including alternate backgrounds and interaction states. Cite the contrast target applicable to the output. If checking a web artifact against WCAG, verify the current relevant success criterion and exceptions using the official reference. Record the measured ratio, size and pair. For type, state the approved medium, permitted distribution, live availability and fallback. For logos and imagery, direct the implementer to the cleared asset/variant.

Use a written recipe and point to an existing example for a standards request. Build a new specimen only if the user requests one. Record which existing renders and delivery sizes you actually inspected. Document applicable failure cases and scope untested combinations explicitly.

## What you get back

A role-to-value table, layout recipes, links to approved assets, and a checklist. Every entry is marked observed, specified, or proposed.

## The trap

A teal sampled from a screenshot reads #1F7A6C. The design file says #176B60. The capture shows the apparent color for that rendered example. Use the active source declaration for the specified value and record any discrepancy.

## Check it

- Every value traces to a source file or is marked proposed.
- Status colors never rely on color alone. There's a label or icon too.
- Text passes contrast at its actual size.

Use [the released CSS and slide exception case](examples/practice.md) to practice separating measurements from proposals.

## Try it on your work

Approved design files, exports or screenshots, and the surface where the rules will be applied.

> Document the reusable type, color, spacing and imagery rules. Cite the source for each, and identify values that still need an editable file or owner decision.

**Get the download.** On GitHub, keep the branch or commit shown for this file. Open `CATALOG.md` in the repository’s file tree and download `define-visual-standards.zip`. If someone sent you the ZIP, open its `SETUP.md` for the first run. For a company release, use `company/DEPLOY.md` in your private repository.

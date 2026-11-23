# Editable brand file

Write UTF-8 JSON. Each reference in refs is a source ID. Every source has an id, locator (PDF page, URL or snapshot section), excerpt and clearance: public, internal or unconfirmed. The source register stays in the internal guide.

| Key | Required content |
| --- | --- |
| company, audience, positioning | Company, the one-sheet buyer and a specific supportable positioning sentence |
| status, decision | "draft" or "owner-approved"; exact outstanding decision, evidence gap or approval reference |
| sources | Array of source objects |
| voice | Array of at least two objects: rule, before, after, refs. Capture terminology and claims qualifications inside these rules. |
| visual | Array of objects: rule, status ("observed" or "proposed"), refs. Cover logo handling, type/fallbacks, palette, icon style and density. |
| layout | Choose comparison for parallel benefits, sequence for ordered steps, or index for a fast label-and-detail reference. Explain the choice in visual. |
| font_stack, heading_font_stack | Optional local CSS font stacks. Use source-appropriate fallbacks. |
| color | Primary applied text and background as ink and paper (six-digit hex colors). Add action for CTA and icon ink when the identity supplies a distinct action color. Document the origin of color choices in visual. |
| sheet | headline, intro, cards, cta, destination and refs. Use a specific https URL for a supplied next step, or an empty destination with an explicitly unresolved decision. |
| sheet.cards | Two to four objects: icon, label, text and refs. Pick a distinct concept per card. |
| production | For a new brief supply direction, relationship, assets and acceptance as specific text. Older files without this section produce a handoff flagged for completion. Keep the owner’s private reference in its authorized location. |
| copy_limit | Optional positive integer. Count the sample headline, intro, labels, body and CTA only when the brief supplies a budget. |
| logo | Optional filename of an approved local PNG or JPEG next to brand.json, e.g. logo.png. The renderer embeds it and preserves aspect ratio. Without an asset it displays company text. Document any outstanding logo file request under visual. |

Icons available: route (movement/handoff), inspect (inspection/search), record (written record), protect (protection), time (timing), people (people/team), signal (measurement or signal), package (physical goods), payment (transaction), place (location), calendar (schedule), tools (maintenance). Choose by meaning. For a missing concept, set the card's icon to custom and supply an svg_path containing a simple valid SVG path in a 24×24 viewBox. Use a consistent unfilled two-unit stroke; give each custom icon a distinct path. Check visual meaning in the rendered page.

All claims in the one-sheet must trace to publicly cleared source IDs. An observed visual rule needs evidence. An intentional new design choice uses status proposed. The reference check establishes a link; read the cited material to confirm it actually supports the wording. Omitting a claim is preferable to upgrading private evidence into a public promise.

When working offline use labeled website captures and disclose the snapshot date if supplied. Do not imply the live site was inspected. A fresh-session proof should include one additional channel, e.g. a homepage hero or a follow-up email made by a second writer with only the finished voice brief.

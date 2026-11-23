# Editable brand file

Write UTF-8 JSON. Each reference in refs is a source ID. Every source has an id, locator (PDF page, URL or snapshot section), excerpt and clearance: public, internal or unconfirmed. The source register stays in the internal guide.

| Key | Required content |
| --- | --- |
| company, audience, positioning | Company, the one-sheet buyer and a specific supportable positioning sentence |
| status, decision | "draft" or "owner-approved"; exact outstanding decision, evidence gap or approval reference |
| sources | Array of source objects |
| voice | Array of at least two objects: rule, before, after, refs. Capture terminology and claims qualifications inside these rules. |
| visual | Array of objects: rule, status ("observed" or "proposed"), refs. Cover logo handling, type/fallbacks, palette, icon style and density. |
| layout | Use specimen when a cleared visual teaches the buyer a specific decision. Transcript is the default for a copy-only job. Existing comparison, sequence and index proofs remain readable. Layout conveys no owner approval. |
| font_stack, heading_font_stack | Optional local CSS font stacks. Use source-appropriate fallbacks. |
| color | Optional for transcript-only work. Omitted values yield plain high-contrast proof text. Primary applied text and background as ink and paper (six-digit hex colors). Add action for CTA and icon ink when the identity supplies a distinct action color. Document the origin of color choices in visual. |
| sheet | headline, intro, cards, cta, destination and refs. Use a specific https URL for a supplied next step, or an empty destination with an explicitly unresolved decision. |
| sheet.cards | Two to four objects: icon, label, refs and optional text. Omit text when the label fully explains the job. Pick a distinct concept per card. |
| production | For a new brief supply direction, relationship, assets and acceptance as specific text. Older files without this section produce a handoff flagged for completion. Keep the owner’s private reference in its authorized location. |
| copy_limit | Optional positive integer. Count the sample headline, intro, labels, body and CTA only when the brief supplies a budget. |
| logo | Optional filename of an approved local PNG or JPEG next to brand.json, e.g. logo.png. The renderer embeds it and preserves aspect ratio. Without an asset it displays company text. Document any outstanding logo file request under visual. |

Icons available: route (movement/handoff), inspect (inspection/search), record (written record), protect (protection), time (timing), people (people/team), signal (measurement or signal), package (physical goods), payment (transaction), place (location), calendar (schedule), tools (maintenance). Choose by meaning. For a missing concept, set the card's icon to custom and supply an svg_path containing a simple valid SVG path in a 24×24 viewBox. Use a consistent unfilled two-unit stroke; give each custom icon a distinct path. Check visual meaning in the rendered page.

All claims in the one-sheet must trace to publicly cleared source IDs. An observed visual rule needs evidence. An intentional new design choice uses status proposed. The reference check establishes a link; read the cited material to confirm it actually supports the wording. Omitting a claim is preferable to upgrading private evidence into a public promise.

When working offline use labeled website captures and disclose the snapshot date if supplied. Do not imply the live site was inspected. A fresh-session proof should include one additional channel, e.g. a homepage hero or a follow-up email made by a second writer with only the finished voice brief.

For new jobs include the following alongside the original fields. Older files without these fields still render.

- `inputs` accounts for both `deck` and `website`. Each has a `state` (`inspected`, `snapshot` or `unavailable`), `detail` (what was inspected or why access failed), and `refs`. For an unavailable input use an empty list. The register records exact quotations or visual observations explicitly labeled as such. Never invent an excerpt for a missing file.
- `conflicts` is an array (empty when none). Each row has `issue`, `refs` covering both sides, `state` (`resolved` or `open`), and `decision` giving the rule used or claim held. An open conflict requires a draft. Put no disputed or private claims into the applied piece. A missing CTA destination likewise keeps the job in draft.
- Set `sheet` to `null` for a private guide with no cleared buyer copy. Include company, audience, positioning, status, decision, sources, voice, visual and color as usual. The renderer emits only the internal guide and voice brief. Omit production and layout for this mode.
- The design brief carries the exact applied color roles, font stacks, logo status and each icon assignment. Only visual rules whose references are public (or proposals using no protected sources) appear there. Review these fields, the buyer copy and production notes for permission and accuracy before giving the brief to another tool. Keep the full register, disputed claims and internal writing examples private.

- In a full job the portable voice brief includes only rules based entirely on public references. For a mixed/private rule, optionally supply a sanitized `portable` object with its own `rule`, `before`, `after` and publicly cleared `refs`. Use a newly written illustrative before line. When a public example cannot be written safely, leave the rule in the private guide. A guide-only job labels the entire voice brief private.

- `guide.html` and the source JSON are the internal master and evidence register. `partner-guide.md` is the editable partner copy and uses the public-source application, portable examples and eligible visual rules. It excludes unrestricted internal positioning, owner decisions, conflicts, source locators and excerpts. Exact fonts/colors used in the proof and the supplied logo filename are carried into the partner guide and design brief. Choose only recipient-cleared values and assets for the applied proof. When no partner-facing use is cleared, run the internal guide-only mode.

- Use optional `sheet.action_note` for what happens after the buyer acts, such as a coordinator emailing a sample. Include the supporting public source in `sheet.refs`. The note counts toward the copy budget and appears beside the action in the proof, partner guide and design brief.

### How a visual decision survives the handoff

Supply `identity_basis` for the roles `ink`, `paper`, `action`, `font_stack` and `heading_font_stack`. Each entry contains `status` (`verified`, `production choice` or `unknown`), `basis` (brief shareable rationale and scope) and `refs`. A verified role requires a cleared source and an exact `value` matching the applied setting. State scope precisely, e.g. “Specified for the intake diagram,” separate from approval for other brand work. A legacy role without evidence is labeled a proof setting with unknown provenance. Data values, source IDs and implementation checks alone cannot verify that the source supports the decision.

`design_spec` contains the current `version`, `substitution_test` (the observable result after the name is covered and a different category substituted), and `owner_rejections`. Each rejection has a recipient-cleared `instruction` and corresponding `refs`. Paraphrase limitations approved for sharing. Keep private owner quotations and confidential rationale in the internal record. When no direction is available, leave the entry absent and mark the direction pending.

For `layout: "specimen"` add `sheet.device`. Give it a cleared local PNG/JPEG `file` beside the JSON, an optional `mobile_file` with the same information recomposed for narrow screens, meaningful `alt` text, `finding` (the visible short caption), `visible_words` (transcription of labels embedded in the artwork for the word budget), `meaning` (the decision the illustration resolves), and public `refs`. Include the editable source art when permitted. The output HTML embeds the image to travel offline. Rendered legibility, distinctiveness and owner approval are independent judgments. In the absence of cleared source imagery or a defensible source-specific diagram, deliver `transcript` and identify exactly which visual would settle the missing decision.

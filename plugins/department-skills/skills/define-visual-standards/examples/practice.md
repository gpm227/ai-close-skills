# Resolve a color disagreement and document type fallbacks

## Request and input evidence

Fictional Line Press wants a web-to-slide guide. T1, released CSS `release.css`, defines body ink `#17343A`, background `#FFFFFF`, action `#18565B`, and heading stack `"Freight Text", Georgia, serif`. T2, export of an older screenshot, looks teal; there is no token value in the image. L1 licenses the heading font for the company website only. Slide 4 uses a heavier heading. No slide template, logo master, or evidence for an established spacing scale is supplied.

## Approved colors and type fallbacks

| Role | Web | Slides / action | Evidence status |
| --- | --- | --- | --- |
| Body ink on white | #17343A on #FFFFFF, about 13.2:1 | Trial the same pair on white. | Web specified by T1. Slide extension proposed. |
| Action text on white | #18565B on #FFFFFF, about 8.3:1 | Underline links as well as coloring them. | Web values specified by T1; slide treatment proposed. |
| Headline | Freight Text, Georgia, serif | Use an available, permitted Georgia or system serif. Do not embed the licensed web face in a distributed deck. | Web stack specified T1. Rights boundary L1. |
| Hierarchy | Body copy uses ink rather than action color. | Start with a 32 pt title and 20 pt body. Check the projected slide. | Web specified; sizes are proposals. Slide 4 shows relative weight only. |

A source file governs its own release. Record older screenshot color as observed only. Check actual body/link pairs and font availability at target size; use the same sRGB relative-luminance calculation after any foreground or background change. The working deck uses a temporary text identifier while the logo master is requested.

**Apply.** On desktop place the repair action adjacent to the service name; on a narrow screen stack label then action and allow the full label to wrap. On the slide retain one focal title and one legible destination. Mark these layout choices proposed. Inspect the resulting render for clipping at the actual target size.

## Boundary test

A new reseller flyer has a black photo background. The white-page contrast numbers do not carry over, and the web font license gives no print usage. Check the actual location and each approved pairing or use a proposed opaque background and the permitted print fallback pending owner approval.

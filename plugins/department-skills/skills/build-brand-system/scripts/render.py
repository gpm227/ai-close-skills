"""Render a private brand guide, voice brief, design handoff and copy proof offline."""
import argparse
import base64
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ICONS = {
    "route": "M4 7h12a4 4 0 0 1 0 8H8m3-3-3 3 3 3M4 4v6",
    "inspect": "M16 10a6 6 0 1 1-12 0 6 6 0 0 1 12 0m-2 5 6 6",
    "record": "M5 3h10l4 4v14H5zM14 3v5h5M8 12h8M8 16h6",
    "protect": "M12 2 3 6v6c0 5 5 9 9 11 4-2 9-6 9-11V6zM8 12l3 3 5-6",
    "time": "M22 12a10 10 0 1 1-20 0 10 10 0 1 1 20 0M12 6v6l4 2",
    "people": "M15 7a3 3 0 1 1-6 0 3 3 0 0 1 6 0M5 21v-3a7 7 0 0 1 14 0v3",
    "signal": "M3 20h18M6 16v-4m5 4V7m5 9V3",
    "package": "M3 7l9-5 9 5v10l-9 5-9-5zM3 7l9 5 9-5m-9 5v10",
    "payment": "M2 5h20v14H2zM2 9h20M5 15h5",
    "place": "M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0M14 10a2 2 0 1 1-4 0 2 2 0 0 1 4 0",
    "calendar": "M3 5h18v16H3zM3 10h18M7 2v6m10-6v6M7 14h3m4 0h3",
    "tools": "M20 3a6 6 0 0 0-8 8L3 20l2 2 9-9a6 6 0 0 0 7-8l-4 4-3-3z",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def string(obj, key):
    value = obj[key]
    require(isinstance(value, str) and value.strip(), f"Missing text: {key}")
    return value.strip()


def color_lightness(color):
    require(re.fullmatch(r"#[0-9a-fA-F]{6}", color), "Use six-digit hex colors")
    parts = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in parts]
    return sum(x * weight for x, weight in zip(linear, (0.2126, 0.7152, 0.0722)))


def esc(value):
    return html.escape(value, quote=True)


def tag(obj, key):
    return esc(string(obj, key))


def raster_uri(folder, filename):
    require(isinstance(filename, str) and Path(filename).name == filename, "Supply a local image filename")
    asset = folder / filename
    require(asset.is_file() and not asset.is_symlink() and asset.stat().st_size <= 5_000_000,
            "Supply a regular PNG or JPEG of at most 5 MB")
    content = asset.read_bytes()
    if content.startswith(b"\x89PNG\r\n\x1a\n"):
        mime = "image/png"
    elif content.startswith(b"\xff\xd8\xff"):
        mime = "image/jpeg"
    else:
        raise ValueError("Supply a PNG or JPEG image")
    return f"data:{mime};base64,{base64.b64encode(content).decode()}"


def render(data, folder):
    sources = {}
    for source in data["sources"]:
        key = string(source, "id")
        require(key not in sources and source["clearance"] in {"public", "internal", "unconfirmed"}, "Invalid source")
        for field in ("locator", "excerpt"):
            string(source, field)
        sources[key] = source

    def refs(item, public=False, optional=False):
        ids = item["refs"]
        require(isinstance(ids, list) and (ids or optional), "Missing evidence references")
        for key in ids:
            require(key in sources, f"Unknown source: {key}")
            require(not public or sources[key]["clearance"] == "public", f"Source lacks public clearance: {key}")
        return esc(", ".join(ids))

    company = tag(data, "company")
    sheet = data["sheet"]
    color = data.get("color", {"ink": "#000000", "paper": "#FFFFFF"})
    icon_color = esc(color.get("action", color["ink"]))

    if sheet is not None:
        refs(sheet, public=True)
        cards = sheet["cards"]
        require(2 <= len(cards) <= 4, "Use two to four icon-led buyer jobs")
        words = [string(sheet, k) for k in ("headline", "intro", "cta")]
        action_note = sheet.get("action_note", "")
        require(isinstance(action_note, str), "Use text for the optional action note")
        action_note = action_note.strip()
        words.append(action_note)
        icons, panels = set(), []
        for card in cards:
            refs(card, public=True)
            name = string(card, "icon")
            path = string(card, "svg_path") if name == "custom" else ICONS.get(name, "")
            require(re.fullmatch(r"[Mm][MmZzLlHhVvCcSsQqTtAa0-9Ee.,+\s-]+", path), "Choose a supported icon or valid path")
            require(path not in icons, "Choose a distinct icon for each job")
            icons.add(path)
            label = string(card, "label")
            detail = card.get("text", "")
            require(isinstance(detail, str), "Use text for optional card detail")
            detail = detail.strip()
            require(not detail or label.casefold().rstrip(".!?") != detail.casefold().rstrip(".!?"),
                    "Omit the supporting line when it repeats the label")
            words.extend([label, detail])
            paragraph = f"<p>{esc(detail)}</p>" if detail else ""
            panels.append(f'<article><svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="{icon_color}" stroke-width="1.7" stroke-linejoin="round" stroke-linecap="round"><path d="{esc(path)}"/></svg>'
                          f'<h2>{esc(label)}</h2>{paragraph}</article>')
        if sheet.get("device"):
            words.extend([string(sheet["device"], "finding"), string(sheet["device"], "visible_words")])
        count = len(" ".join(words).split())
        if "copy_limit" in data:
            limit = data["copy_limit"]
            require(type(limit) is int and limit > 0 and count <= limit, f"Sample uses {count} words; budget is {limit}")
    ink, paper = color["ink"], color["paper"]
    a, b = sorted(map(color_lightness, [ink, paper]))
    require((b + 0.05) / (a + 0.05) >= 4.5, "Applied body text pair falls below 4.5:1")
    require(data["status"] in {"draft", "owner-approved"}, "State the actual approval status")
    font = data.get("font_stack", "Arial, sans-serif")
    require(re.fullmatch(r"[a-zA-Z0-9 ,'\-]+", font), "Use a local font stack")
    heading_font = data.get("heading_font_stack", font)
    require(re.fullmatch(r"[a-zA-Z0-9 ,'\-]+", heading_font), "Use a local heading font stack")
    action = color.get("action", ink)
    lum_a, lum_b = sorted((color_lightness(action), color_lightness(paper)))
    require((lum_b+0.05)/(lum_a+0.05) >= 4.5, "Action text contrast falls below 4.5:1")
    layout = data.get("layout", "transcript")
    require(layout in {"specimen", "transcript", "comparison", "sequence", "index"}, "Unrecognized copy proof layout")
    css = f":root{{--ink:{ink};--paper:{paper};font-family:{font};color:var(--ink);background:var(--paper)}}"
    css += """*{box-sizing:border-box}body{max-width:58rem;margin:auto;padding:clamp(1.3rem,5vw,4rem);line-height:1.45}
    header{border-bottom:2px solid;padding-bottom:1.2rem;font-size:1.15rem;font-weight:bold}header img{max-width:14rem;max-height:4rem;object-fit:contain}
    h1{font-size:3rem;font-size:clamp(2.25rem,6.4vw,4.6rem);line-height:1.04;letter-spacing:-.045em;max-width:20ch;margin:1em 0 .3em}
    h2,h3{line-height:1.15}section{margin:2.2rem 0}article{padding:1.3rem 0;border-top:1px solid}
    .intro{font-size:1.2rem;max-width:52ch}.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,11rem),1fr));gap:1.4rem}
    svg{width:3rem;height:3rem;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linejoin:round;stroke-linecap:round}
    .cta{display:inline-block;padding:.7rem 1rem;background:var(--ink);color:var(--paper);text-decoration:underline}
    small{display:block}p,li,small{overflow-wrap:anywhere}dt{font-weight:bold;margin-top:1rem}dd{margin:.25rem 0}
    @media print{body{max-width:none;padding:.2in}article{break-inside:avoid}.cta{background:transparent;color:var(--ink)}}
    """
    css += f"h1,h2,h3{{font-family:{heading_font}}}.cta{{background:{action};color:{paper}}}svg{{color:{action}}}"
    if layout == "index":
        css += ".cards{display:block}.cards article{display:grid;grid-template-columns:4.5rem minmax(8rem,1fr) 2fr;gap:1rem;align-items:center}.cards h2,.cards p{margin:0}"
        css += "@media(max-width:34rem){.cards article{grid-template-columns:3.5rem 1fr}.cards p{grid-column:2}.cards svg{grid-row:span 2}}"
    elif layout == "sequence":
        css += ".cards{border-left:2px solid;display:block;padding-left:1.5rem}.cards article{border:0;display:grid;grid-template-columns:3.5rem 1fr;column-gap:1rem}.cards svg{grid-row:span 2}.cards h2,.cards p{margin:.2rem 0}"
    css += "@media print{.cards article{display:block;position:relative;min-height:3.7rem;padding:.55rem 0 .55rem 3.9rem}.cards article svg{position:absolute;top:.55rem;left:0}.cards h2,.cards p{margin:.18rem 0}h1{font-size:32pt;max-width:24ch}html{font-size:12pt}.cta{background:transparent;color:var(--ink);padding:0}.cta::after{content:' · ' attr(href);font-size:.8em;overflow-wrap:anywhere}}"
    wordmark = company
    if data.get("logo"):
        logo_uri = raster_uri(folder, data["logo"])
        wordmark = f'<img alt="{company}" src="{logo_uri}">'

    if layout == "specimen":
        css += """
        .specimen h1{font-size:clamp(1.65rem,3.5vw,2.6rem);letter-spacing:-.025em;margin:.65em 0 .12em;max-width:none}
        .specimen .intro{margin:.2rem 0 .8rem}.specimen figure{margin:0 0 1rem}
        .specimen figure img{display:block;width:100%;height:auto}
        .specimen figure a{color:inherit;text-decoration:none}
        .specimen .steps article{display:flex;align-items:baseline;gap:.7rem;border:0;padding:.25rem 0;flex-wrap:wrap}
        .specimen .steps svg{height:1rem;width:1rem;align-self:center;flex:none}
        .specimen .steps h2{font-size:1rem;margin:0}.specimen .steps p{margin:0}
        .specimen .cta{margin:.2rem 0 .8rem}
        @media print{.specimen h1{font-size:23pt}.specimen figure{margin:.1in 0 .12in}
        .specimen .steps article{min-height:0;position:static;display:block;padding:.04in 0}
        .specimen .steps article svg{position:static;vertical-align:middle;margin-right:.07in}
        .specimen .steps h2,.specimen .steps p{display:inline;margin-right:.08in}
        .specimen .cta{margin-top:.08in}}
        """
    elif layout == "transcript":
        css += """
        header{font-size:1rem;border:0;padding:0}h1{font:inherit;font-weight:bold;letter-spacing:normal;margin:1em 0}
        .intro{font-size:inherit}.cards{display:block}.cards article{border:0;min-height:0;padding:.2rem 0}
        .cards svg{display:none}.cards h2,.cards p{font-size:inherit;margin:.2rem 0}
        """

    def page(title, body):
        return (f'<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
                f'<title>{title} | {company}</title><style>{css}</style><body><header>{wordmark}</header><main>{body}</main></body></html>')

    if sheet is not None:
        url = sheet["destination"]
        require(isinstance(url, str) and (not url or (urlsplit(url).scheme == "https" and urlsplit(url).hostname)), "Invalid CTA destination")
        require(url or data["status"] == "draft", "An unresolved destination requires draft status")
        cta = f'<a class="cta" href="{esc(url)}">{tag(sheet,"cta")}</a>' if url else f'<p>{tag(sheet,"cta")}</p>'
        if action_note:
            cta += f'<p>{esc(action_note)}</p>'
        device = sheet.get("device")
        if layout == "specimen":
            require(isinstance(device, dict), "A specimen requires the actual cleared visual device")
            refs(device, public=True)
            filename = string(device, "file")
            image_uri = raster_uri(folder, filename)
            alt = tag(device, "alt")
            string(device, "meaning")
            finding = tag(device, "finding")
            artwork = f'<img src="{image_uri}" alt="{alt}">'
            if device.get("mobile_file"):
                mobile_uri = raster_uri(folder, string(device, "mobile_file"))
                artwork = f'<picture><source media="screen and (max-width: 40rem)" srcset="{mobile_uri}">{artwork}</picture>'
            figure = f'<figure>{artwork}<figcaption>{finding}</figcaption></figure>'
            content = (f'<div class="specimen"><h1>{tag(sheet,"headline")}</h1><p class="intro">{tag(sheet,"intro")}</p>'
                       f'{cta}{figure}<div class="steps">{"".join(panels)}</div></div>')
        else:
            require(device is None, "Choose specimen layout to render the supplied visual device")
            content = (f'<h1>{tag(sheet,"headline")}</h1><p class="intro">{tag(sheet,"intro")}</p>'
                       f'<section class="cards">{"".join(panels)}</section>{cta}')
        sample = page("One-sheet copy proof", content)
    guide = [f'<h1>Internal brand guide</h1><p>Private working file. Includes source excerpts and owner decisions.</p><p>{tag(data,"positioning")}</p><p><b>Audience</b> · {tag(data,"audience")}</p>'
             f'<p><b>{tag(data,"status")}</b> · {tag(data,"decision")}</p><section><h2>Writing in our voice</h2>']
    private_only = sheet is None
    if private_only:
        brief = [f"# Private voice brief · {string(data,'company')}",
                 "Internal working examples. Keep this brief with the private guide."]
    else:
        brief = [f"# Portable voice brief · {string(data,'company')}", "Approval: " + data["status"],
                 "Approved-source copy for this job: " + string(sheet, "headline")]
    require(len(data["voice"]) >= 2 and data["visual"], "Include voice and visual rules")
    for rule in data["voice"]:
        guide.append(f'<article><h3>{tag(rule,"rule")}</h3><p>Before · {tag(rule,"before")}</p><p>After · {tag(rule,"after")}</p><small>{refs(rule)}</small></article>')
        portable = rule.get("portable")
        if portable is not None:
            refs(portable, public=True)
            for field in ("rule", "before", "after"):
                string(portable, field)
        if private_only or all(sources[key]["clearance"] == "public" for key in rule["refs"]):
            example = rule
        else:
            example = portable
        if example is not None:
            brief.extend([string(example,"rule"), "Before: " + string(example,"before"),
                          "After: " + string(example,"after")])
    if not private_only and len(brief) == 3:
        brief.append("No reusable public-source voice examples were supplied. Request one cleared writing sample.")
    guide.append('</section><section><h2>Visual system</h2><ul>')
    for rule in data["visual"]:
        require(rule["status"] in {"observed","proposed"}, "Label visual decisions")
        guide.append(f'<li><b>{tag(rule,"status")}</b> · {tag(rule,"rule")} <small>{refs(rule, optional=rule["status"]=="proposed")}</small></li>')
    guide.append('</ul></section><section><h2>Source register</h2><dl>')
    for key, src in sources.items():
        guide.append(f'<dt>{esc(key)} · {tag(src,"clearance")}</dt><dd>{tag(src,"locator")} — {tag(src,"excerpt")}</dd>')
    guide.append("</dl></section>")
    if "inputs" in data:
        inputs = data["inputs"]
        require(set(inputs) == {"deck", "website"}, "Account for both the deck and website")
        guide.append("<section><h2>Materials inspected</h2><dl>")
        for kind, item in inputs.items():
            state = item["state"]
            require(state in {"inspected", "snapshot", "unavailable"}, "Unknown input state")
            require(state != "unavailable" or item["refs"] == [], "An unavailable input cannot supply evidence")
            guide.append(f"<dt>{esc(kind)} · {esc(state)}</dt><dd>{tag(item, 'detail')} "
                         f"<small>{refs(item, optional=state == 'unavailable')}</small></dd>")
        require(any(item["state"] != "unavailable" for item in inputs.values()), "Supply an inspectable source")
        guide.append("</dl></section>")
    conflicts = data.get("conflicts", [])
    if conflicts:
        guide.append("<section><h2>Conflicting evidence</h2><ul>")
        for conflict in conflicts:
            state = conflict["state"]
            require(state in {"resolved", "open"}, "Give each conflict a disposition")
            require(state != "open" or data["status"] == "draft", "Resolve open conflicts before approval")
            evidence = refs(conflict)
            require(len(set(conflict["refs"])) >= 2, "Cite both sides of a conflict")
            guide.append(f"<li><b>{esc(state)}</b> · {tag(conflict,'issue')} — {tag(conflict,'decision')} "
                         f"<small>{evidence}</small></li>")
        guide.append("</ul></section>")

    if sheet is None:
        require(data["status"] == "draft", "A guide-only result requires draft status")
        guide.append("<p>Guide only. No buyer-facing copy or design handoff has been produced.</p>")
        return {"guide.html": page("Brand guide", "".join(guide)),
                "voice-brief.md": "\n\n".join(brief) + "\n"}

    guide.append('<section><h2>One-sheet evidence</h2><ul>')
    for label, item in [(sheet["headline"],sheet)]+[(c["label"],c) for c in cards]:
        guide.append(f'<li>{esc(label)} · {refs(item,public=True)}</li>')
    if action_note:
        guide.append(f'<li>{esc(action_note)} · {refs(sheet, public=True)}</li>')
    if device:
        guide.append(f'<li>{tag(device,"finding")} · {refs(device, public=True)}</li>')
    guide.append(f'</ul><p>{count} words · {len(cards)} distinct icons</p></section>')
    production = data.get("production")
    design = [f"# Design brief · {string(data, 'company')}", "Working copy proof. Design export and visual review pending.",
              "## Audience", string(data, "audience"), "## Buyer promise", string(sheet, "headline")]
    if production is None:
        design.append("Confirm the intended composition, buyer relationship, authorized assets and visual benchmark before commissioning design.")
    else:
        for key, heading in (("direction", "Composition and reading order"), ("relationship", "What the visual explains"),
                             ("assets", "Assets and permissions"), ("acceptance", "Visual acceptance criteria")):
            design.extend(["## " + heading, string(production, key)])
    roles = {"ink": ("Body text", ink), "paper": ("Page", paper), "action": ("Action and icon ink", action),
             "font_stack": ("Body font stack", font), "heading_font_stack": ("Heading font stack", heading_font)}
    basis = data.get("identity_basis", {})
    require(isinstance(basis, dict) and not set(basis).difference(roles), "Use known identity roles")
    identity = ["## Applied values and their provenance"]
    for key, (label, value) in roles.items():
        item = basis.get(key)
        if item is None:
            identity.append(f"- {label}: {value} — provenance unknown; proof setting only.")
            continue
        state = item["status"]
        require(state in {"verified", "production choice", "unknown"}, "Label each identity basis")
        evidence = refs(item, public=True, optional=state != "verified")
        reason = string(item, "basis")
        require(state != "verified" or item.get("value") == value, f"Verified {key} must match the cited value")
        identity.append(f"- {label}: {value} — {state}. {reason}" + (f" [{evidence}]" if evidence else ""))
    identity.append(f"Use the approved logo file {data['logo']} at its original proportions." if data.get("logo")
                    else "Use the company name as a temporary wordmark. No logo file was supplied.")
    spec = data.get("design_spec")
    if spec is not None:
        identity.extend(["## Visual review standard · " + string(spec, "version"), string(spec, "substitution_test")])
        for item in spec.get("owner_rejections", []):
            refs(item, public=True)
            identity.append("- Owner rejected: " + string(item,"instruction"))
    else:
        identity.append("Specific design benchmark and owner rejections are unrecorded. Treat visual direction as pending.")
    if device:
        identity.extend(["## Visual device", string(device,"file"), string(device,"meaning"), string(device,"finding")])
    else:
        identity.append("No source-specific visual device was supplied. This copy proof cannot establish visual distinctiveness.")
    for rule in data["visual"]:
        if all(sources[key]["clearance"] == "public" for key in rule["refs"]):
            identity.append(f"- {rule['status'].capitalize()}: {string(rule, 'rule')}")
    guide.append("<section><h2>Applied proof and design review</h2><ul>")
    guide.extend(f"<li>{esc(line)}</li>" for line in identity if not line.startswith("## "))
    guide.append("</ul></section>")
    design.extend(identity)
    partner = [f"# Brand guide · {string(data,'company')}",
               f"Working status: {data['status']}.",
               "## Buyer-facing example", string(sheet,"headline"), string(sheet,"intro"),
               *identity, "## Writing rules and examples", *brief[3:]]
    next_action = ["## Next action", string(sheet, "cta"), url or "Destination pending"]
    if action_note:
        next_action.append(action_note)
    partner.extend(next_action)
    design.extend(["## Working copy", string(sheet, "intro")])
    for card in cards:
        detail = card.get("text", "").strip()
        label = string(card, "label")
        design.append(f"- {label} — {detail}" if detail else f"- {label}")
    design.extend(["## Icon assignments",
                   "\n".join(f"- {string(card,'label')}: {string(card,'icon')}" +
                             (f" — 24 × 24 path: {string(card,'svg_path')}" if card["icon"] == "custom" else "")
                             for card in cards)])
    design.extend([*next_action,
                   "## Deliver and review", "Return the editable design and a rendered export. Review the first composition against the owner's benchmark. Revise it and inspect the second export for buyer meaning, brand fidelity and production details. Keep both reviews and identify anything awaiting approval."])
    return {"guide.html":page("Brand guide","".join(guide)), "one-sheet.html":sample, "design-brief.md":"\n\n".join(design)+"\n",
            "voice-brief.md":"\n\n".join(brief)+"\n", "partner-guide.md":"\n\n".join(partner)+"\n"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("brand", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        result = render(json.loads(args.brand.read_text()), args.brand.parent)
        args.output.mkdir(parents=True, exist_ok=False)
        for name, content in result.items():
            (args.output/name).write_text(content, encoding="utf-8")
    except (ValueError, KeyError, TypeError, OSError) as error:
        parser.exit(1, f"Brand system: {error}\n")

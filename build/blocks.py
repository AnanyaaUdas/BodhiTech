# -*- coding: utf-8 -*-
"""the page sections, as functions. each returns a chunk of html.

they reuse the same markup the home page uses, so the styling and the scroll
animations work with no extra effort. check for an existing one before adding
a new section.
"""

import re

from content import (SITE, PILLARS, INDUSTRY_PILLARS, TESTIMONIALS,
                     TRUST_LOGOS, CASES, SOLUTIONS, INDUSTRIES, BLOG_POSTS)

ARROW = ('<svg width="15" height="15" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">'
         '<path d="M3.125 10H16.875M11.25 4.375L16.875 10L11.25 15.625" stroke="currentColor" '
         'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>')

import os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_TESTIMONIALS_PARTIAL = open(
    _os.path.join(_ROOT, "partials", "testimonials.html"), encoding="utf-8").read()

ARROW22 = ARROW.replace('stroke-width="2"', 'stroke-width="2.2"').replace('width="15" height="15"', 'width="14" height="14"')

# the icons. 28 line drawings, one stroke weight, brand colour, no fills.
# they take their colour from whatever container they land in, so nothing
# needs passing in. no emoji anywhere on the site.
# (emoji() is a leftover name from what this used to return.)

def _s(body, w="1.7"):
    """wraps icon path data in the standard 24x24 svg.

    every icon goes through this, so they all get the same stroke weight.
    stroke="currentColor" is what lets them pick up the container's colour.
    """
    return ('<svg width="24" height="24" viewBox="0 0 24 24" fill="none" '
            'stroke="currentColor" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>' % (w, body))

ICON_SET = {
 "globe": _s('<circle cx="12" cy="12" r="8.8"/><path d="M3.2 12h17.6"/>'
             '<path d="M12 3.2c2.3 2.4 3.5 5.4 3.5 8.8s-1.2 6.4-3.5 8.8c-2.3-2.4-3.5-5.4-3.5-8.8S9.7 5.6 12 3.2z"/>'),
 "target": _s('<circle cx="12" cy="12" r="8.8"/><circle cx="12" cy="12" r="4.6"/>'
              '<circle cx="12" cy="12" r="1.1" fill="currentColor" stroke="none"/>'),
 "palette": _s('<path d="M12 3.2a8.8 8.8 0 0 0 0 17.6c1 0 1.7-.8 1.7-1.7 0-.5-.2-.9-.5-1.2a1.7 1.7 0 0 1 1.2-2.9h2a4.4 4.4 0 0 0 4.4-4.4c0-4-3.9-7.4-8.8-7.4z"/>'
               '<circle cx="8" cy="10" r="1" fill="currentColor" stroke="none"/>'
               '<circle cx="11.5" cy="7.2" r="1" fill="currentColor" stroke="none"/>'
               '<circle cx="15.5" cy="8.6" r="1" fill="currentColor" stroke="none"/>'),
 "people": _s('<circle cx="9" cy="8" r="3.4"/><path d="M2.8 20c0-3.4 2.8-6 6.2-6s6.2 2.6 6.2 6"/>'
              '<path d="M17 5.6a3 3 0 0 1 0 5.6"/><path d="M18.6 20c0-2-.6-3.6-1.7-4.8"/>'),
 "chart": _s('<path d="M3 20.2h18"/><path d="M6 17V11"/><path d="M11 17V6.5"/><path d="M16 17v-4"/>'
             '<path d="M20 17V8.5"/>'),
 "mobile": _s('<rect x="7" y="2.6" width="10" height="18.8" rx="2.4"/><path d="M10.6 5.6h2.8"/>'
              '<circle cx="12" cy="18" r="1" fill="currentColor" stroke="none"/>'),
 "rocket": _s('<path d="M12 2.6c2.8 2.4 4.3 5.6 4.3 8.6 0 1.6-.5 3-1.4 4.2H9.1a6.9 6.9 0 0 1-1.4-4.2c0-3 1.5-6.2 4.3-8.6z"/>'
              '<circle cx="12" cy="9.6" r="2"/><path d="M9.1 15.4 6 18.6l3.3-.5"/>'
              '<path d="M14.9 15.4 18 18.6l-3.3-.5"/><path d="M12 18.4v3"/>'),
 "building": _s('<path d="M4 20.4V5.2a1.4 1.4 0 0 1 1.4-1.4h7.2A1.4 1.4 0 0 1 14 5.2v15.2"/>'
                '<path d="M14 9.6h4.6A1.4 1.4 0 0 1 20 11v9.4"/><path d="M2.8 20.4h18.4"/>'
                '<path d="M7 7.6h1.4M11 7.6h1.4M7 11.4h1.4M11 11.4h1.4M7 15.2h1.4M11 15.2h1.4M17 13.4h.8M17 16.8h.8"/>'),
 "gear": _s('<circle cx="12" cy="12" r="3.1"/>'
            '<path d="M19.5 14.6a1.6 1.6 0 0 0 .3 1.8l.1.1a1.9 1.9 0 1 1-2.7 2.7l-.1-.1a1.6 1.6 0 0 0-1.8-.3 1.6 1.6 0 0 0-1 1.5v.3a1.9 1.9 0 1 1-3.8 0v-.2a1.6 1.6 0 0 0-1-1.5 1.6 1.6 0 0 0-1.8.3l-.1.1a1.9 1.9 0 1 1-2.7-2.7l.1-.1a1.6 1.6 0 0 0 .3-1.8 1.6 1.6 0 0 0-1.5-1h-.3a1.9 1.9 0 1 1 0-3.8h.2a1.6 1.6 0 0 0 1.5-1 1.6 1.6 0 0 0-.3-1.8l-.1-.1a1.9 1.9 0 1 1 2.7-2.7l.1.1a1.6 1.6 0 0 0 1.8.3h.1a1.6 1.6 0 0 0 1-1.5v-.3a1.9 1.9 0 1 1 3.8 0v.2a1.6 1.6 0 0 0 1 1.5 1.6 1.6 0 0 0 1.8-.3l.1-.1a1.9 1.9 0 1 1 2.7 2.7l-.1.1a1.6 1.6 0 0 0-.3 1.8v.1a1.6 1.6 0 0 0 1.5 1h.3a1.9 1.9 0 1 1 0 3.8h-.2a1.6 1.6 0 0 0-1.5 1z"/>'),
 "chat": _s('<path d="M20.8 11.6a8.2 8.2 0 0 1-8.8 8.2L4 21l1.2-3.4a8.2 8.2 0 1 1 15.6-6z"/>'
            '<path d="M8.6 10.8h6.8M8.6 14h4"/>'),
 "mail": _s('<rect x="2.8" y="5" width="18.4" height="14" rx="2.2"/><path d="m3.4 7.4 8.6 6 8.6-6"/>'),
 "shield": _s('<path d="M12 3.2 19.8 6.5v5.2c0 4.3-3.2 8-7.8 9.1-4.6-1.1-7.8-4.8-7.8-9.1V6.5z"/>'
              '<path d="m9.1 12 2.2 2.2 3.9-4.2"/>'),
 "cart": _s('<circle cx="9.6" cy="19.4" r="1.5"/><circle cx="17.6" cy="19.4" r="1.5"/>'
            '<path d="M2.6 3.6h2.6l2.4 11.2h11l2-7.6H6.6"/>'),
 "tools": _s('<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.8-3.8a6 6 0 0 1-7.9 7.9l-6.9 6.9a2.1 2.1 0 0 1-3-3l6.9-6.9a6 6 0 0 1 7.9-7.9z"/>'),
 "search": _s('<circle cx="10.8" cy="10.8" r="7"/><path d="m16 16 5 5"/>'),
 "megaphone": _s('<path d="M3.4 10.2v3.6a1.6 1.6 0 0 0 1.6 1.6h2.2l7.4 4.4V4.2L7.2 8.6H5a1.6 1.6 0 0 0-1.6 1.6z"/>'
                 '<path d="M18.4 8.8a4.4 4.4 0 0 1 0 6.4"/><path d="M7.2 15.4v4.4"/>'),
 "magnet": _s('<path d="M4.6 20.4V11a7.4 7.4 0 0 1 14.8 0v9.4h-4.6V11a2.8 2.8 0 0 0-5.6 0v9.4z"/>'
              '<path d="M4.6 16.2h4.6M14.8 16.2h4.6"/>'),
 "flask": _s('<path d="M9.4 3.4v5.9L4.2 18a2 2 0 0 0 1.7 3h12.2a2 2 0 0 0 1.7-3l-5.2-8.7V3.4"/>'
             '<path d="M8.2 3.4h7.6"/><path d="M6.6 14.6h10.8"/>'),
 "puzzle": _s('<path d="M11 3.4a2 2 0 0 1 2 2v.7h2.6a1 1 0 0 1 1 1V10h.7a2 2 0 1 1 0 4h-.7v3.6a1 1 0 0 1-1 1H13v-.7a2 2 0 1 0-4 0v.7H6.4a1 1 0 0 1-1-1V14h-.8a2 2 0 1 1 0-4h.8V7.1a1 1 0 0 1 1-1H9v-.7a2 2 0 0 1 2-2z"/>'),
 "folder": _s('<path d="M3 6.6a1.8 1.8 0 0 1 1.8-1.8h4l2 2.6h7.4A1.8 1.8 0 0 1 21 9.2v8.2a1.8 1.8 0 0 1-1.8 1.8H4.8A1.8 1.8 0 0 1 3 17.4z"/>'
             '<path d="M3 10.6h18"/>'),
 "database": _s('<ellipse cx="12" cy="5.8" rx="7.6" ry="3.2"/>'
                '<path d="M4.4 5.8v12.4c0 1.8 3.4 3.2 7.6 3.2s7.6-1.4 7.6-3.2V5.8"/>'
                '<path d="M4.4 12c0 1.8 3.4 3.2 7.6 3.2s7.6-1.4 7.6-3.2"/>'),
 "handshake": _s('<circle cx="9.2" cy="12" r="5.6"/><circle cx="14.8" cy="12" r="5.6"/>'),
 "leaf": _s('<path d="M12 3c3.2 2.8 4.9 5.8 4.9 8.8A4.9 4.9 0 0 1 12 16.6a4.9 4.9 0 0 1-4.9-4.8C7.1 8.8 8.8 5.8 12 3z"/>'
            '<path d="M12 16.6V21"/><path d="M12 19.4c-1.6-1.5-3.3-2-5-1.7"/>'),
 "check": _s('<circle cx="12" cy="12" r="8.8"/><path d="m8.4 12.2 2.5 2.5 4.7-5.2"/>'),
 "pin": _s('<path d="M19 10.4c0 5-7 11-7 11s-7-6-7-11a7 7 0 1 1 14 0z"/><circle cx="12" cy="10.2" r="2.6"/>'),
 "phone": _s('<path d="M21 16.9v2.6a1.8 1.8 0 0 1-2 1.8 17.6 17.6 0 0 1-7.7-2.7 17.3 17.3 0 0 1-5.3-5.3A17.6 17.6 0 0 1 3.3 5.5a1.8 1.8 0 0 1 1.8-2h2.6a1.8 1.8 0 0 1 1.8 1.5c.1.9.3 1.7.6 2.5a1.8 1.8 0 0 1-.4 1.9l-1.1 1.1a14 14 0 0 0 5.3 5.3l1.1-1.1a1.8 1.8 0 0 1 1.9-.4c.8.3 1.6.5 2.5.6A1.8 1.8 0 0 1 21 16.9z"/>'),
 "clock": _s('<circle cx="12" cy="12" r="8.8"/><path d="M12 6.8V12l3.4 2"/>'),
 "sparkle": _s('<path d="M12 3.2 13.8 9 19.6 10.8 13.8 12.6 12 18.4 10.2 12.6 4.4 10.8 10.2 9z"/>'
               '<path d="M18.6 16.4 19.4 18.8 21.8 19.6 19.4 20.4 18.6 22.8 17.8 20.4 15.4 19.6 17.8 18.8z"/>'),
}


# icons come from the card's own subject, never its position in the grid -
# position-based icons look arbitrary the moment someone reorders a list.
# ordered most specific first, so "Website Maintenance" hits maintenance rather
# than the generic website rule further down. order matters here; do not sort.
ICON_KEYWORDS = [
    (("ecommerce", "e-commerce", "retail", "shop"), "cart"),
    (("maintenance", "post-launch", "onboarding", "support"), "tools"),
    (("seo", "search engine optimi", "search rank"), "search"),
    (("digital marketing", "ppc", "google ads", "paid social", "campaign"), "megaphone"),
    (("email",), "mail"),
    (("talent sourcing", "acquisition of skilled"), "search"),
    (("lead gen", "lead capture"), "magnet"),
    (("social media", "organic social", "community"), "chat"),
    (("research", "discovery", "market research", "empathise", "understanding"), "flask"),
    (("goal", "strategic plan", "strategy", "planning", "consultation"), "target"),
    (("data", "optimis", "analytics", "monitoring"), "chart"),
    (("design", "ux/ui", "graphic", "prototype", "ideate", "aesthetic"), "palette"),
    (("workshop", "sprint", "facilitation"), "puzzle"),
    (("talent", "staff", "screening", "placement", "recruit", "team"), "people"),
    (("project management", "oversight"), "folder"),
    (("mobile", "app", "native", "cross-platform"), "mobile"),
    (("backend", "server", "api", "database"), "database"),
    (("security", "compliance"), "shield"),
    (("mvp", "minimum viable", "launch", "rapid"), "rocket"),
    (("construction", "template"), "building"),
    (("business consult", "advisor", "partner"), "handshake"),
    (("heritage", "distinctive", "youthful", "collaboration"), "leaf"),
    (("innovation", "catalyst", "creative", "idea"), "sparkle"),
    (("budget", "cost", "affordable", "value", "pricing"), "chart"),
    (("speed", "fast", "efficien", "turnaround", "timeline"), "clock"),
    (("transparen", "honest", "trust"), "shield"),
    (("testing", "quality", "qa"), "check"),
    (("integration", "deployment"), "gear"),
    (("wordpress", "bespoke", "custom build", "website", "web develop"), "globe"),
]

# when a label matches nothing, rotate through these rather than repeating
# one generic mark down the whole page.
ICON_CYCLE = ["globe", "target", "palette", "people", "chart", "mobile",
              "rocket", "building", "gear", "chat", "mail", "shield"]


def icon(name_or_index):
    """Accepts an icon name or an index into the fallback rotation."""
    if isinstance(name_or_index, int):
        return ICON_SET[ICON_CYCLE[name_or_index % len(ICON_CYCLE)]]
    return ICON_SET.get(name_or_index, ICON_SET["leaf"])


def emoji(i, label=None):
    """kept under its old name so call sites need no change, but it now
    returns a line-art SVG rather than a pictograph. matching is on word
    boundaries, so "Workshops" does not match "shop"."""
    if label:
        low = label.lower()
        for keys, name in ICON_KEYWORDS:
            for k in keys:
                if re.search(r"\b" + re.escape(k), low):
                    return ICON_SET[name]
    return icon(i)


# technology logos, all pulled from Bodhi tech's own WordPress media library -
# the same files the live case study pages use. keys are lowercased names.
#
# worth flagging before launch: these are hot-linked to bodhitech.com.au rather
# than served locally.
TECH_LOGOS = {
    "figma":        "https://bodhitech.com.au/wp-content/uploads/2024/03/figma.png",
    "wordpress":    "https://bodhitech.com.au/wp-content/uploads/2024/02/Wordpress-1.webp",
    "php":          "https://bodhitech.com.au/wp-content/uploads/2024/03/php.png",
    "mysql":        "https://bodhitech.com.au/wp-content/uploads/2023/12/Mysql_logo.png",
    "html":         "https://bodhitech.com.au/wp-content/uploads/2024/03/HTML.png",
    "css":          "https://bodhitech.com.au/wp-content/uploads/2024/03/CSS.png",
    "jquery":       "https://bodhitech.com.au/wp-content/uploads/2024/03/JQuery.png",
    "bootstrap":    "https://bodhitech.com.au/wp-content/uploads/2024/03/Bootstrap.png",
    "flutter":      "https://bodhitech.com.au/wp-content/uploads/2024/02/Flutter-1.webp",
    "laravel":      "https://bodhitech.com.au/wp-content/uploads/2024/03/laravel-1.png",
    "sembast":      "https://bodhitech.com.au/wp-content/uploads/2024/03/Group-266.png",
    "postgresql":   "https://bodhitech.com.au/wp-content/uploads/2024/03/PostgreSQL.png",
    "amazon aws":   "https://bodhitech.com.au/wp-content/uploads/2024/03/Amazon-AWS.png",
    "vue.js":       "https://bodhitech.com.au/wp-content/uploads/2024/03/Vue-Js.png",
    "ubuntu":       "https://bodhitech.com.au/wp-content/uploads/2024/03/Ubuntu-20.04.png",
    "google cloud": "https://bodhitech.com.au/wp-content/uploads/2023/12/googlecloud.png",
}


def tech_badges(items):
    """the home page's .tech-badge-card, laid out as a simple responsive grid.

    A technology with no logo in the library still gets a card, so the row
    stays visually consistent rather than mixing logos with bare text pills.
    """
    cards = ""
    for name in items:
        src = TECH_LOGOS.get(name.lower())
        img = ('<img src="%s" alt="%s logo" loading="lazy">' % (src, name)) if src else ""
        cards += '                <div class="tech-badge-card">%s<span>%s</span></div>\n' % (img, name)
    return cards


def trim(text, limit=210):
    """Cut to the last sentence end, or failing that the last whole word."""
    if len(text) <= limit:
        return text
    window = text[:limit]
    for stop in (". ", "! ", "? "):
        cut = window.rfind(stop)
        if cut > limit * 0.55:
            return window[:cut + 1]
    cut = window.rfind(" ")
    return window[:cut if cut > 0 else limit].rstrip(" ,;:") + "..."


# the page shells.

def breadcrumb(trail):
    """trail: list of (label, href). the last item passes href=none.

    that none is what marks the current page, which then renders as a span
    rather than a link - a breadcrumb whose last crumb links to the page you
    are already on is a small lie.
    """
    parts = []
    for i, (label, href) in enumerate(trail):
        if i:
            parts.append('<span class="sep">/</span>')
        parts.append('<a href="%s">%s</a>' % (href, label) if href
                     else '<span class="current">%s</span>' % label)
    return '<nav class="breadcrumb" aria-label="Breadcrumb">%s</nav>' % "".join(parts)


def page_hero(tag, title, lead, trail, meta=None, actions=None, variant="light",
              image=None, chip=None, bg=None, brand=None, results=None,
              article=None, mosaic=None):
    """one hero shell with a variant per section.

    variant   split | light | photo | case | article | minimal | showcase
    image     (src, alt) for the leaf frame on a split hero
    chip      (glyph, value, label) floating card on a split hero
    bg        (src, alt) full-bleed background for a photo hero
    brand     (logo_src, label) client mark for a case masthead
    results   [(value, label)] rendered inside a case masthead
    article   dict(category, date, read, image) for an article masthead
    mosaic    [(thumb, name, stat, href)] client tiles for a showcase hero
    """
    crumbs = breadcrumb(trail)

    meta_html = ""
    if meta:
        items = "".join(
            '<div class="phm-item"><strong>%s</strong><span>%s</span></div>' % (v, l)
            for v, l in meta)
        meta_html = '\n                    <div class="page-hero-meta">%s</div>' % items

    act_html = ""
    if actions is None:
        actions = [("Book a Free Consultation", "contact-us.html", "btn-primary"),
                   ("View Our Work", "client-stories.html", "btn-outline")]
    if actions:
        act_html = '\n                    <div class="page-hero-actions">%s</div>' % "".join(
            '<a href="%s" class="btn %s">%s</a>' % (h, c, t) for t, h, c in actions)

    tag_html = '<div class="section-tag">%s</div>' % tag if tag else ""

    # variant: split
    if variant == "split":
        visual = ""
        if image:
            chip_html = ""
            if chip:
                chip_html = """
                        <div class="hero-chip">
                            <div class="hc-mark">%s</div>
                            <div>
                                <strong>%s</strong>
                                <span>%s</span>
                            </div>
                        </div>""" % chip
            visual = """
                <div class="hero-visual">
                    <div class="hero-leaf-img">
                        <img src="%s" alt="%s" loading="lazy">
                    </div>%s
                </div>""" % (image[0], image[1], chip_html)

        return """    <!-- hero, dark -->
    <section class="page-hero hero-split">
        <div class="container">
            <div class="hero-split-grid">
                <div class="page-hero-inner">
                    %s
                    %s
                    <h1 class="page-title">%s</h1>
                    <p class="page-hero-lead">%s</p>%s%s
                </div>%s
            </div>
        </div>
    </section>
""" % (crumbs, tag_html, title, lead, act_html, meta_html, visual)

    # variant: photo
    if variant == "photo":
        bg_html = ""
        if bg:
            bg_html = '\n        <div class="hero-bg"><img src="%s" alt="%s"></div>' % bg
        return """    <!-- hero, photo -->
    <section class="page-hero hero-photo">%s
        <div class="container">
            <div class="page-hero-inner">
                %s
                %s
                <h1 class="page-title">%s</h1>
                <p class="page-hero-lead">%s</p>%s%s
            </div>
        </div>
    </section>
""" % (bg_html, crumbs, tag_html, title, lead, act_html, meta_html)

    # variant: case
    if variant == "case":
        brand_html = ""
        if brand:
            brand_html = """
                <div class="hero-case-brand">
                    <img src="%s" alt="%s logo">
                    <span>%s</span>
                </div>""" % (brand[0], brand[1], brand[1])

        res_html = ""
        if results:
            res_html = '\n            <div class="hero-case-results">%s</div>' % "".join(
                '<div class="hcr"><strong>%s</strong><span>%s</span></div>' % (v, l)
                for v, l in results)

        return """    <!-- hero, case study -->
    <section class="page-hero hero-case">
        <div class="container">
            <div class="page-hero-inner">
                %s%s
                <h1 class="page-title">%s</h1>
                <p class="page-hero-lead">%s</p>%s
            </div>%s
        </div>
    </section>
""" % (crumbs, brand_html, title, lead, act_html, res_html)

    # variant: article
    if variant == "article":
        a = article or {}
        meta_row = """
                <div class="article-meta-row">
                    <span class="article-chip">%s</span>
                    <span class="dot">&bull;</span>
                    <time>%s</time>
                    <span class="dot">&bull;</span>
                    <span class="read">%s</span>
                </div>""" % (a.get("category", ""), a.get("date", ""), a.get("read", ""))

        cover = ""
        if a.get("image"):
            cover = """
            <div class="article-cover">
                <img src="%s" alt="%s" loading="lazy">
            </div>""" % (a["image"], a.get("alt", ""))

        return """    <!-- hero, article -->
    <section class="page-hero hero-article">
        <div class="container">
            <div class="page-hero-inner">
                %s%s
                <h1 class="page-title">%s</h1>
                <p class="page-hero-lead">%s</p>%s
            </div>%s
        </div>
    </section>
""" % (crumbs, meta_row, title, lead, act_html, cover)

    # variant: showcase
    if variant == "showcase":
        tiles = "".join("""
                    <a class="mosaic-tile" href="%s">
                        <img src="%s" alt="%s case study" loading="lazy">
                        <div class="mt-label">
                            <strong>%s</strong>
                            <span>%s</span>
                        </div>
                    </a>""" % (href, thumb, name, name, stat)
            for thumb, name, stat, href in (mosaic or []))

        return """    <!-- hero, mosaic -->
    <section class="page-hero hero-showcase">
        <div class="container">
            <div class="hero-showcase-grid">
                <div class="page-hero-inner">
                    %s
                    %s
                    <h1 class="page-title">%s</h1>
                    <p class="page-hero-lead">%s</p>%s%s
                </div>
                <div class="hero-mosaic">%s</div>
            </div>
        </div>
    </section>
""" % (crumbs, tag_html, title, lead, act_html, meta_html, tiles)

    # variant: minimal
    if variant == "minimal":
        return """    <!-- hero, plain -->
    <section class="page-hero hero-minimal">
        <div class="container">
            <div class="page-hero-inner">
                %s
                %s
                <h1 class="page-title">%s</h1>
                <p class="page-hero-lead">%s</p>%s%s
            </div>
        </div>
    </section>
""" % (crumbs, tag_html, title, lead, act_html, meta_html)

    # variant: light
    return """    <!-- hero, light -->
    <section class="page-hero hero-light">
        <div class="container">
            <div class="page-hero-inner">
                %s
                %s
                <h1 class="page-title">%s</h1>
                <p class="page-hero-lead">%s</p>%s%s
            </div>
        </div>
    </section>
""" % (crumbs, tag_html, title, lead, act_html, meta_html)


def section_head(tag, title, desc="", left=False):
    """the kicker, heading and description that opens a section.

    the .section-title class matters: js/site.js finds it by that name and
    gives it the word-by-word reveal. emit a plain h2 here and the heading
    silently stops animating.
    """
    return """            <div class="section-header%s">
                <div class="section-tag">%s</div>
                <h2 class="section-title">%s</h2>
                %s
            </div>
""" % (" left" if left else "", tag, title, ('<p class="section-desc">%s</p>' % desc) if desc else "")


def trust_strip():
    """the static logo strip. the home page marquee scrolls; this one does
    not, because on a subpage it sits near other moving things.
    """
    logos = "".join(
        '<div class="partner-item"><img src="%s" alt="%s" loading="lazy"></div>' % (s, a)
        for s, a in TRUST_LOGOS)
    return """    <!-- logo strip -->
    <section class="trust-strip">
        <div class="container">
            <h4>Trusted by Australia's fastest growing SMEs &amp; startups</h4>
        </div>
        <div class="marquee-container">
            <div class="marquee-track">%s%s</div>
        </div>
    </section>
""" % (logos, logos)


# the content sections, all built from home-page components.

def bento_section(tag, title, desc, cards, soft=False, cols="", start=0, links=None):
    """cards: list of (title, description). Uses .service-bento-card verbatim."""
    items = ""
    for i, (t, d) in enumerate(cards):
        link = links[i] if links else None
        foot = ""
        if link:
            foot = """            <div class="service-card-footer">
                    <a href="%s" class="service-card-link">
                        <span>%s</span>
                        %s
                    </a>
                    <div class="service-card-arrow">↗</div>
                </div>""" % (link[1], link[0], ARROW22)
        items += """                <div class="service-bento-card">
                    <div>
                        <div class="service-card-top-bar">
                            <span class="service-card-index"><i>%02d</i>%s</span>
                            <div class="service-card-icon-wrap">%s</div>
                        </div>
                        <h3 class="service-card-title">%s</h3>
                        <p class="service-card-desc">%s</p>
                    </div>
                    <div>%s</div>
                </div>
""" % (i + 1, t.upper()[:26], emoji(start + i, t), t, d, foot)

    return """    <!-- card row -->
    <section class="page-section%s">
        <div class="container">
%s            <div class="bento-grid%s">
%s            </div>
        </div>
    </section>
""" % (" soft" if soft else "", section_head(tag, title, desc), cols, items)


def _connectors(count):
    """build the flowing SVG connector paths for a row of `count` step cards.

    mirrors the home page geometry exactly: a 1000x300 viewBox, card centres at
    1000/count * (i + 0.5), odd cards sitting at y=120 and even cards at y=215
    (the nth-child(2n) margin-top in the stylesheet), with the same control
    point offsets the hand-authored 4-card version uses.
    """
    if count < 2:
        return ""
    w = 1000.0 / count
    paths = []
    for i in range(count - 1):
        sx = w * (i + 0.5)
        ex = w * (i + 1.5) - w * 0.46
        sy, ey = (120, 215) if i % 2 == 0 else (215, 120)
        paths.append(
            '                    <path class="ap-line" d="M%.0f,%d C%.0f,%d %.0f,%d %.0f,%d"></path>'
            % (sx, sy, sx + 65, sy, ex - 60, ey, ex, ey))
    return "\n".join(paths)


def approach_section(tag, title, desc, steps, per_row=4):
    """the home page's our approach timeline: dark panel, zig-zag step cards,
    flowing SVG connectors and the sequential 1-2-3-4 highlight loop.

    the home page hardcodes four steps. longer processes are chunked into rows
    of `per_row`, so the zig-zag, the node pulse and the connector geometry all
    keep working (their CSS is nth-child based, which resets per row).
    """
    # balance the rows rather than filling greedily, so seven steps read as
    # 4 + 3 and six as 3 + 3, instead of leaving a stranded row of two.
    n_steps = len(steps)
    if n_steps <= per_row:
        sizes = [n_steps]
    else:
        n_rows = -(-n_steps // per_row)          # ceil
        base, extra = divmod(n_steps, n_rows)
        sizes = [base + (1 if r < extra else 0) for r in range(n_rows)]

    rows, at = [], 0
    for size in sizes:
        rows.append(steps[at:at + size])
        at += size
    grids = ""
    n = 0
    for r, row in enumerate(rows):
        cards = ""
        for name, text in row:
            cards += """                    <div class="approach-step-card%s" data-step="%d">
                        <div class="approach-node-circle">%d</div>
                        <span class="approach-phase-badge">PHASE %02d</span>
                        <h3>%s</h3>
                        <p>%s</p>
                    </div>
""" % (" active" if n == 0 else "", n, n + 1, n + 1, name, text)
            n += 1

        # the stylesheet points every .ap-line at url(#apArrow), and SVG marker
        # references resolve document-wide, so the marker is defined once.
        defs = """                    <defs>
                        <marker id="apArrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M0,0 L10,5 L0,10 z" fill="context-stroke" style="fill: context-stroke;"></path>
                        </marker>
                    </defs>
""" if r == 0 else ""

        grids += """                <div class="approach-row">
                    <svg class="approach-connectors" viewBox="0 0 1000 300" preserveAspectRatio="none" aria-hidden="true">
%s%s
                    </svg>

                    <div class="approach-steps-grid" data-cols="%d">
%s                    </div>
                </div>
""" % (defs, _connectors(len(row)), len(row), cards)

    return """    <!-- process steps -->
    <section class="approach-section">
        <div class="container">
%s            <div class="approach-timeline-wrap">
                <div class="approach-progress-track">
                    <div class="approach-progress-bar-fill"></div>
                </div>

%s            </div>
        </div>
    </section>
""" % (section_head(tag, title, desc), grids)


def case_filmstrip(tag="Proven Impact &amp; Case Studies",
                   title='Client <span class="text-gradient">Success Stories</span>',
                   desc="Dive into our client success stories, tangible proof of how we turn challenges into success for our clients."):
    """The home page's sliding filmstrip / coverflow of case panels."""
    nav, panels = "", ""
    for i, c in enumerate(CASES):
        nav += """                <button type="button" class="case-nav-btn%s" data-index="%d">
                    <span>%s</span>
                </button>
""" % (" active" if i == 0 else "", i, c["name"])

        metrics = ""
        for val, label in c["stats"][:3]:
            # split a trailing +, % or similar so it can take the accent colour
            head, accent = val, ""
            for suffix in ("+", "%"):
                if val.endswith(suffix):
                    head, accent = val[:-1], suffix
                    break
            metrics += """                                <div class="expanded-metric-box">
                                    <div class="expanded-metric-val">%s%s</div>
                                    <span class="expanded-metric-lbl">%s</span>
                                </div>
""" % (head, ('<span class="accent">%s</span>' % accent) if accent else "", label)

        panels += """                <div class="case-accordion-panel%s" data-index="%d">
                    <img src="%s" class="case-panel-bg" alt="%s" loading="lazy">
                    <div class="case-panel-overlay"></div>

                    <div class="case-panel-collapsed">
                        <span class="collapsed-num">%02d</span>
                        <div class="collapsed-title"><b>%s</b><span>%s</span></div>
                        <div class="collapsed-icon">↗</div>
                    </div>

                    <div class="case-panel-expanded">
                        <div class="expanded-top-row">
                            <div class="expanded-brand-pill">
                                <img src="%s" alt="%s logo">
                            </div>
                            <span class="expanded-sector-tag">%s</span>
                        </div>

                        <div class="expanded-body">
                            <h3 class="expanded-headline">%s</h3>
                            <p class="expanded-desc">%s</p>

                            <div class="expanded-metrics-grid">
%s                            </div>

                            <div class="expanded-actions">
                                <a href="%s" class="btn btn-secondary btn-sm">
                                    Read Full Case Study
                                    %s
                                </a>
                                <a href="contact-us.html" class="btn btn-outline btn-sm" style="color: #ffffff; border-color: rgba(255,255,255,0.3); background: rgba(0,0,0,0.3);">
                                    Book Technical Scoping
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
""" % (" active" if i == 0 else "", i, c["thumb"], c["name"], i + 1, c["name"],
       c["category"], c["logo"], c["name"], c["category"], c["title"],
       trim(c["teaser"]), metrics, c["slug"], ARROW22)

    return """    <!-- client stories -->
    <section class="case-studies-section">
        <div class="container">
%s            <div class="case-accordion-nav">
%s            </div>

            <div class="case-accordion-container">
%s            </div>
        </div>
    </section>
""" % (section_head(tag, title, desc), nav, panels)


def split_section(tag, title, paragraphs, principles, soft=False):
    """Two columns: prose on the left, a numbered principle list on the right."""
    body = "".join("<p>%s</p>" % p for p in paragraphs)
    cards = ""
    for i, (t, d) in enumerate(principles):
        cards += """                    <div class="principle-card">
                        <div class="pc-icon">%s</div>
                        <h3>%s</h3>
                        <p>%s</p>
                    </div>
""" % (icon(i + 1), t, d)

    return """    <!-- split intro -->
    <section class="page-section%s">
        <div class="container">
            <div class="split-grid">
                <div class="split-body">
                    <div class="section-tag">%s</div>
                    <h2 class="section-title">%s</h2>
                    %s
                </div>
                <div class="split-aside">
%s                </div>
            </div>
        </div>
    </section>
""" % (" soft" if soft else "", tag, title, body, cards)


def challenge_section(tag, title, desc, rows, soft=False):
    """rows: list of (challenge, solution). renders as paired rows.

    used on the industry and solution pages, where the argument is always
    "here is what is hard, here is what we do about it".
    """
    cards = ""
    for i, (name, problem, solution) in enumerate(rows):
        cards += """                <div class="cs-card">
                    <div class="cs-head">
                        <span class="cs-num">%02d</span>
                        <h3>%s</h3>
                    </div>
                    <div class="cs-body">
                        <div class="cs-block">
                            <span class="cs-label problem">The Challenge</span>
                            <p>%s</p>
                        </div>
                        <div class="cs-block">
                            <span class="cs-label solution">Our Solution</span>
                            <p>%s</p>
                        </div>
                    </div>
                </div>
""" % (i + 1, name, problem, solution)

    return """    <!-- challenge / solution -->
    <section class="page-section%s">
        <div class="container">
%s            <div class="cs-grid">
%s            </div>
        </div>
    </section>
""" % (" soft" if soft else "", section_head(tag, title, desc), cards)


def pillars_section(pillars=None, title=None, desc=None, tag="Why Bodhi Tech"):
    """The "why us" cards on a dark band. Defaults to the shared PILLARS."""
    pillars = pillars or PILLARS
    title = title or 'Let\'s collaborate and <span class="text-gradient">innovate</span>'
    desc = desc or ("Whether you're embarking on the startup journey or navigating the growth "
                    "trajectory of an enterprise, you can count on us to deliver customised "
                    "solutions that align perfectly with your objectives.")
    cards = ""
    for i, (t, d) in enumerate(pillars):
        cards += """                <div class="pillar-card">
                    <div class="pc-icon">%s</div>
                    <h3>%s</h3>
                    <p>%s</p>
                </div>
""" % (icon(i + 4), t, d)

    return """    <!-- why us -->
    <section class="page-section dark">
        <div class="container">
%s            <div class="pillar-grid">
%s            </div>
        </div>
    </section>
""" % (section_head(tag, title, desc), cards)


def testimonials_section(limit=6, soft=False):
    """The home page's "what our partners say" section, verbatim.

    the markup lives in partials/testimonials.html, extracted from index.html,
    so the subpages cannot drift from the home page. the only substitution is
    the CTA target: on the home page it jumps to the in-page contact block, on
    a subpage it goes to the contact page.

    `limit` and `soft` are kept so existing call sites still work, but the
    section is deliberately identical everywhere now, so they are ignored.
    """
    return _TESTIMONIALS_PARTIAL.replace("__CTA__", "contact-us.html")


def counter_band(stats, tag="Track Record", title=None, desc=""):
    """Reuses .counter-blocks / .counter-block, including the count-up animation."""
    blocks = ""
    for i, (target, symbol, heading, sub) in enumerate(stats):
        blocks += """                <div class="counter-block cb-%d">
                    <span class="counter-badge-tag">%s</span>
                    <div class="counter-block-foot">
                        <div class="counter-digit-row">
                            <span class="counter-number" data-target="%s">0</span>
                            <span class="symbol">%s</span>
                        </div>
                        <h4>%s</h4>
                        <p>%s</p>
                    </div>
                </div>
""" % (i + 1, tag, target, symbol, heading, sub)

    head = section_head("By the Numbers", title, desc) if title else ""
    return """    <!-- stat band -->
    <section class="page-section tight">
        <div class="container">
%s            <div class="counter-blocks">
%s            </div>
        </div>
    </section>
""" % (head, blocks)


def faq_section(items, tag="Got Questions?", title=None, desc="", soft=True):
    """items: list of (question, answer). the accordion behaviour is in
    js/site.js and keys off .faq-item, so nothing needs wiring up here.
    """
    title = title or 'Frequently Asked <span class="text-gradient">Questions</span>'
    rows = ""
    for q, a in items:
        rows += """                <div class="faq-item">
                    <div class="faq-header">
                        <h3>%s</h3>
                        <div class="faq-toggle-icon">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
                        </div>
                    </div>
                    <div class="faq-body">
                        <div class="faq-body-inner">
                            <p>%s</p>
                        </div>
                    </div>
                </div>
""" % (q, a)

    return """    <!-- faq -->
    <section class="page-section%s">
        <div class="container">
%s            <div class="faq-wrapper faq-flow">
%s            </div>
        </div>
    </section>
""" % (" soft" if soft else "", section_head(tag, title, desc), rows)


def cta_band(title=None, desc=None,
             primary=("Book a Free Consultation", "contact-us.html"),
             secondary=("Explore Our Solutions", "solutions.html")):
    """the closing call to action. every page except the legal ones ends here.

    the defaults are the point: pass nothing and you get the standard band, so
    there is no reason for a page to invent its own closing copy.
    """
    title = title or 'Let\'s collaborate and <span class="text-gradient">innovate</span>'
    desc = desc or "Got questions or want a free consultation? Reach out to us, we're here to help."
    return """    <!-- cta -->
    <section class="cta-band">
        <div class="container">
            <div class="cta-band-inner">
                <div class="section-tag">Get In Touch</div>
                <h2 class="section-title">%s</h2>
                <p class="section-desc">%s</p>
                <div class="cta-band-actions">
                    <a href="%s" class="btn btn-primary">%s</a>
                    <a href="%s" class="btn btn-outline">%s</a>
                </div>
            </div>
        </div>
    </section>
""" % (title, desc, primary[1], primary[0], secondary[1], secondary[0])


def solutions_cards(exclude=None):
    """cards for every solution, optionally leaving one out.

    exclude is the slug of the page doing the asking, so a solution page does
    not list itself under "more solutions".
    """
    cards = ""
    n = 0
    for s in SOLUTIONS:
        if s["slug"] == exclude:
            continue
        cards += """                <div class="service-bento-card">
                    <div>
                        <div class="service-card-top-bar">
                            <span class="service-card-index"><i>%02d</i>%s</span>
                            <div class="service-card-icon-wrap">%s</div>
                        </div>
                        <h3 class="service-card-title"><a href="%s">%s</a></h3>
                        <p class="service-card-desc">%s</p>
                    </div>
                    <div>
                        <div class="service-card-footer">
                            <a href="%s" class="service-card-link">
                                <span>Explore %s</span>
                                %s
                            </a>
                            <div class="service-card-arrow">↗</div>
                        </div>
                    </div>
                </div>
""" % (n + 1, s["short"].upper(), emoji(n, s["name"]), s["slug"], s["name"], s["summary"],
       s["slug"], s["short"], ARROW22)
        n += 1
    return cards


def related_solutions(exclude=None):
    """The full "more solutions" section, wrapped round solutions_cards()."""
    return """    <!-- more solutions -->
    <section class="page-section soft">
        <div class="container">
%s            <div class="bento-grid">
%s            </div>
        </div>
    </section>
""" % (section_head("More Solutions",
                    'Explore our other <span class="text-gradient">capabilities</span>',
                    "Every engagement can draw on the full stack of Bodhi Tech services."),
       solutions_cards(exclude=exclude))

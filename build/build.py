# -*- coding: utf-8 -*-
"""writes the 24 inner pages. run: python3 build/build.py

those .html files are generated - edit one by hand and the next run wipes it.
change content.py for the words, blocks.py for the layout. index.html is the
exception, that one is hand-written.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from content import (SITE, PILLARS, INDUSTRY_PILLARS, TESTIMONIALS,
                     CASES, SOLUTIONS, INDUSTRIES, BLOG_POSTS, HERO_IMAGES)
import blocks as B
import articles as A

HEADER = open(os.path.join(ROOT, "partials", "header.html")).read()
FOOTER = open(os.path.join(ROOT, "partials", "footer.html")).read()
WIDGETS = open(os.path.join(ROOT, "partials", "widgets.html")).read()

FAQS = [
    ("What digital services does Bodhi Tech specialise in?",
     "Bodhi Tech specialises in end-to-end digital solutions, including custom web development, mobile app and platform development, strategic digital marketing, UX/UI graphic design, and dedicated staff augmentation. We partner with startups, SMEs, and established Australian businesses to engineer digital assets that accelerate revenue and streamline operations."),
    ("How does Bodhi Tech approach custom software and web development projects?",
     "We follow a proven four-pillar methodology: Discovery, Strategise, Design and Develop, and Launch and Optimise. We begin by gaining deep clarity on your business story and KPIs before writing code, ensuring every architectural decision supports scalability, security, and long-term business performance."),
    ("What is the typical project timeline and collaboration model?",
     "Timelines depend on the scope and complexity of your requirements. Typical web and branding projects take 4 to 8 weeks, while complex web applications or mobile platforms generally range from 8 to 16 weeks. Throughout the project, we provide dedicated project managers, weekly sprint updates, and transparent milestone demonstrations."),
    ("How do you ensure post-launch support and continuous optimisation?",
     "We position ourselves as your continuous strategic partner beyond deployment. We offer ongoing maintenance, performance tuning, security audits, SEO monitoring, and agile feature iterations to keep your digital platform ahead of competitors and aligned with technological advancements."),
    ("How can we get started with a free consultation?",
     "Getting started is quick and simple. Fill out the contact form or click the Book a Free Consultation button, and our strategic consulting team will schedule an introductory discovery session to discuss your vision, evaluate technical feasibility, and map out a tailored roadmap for your brand."),
]

SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%(title)s</title>
    <meta name="description" content="%(desc)s">
    <link rel="canonical" href="https://bodhitech.com.au/%(slug)s">
    <link rel="icon" type="image/x-icon" href="https://bodhitech.com.au/wp-content/uploads/2023/11/favicon.svg">

    <meta property="og:type" content="website">
    <meta property="og:title" content="%(title)s">
    <meta property="og:description" content="%(desc)s">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">

    <link rel="stylesheet" href="css/site.css">
    <link rel="stylesheet" href="css/pages.css">
</head>
<body class="subpage" data-nav="%(nav)s">

%(header)s

%(body)s
%(footer)s
%(widgets)s
    <!-- site.js before pages.js -->
    <script src="js/site.js"></script>
    <script src="js/pages.js"></script>

</body>
</html>
"""

PAGES = []


def write(slug, title, desc, nav, body):
    """drops a body into the shared shell and writes the file.

    also records the slug in PAGES, which the sitemap and the link check at the
    bottom of this file both read. if you ever write a page without going
    through here, it will be invisible to both.
    """
    html = SHELL % {"title": title, "desc": desc, "slug": slug, "nav": nav,
                    "header": HEADER, "body": body, "footer": FOOTER, "widgets": WIDGETS}
    open(os.path.join(ROOT, slug), "w").write(html)
    PAGES.append(slug)
    return slug


def grad(text, word):
    """Wrap the trailing phrase in the .text-gradient accent span."""
    return text.replace(word, '<span class="text-gradient">%s</span>' % word, 1)


# solution detail pages. one page per entry in SOLUTIONS.

for s in SOLUTIONS:
    title_html = s["h1"].replace("<em>", '<span class="text-gradient">').replace("</em>", "</span>")
    hero_chip = (B.icon("leaf"), s["meta"][0][0], s["meta"][0][1])
    body = B.page_hero(
        "Solutions", title_html, s["lead"],
        [("Home", "index.html"), ("Solutions", "solutions.html"), (s["short"], None)],
        meta=s["meta"][1:], variant="split",
        image=HERO_IMAGES.get(s["slug"]), chip=hero_chip)
    body += B.trust_strip()
    body += B.split_section("Our Philosophy", s["intro_h"], s["intro_p"], s["principles"])
    body += B.approach_section("Our Methodology", grad(s["approach_h"], "Approach"),
                               s["approach_sub"], s["steps"])
    body += B.bento_section("Our Offerings", s["offer_h"], s["offer_sub"], s["offerings"], start=2)
    body += B.case_filmstrip()
    body += B.testimonials_section(3)
    body += B.pillars_section()
    body += B.related_solutions(exclude=s["slug"])
    body += B.cta_band(secondary=("Talk to a Strategist", "contact-us.html"))

    write(s["slug"], "%s | Bodhi Tech" % s["name"], s["lead"].replace('"', "'"), "solutions", body)


# solutions index. the listing that links to them.

body = B.page_hero(
    "Solutions",
    'Elevating possibilities, <span class="text-gradient">innovating futures</span>',
    "We specialise in delivering tailor-made, innovative technological solutions designed to propel SMEs and startups towards exponential growth. From scalable software solutions to strategic digital guidance, we offer a comprehensive suite of services aimed at amplifying your success.",
    [("Home", "index.html"), ("Solutions", None)],
    meta=[("6", "Core solutions"), ("100+", "Projects delivered"), ("74", "Net Promoter Score")])
body += B.trust_strip()
body += """    <section class="page-section">
        <div class="container">
%s            <div class="bento-grid">
%s            </div>
        </div>
    </section>
""" % (B.section_head("Our Solutions",
                      'Empower your journey with <span class="text-gradient">world class services</span>',
                      "Empower your journey with Bodhi Tech's world class services, where your aspirations seamlessly transform into reality."),
       B.solutions_cards())
body += B.case_filmstrip()
body += B.pillars_section(title='Why <span class="text-gradient">choose us?</span>')
body += B.testimonials_section(3)
body += B.faq_section(FAQS)
body += B.cta_band()

write("solutions.html", "Solutions | Bodhi Tech",
      "Tailor-made technological solutions for SMEs and startups: web development, marketing strategy, UX/UI design, staff augmentation, digital marketing and mobile app development.",
      "solutions", body)


# industry pages. one page per entry in INDUSTRIES.

for ind in INDUSTRIES:
    title_html = ind["h1"].replace("<em>", '<span class="text-gradient">').replace("</em>", "</span>")
    body = B.page_hero(
        "Industries", title_html, ind["lead"],
        [("Home", "index.html"), ("Industries", "industries.html"), (ind["name"], None)],
        meta=ind["meta"], variant="photo", bg=HERO_IMAGES.get(ind["slug"]))
    body += B.trust_strip()

    if ind.get("templates"):
        body += B.bento_section(
            "Ready to Launch",
            'Ready-to-launch <span class="text-gradient">website templates</span>',
            "We have ready-made custom website templates for your construction company, tailored to grab the attention of your clients.",
            ind["templates"], cols=" cols-2", start=7,
            links=[("Preview this template", "contact-us.html")] * len(ind["templates"]))

    body += B.bento_section("Our Offerings", ind["offer_h"], ind["offer_sub"],
                            ind["offerings"], soft=not ind.get("templates"),
                            cols=" cols-2", start=1)
    body += B.challenge_section("Challenges &amp; Solutions",
                                grad(ind["cs_h"], "challenges"), ind["cs_sub"],
                                ind["challenges"], soft=bool(ind.get("templates")))
    body += B.pillars_section(
        pillars=INDUSTRY_PILLARS,
        title='Why choose us for <span class="text-gradient">your business?</span>',
        desc="We empower your journey with seamlessly integrated, customised solutions, providing the tools you need to excel.")
    body += B.case_filmstrip()
    body += B.testimonials_section(3)
    body += B.cta_band(
        desc="Embark on a journey of enlightenment and innovation at Bodhi Tech. Our tech solutions are designed to empower and propel your business into a brighter future.")

    write(ind["slug"], "%s | Bodhi Tech" % ind["name"],
          ind["lead"][:190].replace('"', "'"), "industries", body)


# industries index

ind_cards = ""
for i, ind in enumerate(INDUSTRIES):
    ind_cards += """                <div class="service-bento-card">
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
""" % (i + 1, ind["name"].upper()[:22], B.emoji(i + 6, ind["name"]), ind["slug"], ind["name"],
       ind["summary"], ind["slug"], ind["name"], B.ARROW22)

body = B.page_hero(
    "Industries",
    'Empowering industries by exploring and <span class="text-gradient">innovating sectors</span>',
    "We empower various industries by exploring and innovating within different sectors. Our goal is to drive growth and transformation across diverse fields, ensuring progress and innovation thrive in every domain.",
    [("Home", "index.html"), ("Industries", None)],
    meta=[("3", "Specialist sectors"), ("5+", "Years of operation"), ("74", "Net Promoter Score")])
body += B.trust_strip()
body += """    <section class="page-section">
        <div class="container">
%s            <div class="bento-grid">
%s            </div>
        </div>
    </section>
""" % (B.section_head("Our Industries",
                      'Custom industry solutions, turning your <span class="text-gradient">vision into success</span>',
                      "Explore exciting opportunities with Bodhi Tech's custom industry solutions."), ind_cards)
body += B.pillars_section(
    pillars=INDUSTRY_PILLARS,
    title='Why choose us for <span class="text-gradient">your industry needs?</span>',
    desc="We empower your journey with seamlessly integrated, customised solutions, providing the tools you need to excel.")
body += B.case_filmstrip()
body += B.testimonials_section(3)
body += B.cta_band()

write("industries.html", "Industries We Serve | Bodhi Tech",
      "Bodhi Tech delivers custom digital solutions for startups and SMEs, promotional products and merchandising companies, and the construction industry.",
      "industries", body)


# case study pages. one page per entry in CASES.

for c in CASES:
    results = "".join(
        '<div class="result-card"><strong>%s</strong><span>%s</span></div>' % (v, l)
        for v, l in c["stats"])
    services = "".join('<span class="pill">%s</span>' % x for x in c["services"])
    tech = B.tech_badges(c["tech"])

    others = [x for x in CASES if x["slug"] != c["slug"]][:3]
    other_cards = ""
    for o in others:
        other_cards += """                <div class="blog-card">
                    <div class="blog-img-wrap">
                        <img src="%s" alt="%s case study" loading="lazy">
                    </div>
                    <div class="blog-content">
                        <div>
                            <div class="blog-meta"><span class="blog-author">%s</span><span>&bull;</span><span>%s</span></div>
                            <h3>%s</h3>
                            <p>%s</p>
                        </div>
                        <a href="%s" class="blog-link">View in Detail %s</a>
                    </div>
                </div>
""" % (o["thumb"], o["name"], o["name"], o["category"], o["title"],
       o["teaser"][:150] + "...", o["slug"], B.ARROW)

    body = B.page_hero(
        c["category"], c["title"], B.trim(c["teaser"], 240),
        [("Home", "index.html"), ("Client Stories", "client-stories.html"), (c["name"], None)],
        variant="case", brand=(c["logo"], c["name"]), results=c["stats"],
        actions=[("Start a Project Like This", "contact-us.html", "btn-primary"),
                 ("See More Stories", "client-stories.html", "btn-outline")])

    body += """    <section class="page-section soft">
        <div class="container">
            <div class="cs-grid">
                <div class="cs-card">
                    <div class="cs-head"><span class="cs-num">01</span><h3>Where %s started</h3></div>
                    <div class="cs-body">
                        <div class="cs-block">
                            <span class="cs-label problem">The Challenge</span>
                            <p>%s</p>
                        </div>
                    </div>
                </div>
                <div class="cs-card">
                    <div class="cs-head"><span class="cs-num">02</span><h3>What we did about it</h3></div>
                    <div class="cs-body">
                        <div class="cs-block">
                            <span class="cs-label solution">Our Solution</span>
                            <p>%s</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
""" % (c["name"], c["challenge"], c["solution"])

    body += """    <section class="page-section">
        <div class="container">
            <div class="split-grid">
                <div class="split-body">
                    <div class="section-tag">Services Delivered</div>
                    <h2 class="section-title">The work, <span class="text-gradient">end to end</span></h2>
                    <p>Everything below was delivered by one team, so nothing was lost in a handover between vendors.</p>
                    <div class="pill-row">%s</div>
                </div>
                <div class="split-body">
                    <div class="section-tag">Tech Stack</div>
                    <h2 class="section-title">Built <span class="text-gradient">with</span></h2>
                    <p>Chosen for maintainability and cost, not novelty.</p>
                    <div class="tech-badge-row">
%s                    </div>
                </div>
            </div>
        </div>
    </section>
""" % (services, tech)

    body += """    <section class="page-section soft">
        <div class="container">
            <div class="big-quote">
                <blockquote>%s</blockquote>
                <cite>%s<span>%s</span></cite>
            </div>
        </div>
    </section>
""" % (c["quote"], c["quote_name"], c["quote_role"])

    body += """    <section class="page-section">
        <div class="container">
%s            <div class="listing-grid">
%s            </div>
        </div>
    </section>
""" % (B.section_head("Keep Reading", 'More <span class="text-gradient">client stories</span>', ""),
       other_cards)

    body += B.cta_band(title='Ready to write <span class="text-gradient">your story?</span>',
                       desc="Tell us where your business is stuck. We'll tell you honestly whether we can help, and what it would take.")

    write(c["slug"], "%s Case Study | Bodhi Tech" % c["name"],
          c["teaser"][:190].replace('"', "'"), "stories", body)


# client stories index. uses the showcase hero, the one with the mosaic.

story_cards = ""
for c in CASES:
    stats = " &middot; ".join("%s %s" % (v, l.lower()) for v, l in c["stats"][:2])
    story_cards += """                <div class="blog-card">
                    <div class="blog-img-wrap">
                        <img src="%s" alt="%s case study" loading="lazy">
                    </div>
                    <div class="blog-content">
                        <div>
                            <div class="blog-meta"><span class="blog-author">%s</span><span>&bull;</span><span>%s</span></div>
                            <h3>%s</h3>
                            <p>%s</p>
                        </div>
                        <a href="%s" class="blog-link">View in Detail %s</a>
                    </div>
                </div>
""" % (c["thumb"], c["name"], c["category"], stats, c["title"], c["teaser"], c["slug"], B.ARROW)

body = B.page_hero(
    "Client Stories",
    'Triumphs and transformations, in our <span class="text-gradient">clients\' numbers</span>',
    "We believe our clients' success is our success. Every story below is a real Australian business, a real brief and a result we can put a figure against.",
    [("Home", "index.html"), ("Client Stories", None)],
    variant="showcase",
    meta=[("4", "Featured stories"), ("100+", "Projects completed"), ("74", "Net Promoter Score")],
    actions=[("Start Your Story", "contact-us.html", "btn-secondary"),
             ("Talk to Us", "contact-us.html", "btn-outline")],
    mosaic=[(c["thumb"], c["name"],
             "%s %s" % (c["stats"][0][0], c["stats"][0][1].lower()), c["slug"])
            for c in CASES])
body += B.trust_strip()
body += B.case_filmstrip(
    tag="Case Studies",
    title='Proof, not <span class="text-gradient">promises</span>',
    desc="Embark on a journey of enlightenment and innovation at Bodhi Tech. Our tech solutions are designed to empower and propel you into a brighter future.")
body += B.counter_band([
    ("5", "+", "Years of Operation", "Strategic partners for Australian high-growth brands"),
    ("100", "+", "Projects Completed", "App and website builds shipped end to end"),
    ("74", "", "Net Promoter Score", "Measured across our active client base"),
])
body += B.testimonials_section(6, soft=True)
body += B.cta_band(title='Ready to write <span class="text-gradient">your story?</span>')

write("client-stories.html", "Client Stories | Bodhi Tech",
      "Case studies from Bodhi Tech: Chilli Promotions, Take A Local, Boobobutt and Capability. Real numbers from real Australian businesses.",
      "stories", body)


# about us

body = B.page_hero(
    "About Us",
    'Your strategic <span class="text-gradient">digital partner</span>',
    "We are not just a digital agency; we are your strategic partner committed to fueling your business growth journey.",
    [("Home", "index.html"), ("About Us", None)],
    meta=[("100+", "Projects completed"), ("74", "Net Promoter Score")],
    variant="split", image=HERO_IMAGES.get("about-us.html"),
    chip=(B.icon("leaf"), "5+", "Years of operation"),
    actions=[("Work With Us", "contact-us.html", "btn-primary"),
             ("See Our Work", "client-stories.html", "btn-outline")])
body += B.trust_strip()
body += B.split_section(
    "Our Story",
    'The tale of <span class="text-gradient">Bodhi Tech</span>',
    ["The name Bodhi draws inspiration from the tree under which Lord Gautam Buddha attained enlightenment. It symbolises our mission to assist SMEs and startups in achieving digital enlightenment, harnessing technology and digital services to enhance their businesses.",
     "Bodhi Tech is a Melbourne-based digital marketing and software development company catering to startups and SMEs in Australia. We take pride in our strong ties to Nepal, where we have a large team of technical experts working diligently for our international clients.",
     "Founded in 2017, the agency emerged from a vision to democratise access to high-quality digital services for smaller enterprises, the businesses usually priced out of the strategy, design and engineering that larger companies take for granted."],
    [("Our Mission", "To champion entrepreneurship and innovation by empowering SMEs and startups through talent based in Nepal."),
     ("Our Vision", "To support thousands of global businesses while creating opportunities for 10,000+ professionals in Nepal, enabling them to work for an innovative company without being confined by the borders of their beautiful, landlocked country.")])
body += B.counter_band([
    ("5", "+", "Years of Operation", "Strategic partners for Australian high-growth brands"),
    ("100", "+", "Projects Completed", "App and website builds shipped end to end"),
    ("74", "", "Net Promoter Score", "Measured across our active client base"),
])
body += B.bento_section(
    "Brand Voice", 'What we <span class="text-gradient">stand for</span>',
    "Bodhi Tech's core values centre on being a collaborative, authentic and strategic partner to our clients.",
    [("Distinctiveness", "We embody the principles of Byron Sharp, focusing on distinctiveness to stand out in a competitive market. Sameness is the most expensive mistake a growing brand can make."),
     ("Heritage", "We retain our identity as an Australian company while acknowledging our Nepali cultural heritage. Both are load-bearing, neither is decoration."),
     ("Youthfulness", "We present a youthful and dynamic image while staying true to our design roots, because the businesses we serve are building something new."),
     ("Collaboration", "Our brand is founded on a strong technical infrastructure, allowing us to deliver innovative and cost-effective solutions as a collaborative, authentic and strategic partner.")],
    soft=True, start=3)
body += B.approach_section(
    "Our Methodology", 'How we <span class="text-gradient">work</span>',
    "Four phases, applied whether we are building a marketing strategy, a website or a mobile platform.",
    [("Discovery", "We unravel the intricacies of your brand, goals and aspirations, and lay the foundation for work that reflects your actual identity rather than a category template."),
     ("Strategise", "We build purposeful roadmaps over short-term tactics, defining objectives, audiences and the metrics that will tell us whether it worked."),
     ("Design and Develop", "Our design and engineering teams bring the strategy to life, to industry-leading standards of security, performance and responsiveness."),
     ("Launch and Optimise", "Launch is the beginning, not the end. We refine continuously based on real-time analytics, user feedback and emerging trends.")])
body += B.pillars_section()
body += B.case_filmstrip()
body += B.testimonials_section(6)
body += B.cta_band(title='Let\'s build something <span class="text-gradient">worth keeping</span>')

write("about-us.html", "About Us | Bodhi Tech",
      "Bodhi Tech is a Melbourne-based digital marketing and software development company for startups and SMEs, with a large technical team in Nepal.",
      "company", body)


# contact us

body = B.page_hero(
    "Contact", '<span class="text-gradient">Contact</span> Us',
    "Got questions or want a free consultation? Reach out to us, we're here to help. At Bodhi Tech our tech solutions are designed to empower and propel you into a brighter, purposeful future.",
    [("Home", "index.html"), ("Contact Us", None)],
    variant="minimal",
    actions=[("Call %s" % SITE["phone"], SITE["phone_href"], "btn-primary"),
             ("Email Us", "mailto:%s" % SITE["email"], "btn-outline")])

body += """    <section class="page-section">
        <div class="container">
            <div class="contact-methods">
                <div class="contact-method">
                    <div class="cm-icon">%s</div>
                    <h3>Email Us</h3>
                    <p>We're here to help</p>
                    <a href="mailto:%s">%s</a>
                </div>
                <div class="contact-method">
                    <div class="cm-icon">%s</div>
                    <h3>Call Us</h3>
                    <p>Mon to Fri from 9am to 6pm</p>
                    <a href="%s">%s</a>
                </div>
                <div class="contact-method">
                    <div class="cm-icon">%s</div>
                    <h3>Visit Us</h3>
                    <p>Our Melbourne office</p>
                    <a href="https://maps.google.com/?q=470+St+Kilda+Road+Melbourne" target="_blank" rel="noopener">%s</a>
                </div>
                <div class="contact-method">
                    <div class="cm-icon">%s</div>
                    <h3>Follow Us</h3>
                    <p>Visit our LinkedIn</p>
                    <a href="https://www.linkedin.com/company/bodhi-tech/" target="_blank" rel="noopener">View Profile</a>
                </div>
            </div>
        </div>
    </section>
""" % (B.icon(10), SITE["email"], SITE["email"], B.icon(9), SITE["phone_href"],
       SITE["phone"], B.icon(7), SITE["address"], B.icon(1))

body += """    <section class="page-section soft">
        <div class="container">
%s            <div class="contact-landscape-bento">
                <div class="contact-hub-sidebar">
                    <div class="hub-pillars-list">
%s                    </div>
                    <div class="hub-direct-info">
                        <div class="hub-direct-link"><span class="hdl-ico">%s</span><span>%s</span></div>
                        <a href="%s" class="hub-direct-link"><span class="hdl-ico">%s</span><span>%s</span></a>
                        <a href="mailto:%s" class="hub-direct-link"><span class="hdl-ico">%s</span><span>%s</span></a>
                    </div>
                </div>
                <div class="contact-form-side">
                    <div class="contact-form-header">
                        <h3>Send us a message</h3>
                        <p>Tell us where your business is stuck. We will come back to you within one business day.</p>
                    </div>
                    <form id="contactForm" class="landscape-form-grid">
                        <div class="form-group">
                            <label class="form-label" for="userName">Full Name</label>
                            <input type="text" id="userName" class="form-control" placeholder="e.g. John Smith" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="userEmail">Email Address</label>
                            <input type="email" id="userEmail" class="form-control" placeholder="name@company.com" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="userPhone">Phone Number</label>
                            <input type="tel" id="userPhone" class="form-control" placeholder="+61 400 000 000">
                        </div>
                        <div class="form-group">
                            <label class="form-label" for="userCompany">Company Name</label>
                            <input type="text" id="userCompany" class="form-control" placeholder="Your company">
                        </div>
                        <div class="form-group full-span">
                            <label class="form-label" for="userInterest">What can we help with?</label>
                            <select id="userInterest" class="form-control">
%s                            </select>
                        </div>
                        <div class="form-group full-span">
                            <label class="form-label" for="userMessage">Message</label>
                            <textarea id="userMessage" class="form-control" placeholder="Tell us about your project vision, timeline, and goals..."></textarea>
                        </div>
                        <div class="form-group full-span">
                            <button type="submit" class="btn btn-primary" style="width:100%%;">Send My Request</button>
                            <p style="font-size:0.85rem;margin-top:14px;text-align:center;color:var(--muted);">By clicking the button above, you accept our <a href="terms-and-conditions.html" style="color:var(--primary);font-weight:700;">Terms &amp; Conditions</a>.</p>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </section>
""" % (B.section_head("Get In Touch",
                      'Let\'s collaborate and <span class="text-gradient">innovate</span>',
                      "One form, one strategist, no call centre."),
       "".join("""                        <div class="hub-pillar-item">
                            <div class="hub-pillar-icon">%s</div>
                            <div class="hub-pillar-text">
                                <h4>%s</h4>
                                <p>%s</p>
                            </div>
                        </div>
""" % (B.emoji(i + 6, t), t, d) for i, (t, d) in enumerate(PILLARS)),
       B.icon("pin"), SITE["address"],
       SITE["phone_href"], B.icon("phone"), SITE["phone"],
       SITE["email"], B.icon("mail"), SITE["email"],
       "".join('                                <option>%s</option>\n' % s["name"] for s in SOLUTIONS) +
       '                                <option>Something else</option>\n')

body += B.faq_section(FAQS, soft=False)
body += B.cta_band(title='Prefer to just <span class="text-gradient">talk?</span>',
                   desc="Book a 30-minute free business consultation and we will tell you honestly whether we can help.",
                   primary=("Call %s" % SITE["phone"], SITE["phone_href"]),
                   secondary=("Browse Our Solutions", "solutions.html"))

write("contact-us.html", "Contact Us | Bodhi Tech",
      "Contact Bodhi Tech in Melbourne. Email info@bodhitech.com.au, call +61 485 980 712, or book a free consultation.",
      "company", body)


# blog index

post_cards = ""
for p in BLOG_POSTS:
    post_cards += """                <div class="blog-card">
                    <div class="blog-img-wrap">
                        <img src="%s" alt="%s" loading="lazy">
                    </div>
                    <div class="blog-content">
                        <div>
                            <div class="blog-meta"><span class="blog-author">Bodhi Tech</span><span>&bull;</span><span>%s</span><span>&bull;</span><span>%s</span></div>
                            <h3>%s</h3>
                            <p>%s</p>
                        </div>
                        <a href="%s" class="blog-link">Read More %s</a>
                    </div>
                </div>
""" % (p["image"], p["title"], p["date"], p["read"], p["title"], p["excerpt"], p["slug"], B.ARROW)

body = B.page_hero(
    "Insights", 'Blogs &amp; <span class="text-gradient">Insights</span>',
    "Thought leadership from the Bodhi Tech team on web development, digital marketing and getting more out of the budget you actually have.",
    [("Home", "index.html"), ("Blogs &amp; Insights", None)],
    actions=[("Book a Free Consultation", "contact-us.html", "btn-primary"),
             ("Explore Our Solutions", "solutions.html", "btn-outline")])
body += """    <section class="page-section">
        <div class="container">
%s            <div class="listing-grid">
%s            </div>
        </div>
    </section>
""" % (B.section_head("Latest Articles",
                      'Practical writing for <span class="text-gradient">growing businesses</span>',
                      "No filler and no listicles for their own sake. Just what we have learned shipping for Australian SMEs."),
       post_cards)
body += B.cta_band(title='Want this applied to <span class="text-gradient">your site?</span>',
                   desc="Book a 30-minute free consultation and we will look at your website with you.")

write("blog.html", "Blogs & Insights | Bodhi Tech",
      "Articles from the Bodhi Tech team on web development trends, promotional product e-commerce and optimising your business website on a budget.",
      "company", body)


# blog posts. bodies live in articles.py.

for p in BLOG_POSTS:
    art = A.ARTICLES[p["slug"]]
    toc = "".join('<li><a href="#%s">%s</a></li>' % (a, t) for a, t in art["toc"])
    others = [o for o in BLOG_POSTS if o["slug"] != p["slug"]]
    more = "".join('<li><a href="%s">%s</a></li>' % (o["slug"], o["title"]) for o in others)

    body = B.page_hero(
        None, p["title"], p["excerpt"],
        [("Home", "index.html"), ("Blogs &amp; Insights", "blog.html"), (p["category"], None)],
        variant="article", actions=[],
        article={"category": p["category"], "date": p["date"], "read": p["read"],
                 "image": p["image"], "alt": p["title"]})

    body += """    <section class="page-section">
        <div class="container">
            <div class="prose-layout">
                <article class="prose">
%s
                </article>
                <aside class="prose-aside">
                    <div class="aside-card">
                        <h4>On this page</h4>
                        <ul class="toc-list">%s</ul>
                    </div>
                    <div class="aside-card">
                        <h4>Keep reading</h4>
                        <ul class="toc-list">%s</ul>
                    </div>
                    <div class="aside-card cta-aside">
                        <h4>Need a hand?</h4>
                        <p>Book a 30-minute free business consultation and we will evaluate how we can fit within your budget.</p>
                        <a href="contact-us.html" class="btn btn-primary btn-sm">Book a Consultation</a>
                    </div>
                </aside>
            </div>
        </div>
    </section>
""" % (art["html"], toc, more)

    body += B.cta_band(title='Let\'s put this to <span class="text-gradient">work</span>',
                       desc="Tell us what you are trying to fix. We will tell you what it takes.")

    write(p["slug"], "%s | Bodhi Tech" % p["title"],
          p["excerpt"][:190].replace('"', "'"), "company", body)


# legal pages. minimal hero, prose body, no CTA band.

for slug, title, tag, lead, updated, html, toc in A.LEGAL:
    title_html = title.replace("<em>", '<span class="text-gradient">').replace("</em>", "</span>")
    toc_html = "".join('<li><a href="#%s">%s</a></li>' % (a, t) for a, t in toc)

    body = B.page_hero(tag, title_html, lead,
                       [("Home", "index.html"), (tag, None)],
                       meta=[(updated, "Last updated")], variant="minimal",
                       actions=[("Contact Us", "contact-us.html", "btn-primary")])

    body += """    <section class="page-section">
        <div class="container">
            <div class="prose-layout">
                <article class="prose">
%s
                </article>
                <aside class="prose-aside">
                    <div class="aside-card">
                        <h4>On this page</h4>
                        <ul class="toc-list">%s</ul>
                    </div>
                    <div class="aside-card">
                        <h4>Related</h4>
                        <ul class="toc-list">
                            <li><a href="privacy-policy.html">Privacy Policy</a></li>
                            <li><a href="terms-and-conditions.html">Terms &amp; Conditions</a></li>
                            <li><a href="contact-us.html">Contact Us</a></li>
                        </ul>
                    </div>
                </aside>
            </div>
        </div>
    </section>
""" % (html, toc_html)

    write(slug, "%s | Bodhi Tech" % tag, lead[:190].replace('"', "'"), "company", body)


print("Built %d pages:" % len(PAGES))
for p in sorted(PAGES):
    print("  " + p)

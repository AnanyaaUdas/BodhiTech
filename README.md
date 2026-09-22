# Bodhi Tech Website

Plain HTML, CSS and JavaScript. No build step is needed to view it.

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`. Opening `index.html` directly from Finder
also works.

## What changed in this pass

The site was one self-contained `index.html` of 6,854 lines with all CSS and JS
inline. To let 24 new subpages share the same design system and the same
animation engine, the inline blocks were pulled out into files:

| Was | Now |
|---|---|
| 3 inline `<style>` blocks | `css/site.css` |
| 2 inline `<script>` blocks | `js/site.js` |
| `script.js` (unused stale duplicate, not linked from anywhere) | removed, recoverable from git |

`index.html` is now about 1,840 lines and links to those files. Nothing about
the design changed in the move: the scroll-scrub hero, the word-by-word heading
reveals, the tech scatter, the case filmstrip and the approach connectors all
behave exactly as before.

## Pages (25)

| Section | Files |
|---|---|
| Home | `index.html` |
| Solutions | `solutions.html`, `web-development.html`, `marketing-strategy.html`, `ux-ui-graphic-design.html`, `staff-augmentation.html`, `digital-marketing-services.html`, `mobile-app-development.html` |
| Industries | `industries.html`, `startups-and-smes.html`, `promotional-products.html`, `construction.html` |
| Client Stories | `client-stories.html`, `case-chilli-promotions.html`, `case-take-a-local.html`, `case-boobobutt.html`, `case-capability.html` |
| Company | `about-us.html`, `contact-us.html` |
| Blog | `blog.html`, `blog-web-development-trends-2025.html`, `blog-promotional-product-ecommerce.html`, `blog-optimise-website-on-a-budget.html` |
| Legal | `privacy-policy.html`, `terms-and-conditions.html` |

## File layout

```
index.html              Home page
*.html                  Generated subpages
css/site.css            Main stylesheet, extracted from index.html
css/pages.css           Subpage-only components
js/site.js              UI behaviour + the scroll animation engine
js/pages.js             Subpage behaviour: active nav, drawer groups, hero heading reveal
partials/               Shared header, footer and chat widget markup
build/                  Page generator
brand_guidelines.pdf    Bodhi Tech Brand Guidelines 2024
```

## Reading the code

Every source file opens with a header that says what it is for and what will
bite you. Beyond that, three conventions worth knowing before you start
editing:

**Comments say why, not what.** `display: flex` does not need a comment. The
reason a value is `0.62` and not `0.5`, or why a rule has to match two
selectors instead of one, does. Where a comment exists it is usually because
something cost an hour to work out, and it says so.

**Stylesheets are ordered, not alphabetised.** `site.css` runs in three parts:
tokens and components, then motion, then odds and ends. Part 2 is meant to
override part 1. Moving a rule between parts changes which one wins.

**The 24 subpages are generated.** Editing them directly is wasted work; the
next `python3 build/build.py` overwrites it. Change `build/content.py` for
words and `build/blocks.py` for markup. `index.html` is the exception: it is
hand-written and the builder never touches it.

## Subpages reuse home-page components

No parallel design system was introduced. Every subpage section is built from a
component the home page already defines, so a style change in `css/site.css`
updates all 25 pages at once:

| Subpage section | Component reused |
|---|---|
| Offerings, solution cards, brand values | `.service-bento-card` in a `.bento-grid` |
| Our Approach / process steps | `.approach-step-card` in the `.approach-timeline-wrap`, with the flowing SVG connectors, node pulse and 1-2-3-4 highlight loop |
| Client Success Stories | the `.case-accordion-*` filmstrip, with the selector pills and sliding coverflow track |
| Blog listings, "keep reading" rows | `.blog-card` in a `.listing-grid` |
| Testimonials | `.testimonial-bento-card` in a `.tst-masonry` |
| Stat bands | `.counter-block` in `.counter-blocks`, with the count-up |
| FAQ | `.faq-item` in `.faq-flow` |
| Section headings | `.section-header` / `.section-tag` / `.section-title` |

Genuinely new pieces live in `css/pages.css`: the subpage hero, breadcrumbs, the
challenge/solution cards, case result tiles, the pillar cards, the article and
legal prose layout, and the CTA band.

## Subpage hero variants

`B.page_hero(..., variant=...)` picks a masthead to suit the section, so the 24
pages are not all the same slab:

| Variant | Pages | What it is |
|---|---|---|
| `split` | 6 solution pages, About Us | Brand gradient, text left, leaf-cropped photo right with a floating stat chip |
| `showcase` | Client Stories | Four client tiles woven into an offset mosaic, each with its headline number |
| `photo` | 3 industry pages | Full-bleed photograph under a warm scrim |
| `case` | 4 case studies | Dark masthead carrying the client mark and the results band |
| `article` | 3 blog posts | White, author/date/read-time row, wide cover bleeding into the body |
| `light` | Solutions / Industries / Blog indexes | Soft cream, wide and calm |
| `minimal` | Contact, Privacy, Terms | Short and plain |

On `split`, `photo` and `case` the primary CTA switches to the secondary orange,
because the primary brown sits almost on top of those backgrounds.

## The leaf shape

The guidelines (p.21 and p.23) define one shape for buttons, image frames,
badges and dots: the Bodhi leaf, which rounds on the **top-left / bottom-right
diagonal only**. The other two corners are a true point, not a small radius.
Measured off the guideline artwork:

| Element | Guideline | Token |
|---|---|---|
| Image mark | 1:1 box, 38% corner | `--radius-leaf-lg: 38% 0 38% 0` |
| Button | corner = 0.35 x its own height | `--radius-leaf-md: 20px 0 20px 0` (on the 58px button) |
| Small badge | same diagonal, smaller | `--radius-leaf-sm: 14px 0 14px 0` |

`--radius-leaf-lg` is a percentage, so it only belongs on a 1:1 box. On a wide
box the percentage stretches into a flat ellipse, which is why `.article-cover`
(21:8) carries an explicit pixel value instead.

A few home-page pieces were drawn on the mirrored diagonal (rounded top-right,
rounded bottom-left). Those were flipped to match: the ribbon icon badge, the
fanned deck cards and the hero chip mark.

## No emoji, and no // separators

Emoji read as machine-written, so none appear anywhere in the UI. The brand
guidelines already prescribe the replacement (p.14): *"icons are made with
light line strokes and are typically created in any brand colour other than
black... a 1-pt stroke weight."*

`build/blocks.py` holds `ICON_SET`, 28 named line-art marks drawn to that
spec. They carry no colour of their own, only `currentColor`, so each one
picks up whatever brand colour its container sets. `ICON_KEYWORDS` picks an
icon from the card's own subject rather than its position in the grid, most
specific rule first, matching on word boundaries so "Workshops" does not
match "shop".

The literal `//` separators are gone too:

| Was | Now |
|---|---|
| `// Verified Client Reputation` | `Verified Client Reputation` (the rule before it is drawn in CSS) |
| `01 // BUSINESS CONSULTATION` | `01` in the accent orange, then the label |
| `Boobobutt // Kids Marketplace` | client name, a short rule, then the sector |

Two typographic marks are deliberately kept, because they are not emoji and
read as ordinary UI: the `★` in the five-star ratings, and the `✓` in the
feature lists.

## The hero scrub and window width

The scrub's rightward travel was derived entirely from the deck, which is
capped at `min(1100px, 100%)`, so it took no account of how much window there
actually was. Between roughly 1024px and 1330px wide the outermost card
finished past the right edge and was clipped, on a fresh load as well as after
a resize. `apply()` now works out how much travel the window can hold and
scales only the horizontal spread, so the cascade keeps its vertical rhythm
and simply sits tighter on a narrower screen. Above about 1330px nothing
changes.

The 768px cutoff used to be read once, at load:

```js
if (window.matchMedia("(max-width: 768px)").matches) return;
```

So opening the page narrow and then widening the window left the scrub dead
for the rest of the session, over a hero still 2100px tall, and opening it
wide and then narrowing left it running with desktop geometry. It is a live
`matchMedia` now, checked inside `apply()`, and the existing not-scrubbing
branch puts everything back to its plain state.

Verified at every width from 390px to 2000px, and resizing in both directions
across the cutoff.

### Below 768px: the same animation, unpinned

Narrow screens used to get nothing at all, because pinning the page for two
screens of scrolling is unpleasant on a phone. They now run `applyNarrow()`,
which plays the same choreography (fan, collapse to one stack, cascade right)
driven by how far the hero has scrolled up the screen rather than by pinning.
Progress runs from 0 at the top of the page to 1 after about half a screen, so
it completes while the deck is still in view, and the scroll is never taken
away from the visitor. The heading and copy are left alone, because on a small
screen they are the thing worth reading.

Two things this depends on:

- **`is-scrub` must be on.** All that class does is `transition: none` on the
  cards. Without it each frame sets a target the cards never reach through
  their own 0.85s transition, so they barely move. It is switched on as soon
  as scrolling starts, and stays off at the very top so the load-time fan-out
  still animates.
- **`.hero-section` must clip horizontally below 768px.** The cascade pushes
  the cards past the right edge, and without clipping the whole page could be
  dragged sideways.

## On a phone

Every scroll animation runs on a phone exactly as it does on a desktop: the
word-by-word heading reveals, the card stagger, the container reveals, the
Our Approach step reveal and the tech scatter are all driven by
IntersectionObserver, which does not care about screen width. Verified by
scrolling each page top to bottom at 390px.

Two things are deliberately desktop-only, and both would be worse on a phone:
the pinned hero scroll-scrub (it hijacks the scroll), and the SVG connectors
between the Our Approach steps (the zig-zag means nothing once the cards are
in one column).

These phone defects were fixed:

| Was | Now |
|---|---|
| The Client Stories card kept its desktop height with its contents absolutely positioned inside, so the copy, the figures and the buttons were cut off. The active panel also inherited `flex: 0 0 min(660px, 74vw)`, which a **column** flex container reads as a height, pinning every card to 288px. | The card flows and grows to fit. The vertical spine is dropped, the pills scroll sideways with the active one kept in view, and the buttons stack full width. |
| The section only auto-advanced above 992px, so a phone showed one story and no way to know the others existed. | It advances on a phone too. Touch pauses it for 4 seconds the way hover pauses it on a desktop, and a sideways swipe moves between stories. |
| The contact bento had no phone rule at all, so it stayed a two-column grid inside an `overflow: hidden` box and the entire form sat off the right edge, invisible. | It stacks, form first, with single-column fields. |
| All five hero badges are positioned as percentages of an 1100px deck, so at phone width they landed on top of each other and clipped. | Two are kept and moved clear of the fan. |
| The chat greeting sat over the page for as long as the page was open. | It retires after 7 seconds, and below 560px the button speaks for itself. |
| Card links were 22-25px tall. | 44px on phones, without moving the text. |
| `.blogs-grid` was a hard `repeat(3, 1fr)` with no breakpoint at all, so on a 360px phone the three cards sat side by side in 82px columns, one word per line. | Two columns at 1000px, one at 700px, with a shorter cover image and tighter padding once it is single-column. |
| `.expanded-metrics-grid` only paired up below 420px, so between 421 and 560 three stat columns fell under 100px and the labels broke across three lines. | The pair-up moves to 560px, third box on its own row. |
| `.approach-steps-grid` held four fixed columns down to 992px, so a 1000-1140px laptop got 140px cards. | Two columns below 1140px, connectors hidden and the 58px stagger removed so the columns line up. Unchanged above that. |
| The contact sidebar's 44px side padding plus the pillar icon left the pillar copy about 18 characters wide at 360px. | Padding and icon gap tighten below 620px. |

## What Our Partners Say

The section is defined once, in `partials/testimonials.html`, which was
extracted verbatim from `index.html`. `B.testimonials_section()` returns that
file, so a subpage cannot drift from the home page: same heading block, same
4.9/5 and NPS trust pills, same six cards with their client logos and metric
pills. The only substitution is the CTA target, `__CTA__`, which the home page
points at its in-page contact block and every subpage points at
`contact-us.html`.

`index.html` still holds the markup inline, because it is not generated by the
build. The footer is handled the same way: `partials/footer.html` is spliced
into `index.html` verbatim. If either is edited in `index.html`, re-extract or
re-splice so the two stay in step.

## Client Stories: the motion layer

The accordion behaves as before (pills, hover, click, auto-advance) with four
additions, in `js/site.js` and the block at the foot of `css/site.css`:

1. **Dwell bar.** A 3px bar fills across the active pill. It is driven by the
   same clock that advances the panel, so the bar and the switch cannot drift
   apart. It pauses while the pointer is inside the section or a pill has
   keyboard focus.
2. **Parallax.** The panel photograph translates about 26px as the section
   crosses the viewport. It is scaled to 1.12 to give the translate somewhere
   to go, so the photo never pulls away from the panel edge.
3. **Count-up.** Each metric figure counts from zero when its panel opens, and
   the exact original text is written back at the end. The parser keeps any
   prefix and suffix, so `$3M`, `>1,000`, `<0.9` and `+256` all animate only
   their digits.
4. **Staggered reveal.** Brand pill, sector tag, headline, copy, each metric
   box and each button fade up in sequence, 90ms to 610ms.

One `requestAnimationFrame` loop drives all of it, and an IntersectionObserver
stops that loop while the section is off screen. Everything is skipped under
`prefers-reduced-motion`: no auto-advance, no parallax, no count-up, contents
shown at once.

## Animation

Subpages use the same vocabulary as the home page, driven by the same engine:

- `.section-title` splits into words and reveals on scroll, automatically.
- `.page-title` (the subpage hero heading) gets the same treatment from `js/pages.js`.
- Card grids stagger via `.anim-rise` + `.in`, applied by the `RISE_GROUPS` table.
- Container reveals (`.feat-list`, `.faq-flow`, `.counter-blocks`, `.tst-masonry`)
  add `.in` when they scroll into view.

Three small changes were made to the engine so it works on subpages:

1. `RISE_GROUPS` and the container-reveal list now use `querySelectorAll`
   instead of `querySelector`. Previously only the first matching container on a
   page animated, which was fine for the home page but broke subpages that hold
   several grids of the same kind.
2. Subpage container selectors were added to `RISE_GROUPS`.
3. The Our Approach reveal (section 5b) also moved to `querySelectorAll`, so a
   process longer than four steps arms and reveals each row on its own scroll
   position.

### Our Approach with more than four steps

The home page hardcodes four step cards in one row, with one absolutely
positioned connector overlay and nth-child rules driving the zig-zag and the
node pulse. Longer processes are chunked into balanced rows (seven steps read as
4 + 3, six as 3 + 3), each row in its own `.approach-row` so its overlay
positions against that row and the nth-child rules reset. Connector paths are
generated to match the column count using the same geometry as the
hand-authored four-card version.

Both halves of the reduced-motion handling (the CSS media query and the JS
`REDUCE` short-circuit) are untouched and still apply.

## Regenerating the subpages

```bash
python3 build/build.py
```

- `build/content.py` - page copy, case study data, testimonials, solutions, industries
- `build/articles.py` - blog article and legal page bodies
- `build/blocks.py` - section builders that emit the home page's components
- `build/build.py` - assembles and writes each page

Edit `partials/header.html` once and re-run the build to update the nav on all
24 subpages. `index.html` is not regenerated by the build, so a nav change needs
to be pasted into it too, or re-applied the way it was this time.

You can also edit the generated `.html` files directly, but a rebuild will
overwrite those edits.

## Before going live

- **Images are hot-linked** to `bodhitech.com.au/wp-content/` and to Unsplash.
  Download them into a local `img/` folder if this will be hosted elsewhere.
- **The contact form is front-end only.** It fakes a success state. Wire it to
  your form handler or CRM.
- **`cookies.txt` and `confirm.txt`** are empty leftovers from a curl session,
  both committed to the repo. They can be deleted.
- Phone number is `+61 485 980 712` and the address is 470 St Kilda Road,
  Melbourne, matching the live site. The older `+61 405 500 551` was replaced.

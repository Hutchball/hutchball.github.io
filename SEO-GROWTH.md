# Cake Squared organic growth plan

Audit and implementation: 17 October 2026. Scope: all ten sitemap URLs and the legacy DotBop redirect. Changes retain the visual identity, assets and static delivery; no paid services or tracking scripts added.

## Problems reported before implementation

- App-page H1s were often slogans rather than app names and purposes; feature cards skipped from H1 to H3. Setup and privacy headings also needed clearer hierarchy.
- Existing titles, descriptions, canonicals and Open Graph tags were present and unique. Improvements concern relevance and clarity, not missing metadata. BrainDump shared the generic brand social image.
- Naming differed from the owner's supplied current names (WageWatcher, AppTrackr, BrainDump). Apple still lists Wage Watcher and AppTrack.er: retain their working destination URLs and recommend aligning store names separately.
- SoftwareApplication schema already existed for five published apps; no standalone organisation/site identity or breadcrumb schema. BrainDump is unreleased and should not imply install availability.
- App pages mostly sent visitors back to the homepage; relevant cross-app navigation and an explicit catalogue route were limited. Top download buttons and official screenshot rails already existed; lower-page download links also already existed.
- Homepage and catalogue repeat the same app cards, but have different introductions and purposes. Retain both for now; inspect Google's canonical choices before deciding whether consolidation is warranted.
- No verified search baseline, query volumes, keyword difficulty, download attribution or field Core Web Vitals was available. These are measurement gaps, not evidence of poor rankings.

Initial live checks: all ten sitemap URLs, robots.txt and sitemap.xml returned HTTP 200. No HTML or HTTP-header noindex found. HTTP and www homepage requests resolved to https://cakesquared.co.uk/. DotBop returned HTML with an immediate meta refresh and correct DotBot canonical; this is not a server-side 301. No broken local references found during implementation.

## Keyword strategy

These are intent hypotheses, not measured volume, difficulty or ranking estimates. UK English throughout. Prioritise qualified visitors who want the existing app, then refine using actual queries and conversions.

| Page | Primary phrase | Secondary phrases | Evidence and boundaries |
| --- | --- | --- | --- |
| DotBot | learn Morse code | Morse code game; Morse code for beginners; Morse code learning app; Apple Watch Morse code | Existing lessons, rescue game and haptics; do not claim suitability specifically for children without product validation. |
| WageWatcher | live earnings calculator | Apple Watch earnings tracker; real-time wage calculator; salary per second; hourly pay tracker | Listing confirms estimated live earnings and hourly/annual settings. Not a take-home-pay or tax calculator; salary-per-second intent needs query testing. |
| AppTrackr | app idea organiser | app development tracker; app project planner; development notes app; app release planner | Existing projects, stages, tasks and notes. Defer AI app development notes as a target: no verified AI feature. |
| BrainDump | quick thought capture | brain dump app; capture ideas quickly; thought capture app; organise ideas later | Preview-stage target only; no download URL or SoftwareApplication install claim. Defer ADHD-friendly positioning until tested and supported. |
| Jim Bro | fitness instructor timer | gym class timer; workout music timer; workout and recovery timer; Apple Music workout controls | Existing timer and music controls; no new workout modes claimed. |
| InterludeRadio | radio static sounds app | radio tuning sounds; sounds between songs; live performance changeover sounds; radio sound effects for live shows | Apple description confirms static, tuning and PA use. Broad radio searches largely concern station streaming, so avoid that intent. |

InterludeRadio research: live searches for the exact name and radio-tuning/live-performance terms found its Apple listing and predominantly unrelated streaming-radio results for broader terms. This supports precise positioning, not a claim of demand. Official description: https://apps.apple.com/gb/app/interluderadio/id6811347236. All five published app IDs were checked against Apple's GB lookup endpoint before changes. Existing site content supplies the detailed features and screenshots; no new capabilities were introduced.

## Implemented

- Refined six app-page titles, descriptions, H1s and introductory copy; kept Open Graph and app JSON-LD descriptions in sync.
- Added descriptive feature H2s, preserved H3s inside FAQ/plans sections and corrected setup/privacy hierarchy. CSS keeps the existing card heading appearance.
- Used owner-specified app names consistently in visible copy and structured data, preserving URLs and the DotBop redirect.
- Added Organization and WebSite on the homepage, plus BreadcrumbList and visible breadcrumb navigation on app and setup pages. Catalogue/privacy breadcrumb schema uses existing homepage links.
- Preserved SoftwareApplication for the five published apps; corrected InterludeRadio's category to UtilitiesApplication to match Apple. No invented offers, prices, ratings, reviews or statistics. Schema validity does not mean eligibility for Google's software-app rich results; required commercial/review evidence is deliberately not fabricated.
- Added catalogue and related-app footer links, kept existing top and bottom App Store CTAs, and made WageWatcher's horizontal screenshot rail keyboard focusable.
- Gave BrainDump its own social icon; retained its coming-soon status and linked available apps.
- Added repeatable offline SEO validation in `scripts/validate_seo.py`; preserved existing robots.txt, sitemap.xml and legacy redirect because they were already correct.

## Conversion recommendations and approval-dependent follow-up

Top CTAs are already next to the app explanation. Keep screenshot rails and lower-page downloads, and measure whether mobile visitors reach them before adding sticky controls. Existing real screenshots are preferable to invented mockups. Consider testing benefit-specific screenshot captions and the first screenshot after establishing a baseline; no new screenshots or redesign are required now.

Owner action/approval needed: align App Store listing names with the website names; supply App Store Connect campaign links/tokens for acquisition attribution; confirm BrainDump release details and any ADHD positioning before publication. No approval is needed for the implemented static changes. No analytics, cookies, email capture, pop-ups or third-party paid tools introduced.

## Measurement and external tools

1. Export the last 28 days of Search Console performance by page and query: impressions, clicks, CTR and average position, with UK/device splits. Record launch date. Compare the next 28 days and a longer 8–12 week window, accounting for low traffic, indexing lag and seasonality.
2. Use URL Inspection for changed app pages and Google's selected canonicals; request recrawling where useful. Sitemap is already submitted; no routine resubmission needed while URLs are unchanged. Ten discovered URLs does not establish ten indexed pages.
3. Run Google's Rich Results Test and Schema.org Validator against deployed pages. Local checks verify JSON parsing, types, key fields, breadcrumb order and URL consistency; external validators were not run. Do not promise software-app rich results without required genuine evidence.
4. Review Search Console Core Web Vitals and PageSpeed Insights on mobile. Responsive browser checks are not field performance or battery measurements.
5. In App Store Connect, compare website-referred product-page views, first-time downloads and conversion rate by app, using campaign attribution if available. Search Console clicks measure Google-to-site visits, not App Store clicks or installs. Without approved outbound-event measurement, exact on-site App Store CTR is unknown.
6. Adjust titles/copy based on relevant impressions and download outcomes. Do not judge success by an arbitrary SEO score, or claim ranking gains before Search Console supports them.

## References

- [Google SEO starter guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Title links](https://developers.google.com/search/docs/appearance/title-link)
- [Software app structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- [Site names](https://developers.google.com/search/docs/appearance/site-names)
- [Canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Redirects, including instant meta refresh](https://developers.google.com/search/docs/crawling-indexing/301-redirects)
- [Schema.org SoftwareApplication](https://schema.org/SoftwareApplication)
- [Schema.org BreadcrumbList](https://schema.org/BreadcrumbList)

## Validation and files

Offline validator passes for ten canonical sitemap pages, eleven HTML files and 224 internal URL/asset/fragment references. Titles are unique, each canonical page has one H1, metadata matches, JSON-LD parses and breadcrumb positions/URLs agree. No new JavaScript or runtime dependency added to the website. Browser checks cover all ten pages at widths 320, 390, 768 and 1440 pixels, including image decoding and document overflow. Mobile screenshots were visually reviewed. This is not a physical-device accessibility audit or a measured Core Web Vitals result.

Modified: `index.html`, `apps/index.html`, `dotbot.html`, `wage-watcher.html`, `app-track.html`, `brain-dump.html`, `jim-bro.html`, `interlude.html`, `wage-watcher-setup.html`, `privacy-policy.html`, `style.css`, `README.md`. Added: `SEO-GROWTH.md`, `scripts/validate_seo.py`. Existing `dotbop.html`, `robots.txt`, `sitemap.xml`, asset files and App Store destination URLs are preserved.

Screenshot follow-up: DotBot's supplied App Store artwork still visibly says “DotBop”, and AppTrackr artwork shows the earlier app name. These existing assets were preserved. Supply current official screenshots to remove the remaining visual naming mismatch; avoid editing UI images to imply a shipped version that has not been verified.

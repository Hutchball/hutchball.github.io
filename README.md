# Cake Squared website

Static website for cakesquared.co.uk. The root homepage and `/apps/` share the new Apps design in `home.css`. App details, the setup guide and privacy policy use `style.css`.

Preview from this directory with `python3 -m http.server 8000`, then open http://localhost:8000. No build step or JavaScript runtime is needed.

## Design and iOS development references

Use accessible layouts, readable typography, visible keyboard focus, generous touch targets and reduced motion. Keep website effects lightweight and avoid continuous decorative animations.

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [Apple Design Resources](https://developer.apple.com/design/resources/)
- [Getting started with Apple design](https://developer.apple.com/design/get-started/)
- [Apple design updates](https://developer.apple.com/design/whats-new/)
- [Apple design tips](https://developer.apple.com/design/tips/)
- [The Swift Programming Language](https://docs.swift.org/swift-book/)
- [SwiftUI](https://developer.apple.com/documentation/swiftui/)
- [UIKit](https://developer.apple.com/documentation/uikit/)
- [AppKit for macOS](https://developer.apple.com/documentation/appkit/)
- [API design guidelines](https://developer.apple.com/documentation/apple_sdk_guidelines/api-design)
- [Accessibility](https://developer.apple.com/accessibility/)
- [Performance](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)
- [Energy efficiency](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/)

## Search indexing and maintenance

`sitemap.xml` lists the ten public canonical HTML pages, including the distinct `/apps/` directory and the BrainDump app page. Index-file aliases are excluded. No `lastmod` values are supplied because reliable content modification dates are not maintained. `robots.txt` allows crawling and declares the sitemap. GitHub Pages serves both files directly from the repository root.

Keep each page's canonical, title, description, Open Graph metadata and app structured data aligned when editing it. Add new indexable pages to the sitemap; exclude redirects, duplicate aliases and noindex pages. App structured data describes existing features without inventing ratings, reviews or prices; rich-result eligibility is not guaranteed.

DotBot uses `/dotbot.html`, renamed asset paths and the current App Store URL. The legacy `/dotbop.html` page contains an instant meta refresh and canonical pointing to `/dotbot.html`; it is excluded from the sitemap. GitHub Pages serves static HTML, so this is a browser redirect rather than an HTTP 301. Google treats zero-second meta refresh redirects as permanent: [redirect guidance](https://developers.google.com/search/docs/crawling-indexing/301-redirects). Keep the legacy redirect to preserve existing inbound links.

Validation: parse sitemap XML, check unique metadata and self-canonicals, validate structured JSON, check every local link/image/fragment, then verify all ten public URLs plus sitemap and robots return HTTP 200 after deployment. Responsive viewport tags, existing mobile breakpoints, reduced-motion rules and CSS are preserved; this is not a measured Core Web Vitals audit.

The sitemap is already submitted in Google Search Console. Monitor indexing after deployment; resubmit only if needed.

Useful authoritative references:

- [Google: build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: software application structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- [Google: mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- [Apple: testing performance with Instruments](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)
- [Swift concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)

## Organic growth maintenance

See [SEO-GROWTH.md](SEO-GROWTH.md) for the audit, per-app keyword hypotheses, implementation boundaries and Search Console/App Store measurement plan. Run `python3 scripts/validate_seo.py` from the repository root before publishing. The sitemap has already been submitted; monitor indexing rather than routinely resubmitting an unchanged sitemap.

Further iOS engineering references:

- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance): reduce expensive view work and unnecessary updates.
- [SwiftUI accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals): expose useful labels, values and actions with native controls.

Use native platform behaviour, accessible text and controls, and measured performance work to guide iOS development. Profile before optimising; minimise repeated background work and unnecessary view updates to protect responsiveness and battery life.

## PageSpeed improvements (19 October 2026)

All rendered logos and app icons use responsive WebP assets with explicit HTML dimensions. Original PNG/JPEG artwork remains available for social metadata and future exports. The six homepage icons total 68,502 bytes at 280px versus 1,889,276 bytes for the originals (96.4% smaller). Browsers choose an appropriate candidate using `srcset` and `sizes`; actual transfer sizes depend on screen density. Regenerate with `python3 scripts/optimise_images.py` using Pillow, then update HTML filenames if the generated content hashes change. Review artwork after compression.

Manrope is self-hosted as one 24,836-byte Latin variable WOFF2, preloaded with `crossorigin` and rendered with `font-display: swap`. It replaces the Google Fonts stylesheet, preconnects and remote font requests. Source: [Fontsource Manrope](https://fontsource.org/fonts/manrope); redistribution licence is in `assets/fonts/Manrope-OFL.txt`. Use a wider character subset if new languages require it. CSS URLs have a new version to refresh existing caches.

The Coming soon badge uses `#465166` on `#e9edf3`, meeting WCAG AA normal-text contrast. Existing styling, content and SEO metadata are retained.

### Hosting and cache lifetimes

This repository is configured for GitHub Pages. Its HTTP cache lifetimes are controlled by the hosting service, not HTML or CSS. No ineffective `_headers` or `.htaccess` file has been added. Smaller images reduce both first-load cost and the bytes affected by the short-cache warning. Generated images and the local font have content hashes, ready for long caching if a configurable hosting/CDN layer is introduced. On such a host, use `Cache-Control: public, max-age=31536000, immutable` only for content-hashed files; keep HTML revalidated and avoid applying immutable caching indiscriminately to original assets. Hosting/CDN changes are a separate deployment task.

Validation: existing SEO validator passes. Local Chrome checks at 390px and 1280px verify homepage, app listing, Jim Bro detail and WageWatcher setup: no horizontal overflow, missing dimensions, failed image loads or Google Fonts requests; Manrope loads successfully. Mobile homepage screenshot visually reviewed. Run PageSpeed Insights again after publishing; no new live score is claimed.

Further performance references:

- [Google: properly size images](https://developer.chrome.com/docs/lighthouse/performance/uses-responsive-images/)
- [Google: web font loading](https://web.dev/articles/optimize-webfont-loading)
- [Google: HTTP caching](https://web.dev/articles/http-cache)
- [Chrome DevTools: contrast](https://developer.chrome.com/docs/devtools/accessibility/contrast)

## BrainDump App Store launch (20 October 2026)

BrainDump is available on the App Store. The homepage and app directory lead with BrainDump, WageWatcher, then DotBot. BrainDump copy focuses on capturing day-to-day thoughts, revisiting them later and choosing what to bin or keep, including its usefulness for people with ADHD. Keep download links and metadata aligned with the detail page.

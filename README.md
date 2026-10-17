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

`sitemap.xml` lists the ten public canonical HTML pages, including the distinct `/apps/` directory and the Brain Dump coming-soon page. Index-file aliases are excluded. No `lastmod` values are supplied because reliable content modification dates are not maintained. `robots.txt` allows crawling and declares the sitemap. GitHub Pages serves both files directly from the repository root.

Keep each page's canonical, title, description, Open Graph metadata and app structured data aligned when editing it. Add new indexable pages to the sitemap; exclude redirects, duplicate aliases and noindex pages. App structured data describes existing features without inventing ratings, reviews or prices; rich-result eligibility is not guaranteed.

DotBot is the current name supplied by the project owner. The existing `/dotbop.html` URL, lowercase asset paths and App Store URL are preserved. The App Store listing still displayed DotBop during this audit, and existing screenshot artwork may retain that name; align those assets and the store listing during the app rebrand.

Validation: parse sitemap XML, check unique metadata and self-canonicals, validate structured JSON, check every local link/image/fragment, then verify all ten public URLs plus sitemap and robots return HTTP 200 after deployment. Responsive viewport tags, existing mobile breakpoints, reduced-motion rules and CSS are preserved; this is not a measured Core Web Vitals audit.

Submit https://cakesquared.co.uk/sitemap.xml manually in Google Search Console → Indexing → Sitemaps after deployment.

Useful authoritative references:

- [Google: build and submit a sitemap](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: canonical URLs](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google: software application structured data](https://developers.google.com/search/docs/appearance/structured-data/software-app)
- [Google: mobile-first indexing](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing)
- [Apple: testing performance with Instruments](https://developer.apple.com/documentation/xcode/improving-your-app-s-performance)
- [Swift concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/)

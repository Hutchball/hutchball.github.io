"""Offline checks for canonical pages, metadata, JSON-LD and local links. Run from repo root."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://cakesquared.co.uk'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.tags = []; self.json = []; self.current = None; self.title = ''; self.in_title = False
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs); self.tags.append((tag, a))
        if tag == 'title': self.in_title = True
        if tag == 'script' and a.get('type') == 'application/ld+json': self.current = ''
    def handle_data(self, data):
        if self.in_title: self.title += data
        if self.current is not None: self.current += data
    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False
        if tag == 'script' and self.current is not None:
            self.json.append(json.loads(self.current)); self.current = None

urls = [n.text for n in ET.parse(ROOT / 'sitemap.xml').iter() if n.tag.endswith('loc')]
assert len(urls) == len(set(urls)) == 10
pages = {p: Page(p.read_text()) for p in ROOT.rglob('*.html') if '.git' not in p.parts}
titles = []
for url in urls:
    path = urlsplit(url).path
    p = ROOT / (path.lstrip('/') + 'index.html' if path.endswith('/') else path.lstrip('/'))
    page = pages[p]; titles.append(page.title)
    canon = [a['href'] for t,a in page.tags if t == 'link' and a.get('rel') == 'canonical']
    assert canon == [url], (p, canon)
    assert len([1 for t,a in page.tags if t == 'h1']) == 1, p
    for key in ['description','viewport']:
        assert len([a for t,a in page.tags if t == 'meta' and a.get('name') == key and a.get('content')]) == 1, (p,key)
    meta = {a.get('property'): a.get('content') for t,a in page.tags if t == 'meta'}
    assert meta['og:title'] == page.title
    assert meta['og:url'] == url
    assert all(meta.get(k) for k in ['og:description','og:image','og:image:alt','og:locale'])
    assert not any('noindex' in a.get('content','').lower() for t,a in page.tags if t == 'meta' and a.get('name','').lower() in ['robots','googlebot'])
    for d in page.json:
        assert d['@context'] == 'https://schema.org'
        if d.get('@type') == 'SoftwareApplication':
            assert d['url'] == url and d['name'] and d['operatingSystem'] and d['applicationCategory']
            assert d['installUrl'].startswith('https://apps.apple.com/')
            assert not any(k in d for k in ['aggregateRating','review','offers','downloadCount'])
        if d.get('@type') == 'BreadcrumbList':
            items = d['itemListElement']
            assert [x['position'] for x in items] == list(range(1,len(items)+1))
            assert items[-1]['item'] == url
assert len(titles) == len(set(titles)), 'Duplicate titles'
links = 0
for p,page in pages.items():
    for tag,a in page.tags:
        if tag == 'img': assert 'alt' in a, (p,a)
        for key in ['href','src']:
            if key not in a: continue
            u = urlsplit(a[key])
            if u.scheme and u.scheme not in ['http','https']: continue
            if u.netloc and u.netloc != 'cakesquared.co.uk': continue
            assert u.scheme != 'http', (p,a)
            target = ROOT / unquote(u.path.lstrip('/')) if u.path.startswith('/') else p.parent / unquote(u.path) if u.path else p
            if target.is_dir(): target /= 'index.html'
            assert target.exists(), (p,a,target)
            if u.fragment and target.suffix == '.html':
                assert any(b.get('id') == unquote(u.fragment) for t,b in pages[target.resolve()].tags), (p,a)
            links += 1
legacy = (ROOT / 'dotbop.html').read_text()
assert 'content="0; url=https://cakesquared.co.uk/dotbot.html"' in legacy
assert BASE + '/dotbop.html' not in urls
assert 'Allow: /' in (ROOT / 'robots.txt').read_text()
assert 'Sitemap: '+BASE+'/sitemap.xml' in (ROOT / 'robots.txt').read_text()
print(f'PASS: {len(urls)} sitemap pages, {len(pages)} HTML files, {links} internal references; metadata, JSON-LD and legacy redirect.')

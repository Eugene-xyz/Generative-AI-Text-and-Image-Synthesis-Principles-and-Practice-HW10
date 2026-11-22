"""Final local-file checks after documentation is rebuilt; no browser claims."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from datetime import datetime, timezone, timedelta
import hashlib
import json
import re
import argparse

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.ids = [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        self.links.extend(values[k] for k in ('href', 'src') if values.get(k))
        if values.get('id'):
            self.ids.add(values['id'])


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('--output', default='reports/checks/artifact-integrity-latest.json')
    output = (ROOT / args.parse_args().output).resolve()
    if not output.is_relative_to(ROOT):
        raise ValueError('Output must stay inside HW10')
    manifest = json.loads((ROOT / 'reports/build-manifest.json').read_text(encoding='utf-8'))
    generated = ['index.html', 'slides/index.html'] + manifest['reader_pages']
    parsed = {f: Links((ROOT / f).read_text(encoding='utf-8')) for f in generated}
    missing, count = [], 0

    def verify(origin, url, anchors=False):
        nonlocal count
        part = urlsplit(url)
        if part.scheme or part.netloc:
            return
        count += 1
        target = (origin.parent / unquote(part.path)).resolve() if part.path else origin
        if target == output:
            return  # This result is written at the end of the run.
        if not target.exists():
            missing.append({'from': str(origin.relative_to(ROOT)), 'target': url})
        elif anchors and part.fragment and target.suffix == '.html':
            key = target.relative_to(ROOT).as_posix()
            doc = parsed.get(key) or Links(target.read_text(encoding='utf-8'))
            if unquote(part.fragment) not in doc.ids:
                missing.append({'from': str(origin.relative_to(ROOT)), 'target': url, 'reason': 'anchor missing'})

    for name, document in parsed.items():
        for link in document.links:
            verify(ROOT / name, link, True)
    markdown_count = 0
    for p in ROOT.rglob('*.md'):
        if any(x in {'raw', 'site', '.git', 'node_modules'} for x in p.relative_to(ROOT).parts):
            continue
        markdown_count += 1
        text = re.sub(r'```.*?```', '', p.read_text(encoding='utf-8'), flags=re.S)
        for link in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)', text):
            verify(p, link.strip())

    before = json.loads((ROOT / 'reports/checks/html-before-delivery-2026-11-22.json').read_text(encoding='utf-8'))
    changed = sorted(f for f, old in before['hashes'].items() if sha(ROOT / f) != old)
    expected = ['assets/diagrams/slide-06-2.svg', 'assets/diagrams/slide-17-1.svg']
    input_match = (sha(ROOT / 'slides/content.md') == manifest['source_sha256']
                   and sha(ROOT / 'slides/source-map.md') == manifest['source_map_sha256'])
    passed = not missing and changed == expected and input_match
    result = {
        'checked_at': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
        'scope': 'Local generated HTML, anchors, Markdown links, source hashes; no browser rerun',
        'passed': passed, 'generated_html_pages': len(generated), 'markdown_pages': markdown_count,
        'local_links_checked': count, 'missing': missing,
        'changed_from_full_browser_pass': changed,
        'changed_diagrams_checked_in': 'html-2026-11-22/delivery-recheck/browser-results.json',
        'unchanged_deck_html_css_js': changed == expected,
        'build_matches_current_inputs': input_match,
        'artifact_sha256': {f: sha(ROOT / f) for f in before['hashes']},
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('checked_at', 'passed', 'generated_html_pages', 'markdown_pages', 'local_links_checked', 'missing', 'unchanged_deck_html_css_js')}, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())

"""Create traceable text derivatives; does not create or update the Wiki."""
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
import html
import json
from pathlib import Path
import re
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.output = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip += 1
        if not self.skip and tag in {"h1", "h2", "h3", "h4", "p", "div", "section", "article", "li", "br", "strong"}:
            self.output.append("\n")

    def handle_endtag(self, tag):
        if tag in {"script", "style", "svg", "noscript"}:
            self.skip = max(0, self.skip - 1)
        if not self.skip and tag in {"h1", "h2", "h3", "h4", "p", "div", "section", "article", "li", "strong"}:
            self.output.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.output.append(data)

    def lines(self):
        return [line for raw in "".join(self.output).splitlines() if (line := re.sub(r"\s+", " ", raw).strip())]


class ArticleSection(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.depth = 0
        self.fragments = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "section" and (self.depth or "story-detail-body" in attributes.get("class", "")):
            self.depth += 1
        if self.depth:
            self.fragments.append(self.get_starttag_text())

    def handle_endtag(self, tag):
        if self.depth:
            self.fragments.append(f"</{tag}>")
            if tag == "section":
                self.depth -= 1

    def handle_data(self, data):
        if self.depth:
            self.fragments.append(data)

    def handle_entityref(self, name):
        if self.depth:
            self.fragments.append(f"&{name};")

    def handle_charref(self, name):
        if self.depth:
            self.fragments.append(f"&#{name};")


def main():
    inventory = []
    for folder in sorted((ROOT / "raw").glob("S[0-9][0-9]")):
        receipt_path = folder / "retrieval.json"
        if not receipt_path.exists():
            continue
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        source = ROOT / receipt["local_path"]
        item = dict(receipt)
        item["review_status"] = "fetched_not_yet_ingested"
        if source.suffix == ".pdf":
            reader = PdfReader(source)
            if (folder / "pages.json").exists():
                pages = json.loads((folder / "pages.json").read_text(encoding="utf-8"))
            else:
                pages = [{"pdf_page": i + 1, "text": page.extract_text(extraction_mode="layout")} for i, page in enumerate(reader.pages)]
            (folder / "pages.json").write_text(json.dumps(pages, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            (folder / "text-by-page.txt").write_text("\n\n".join(f"===== PDF PAGE {page['pdf_page']} =====\n{page['text']}" for page in pages) + "\n", encoding="utf-8")
            item.update({"pdf_pages": len(pages), "pdf_metadata": {str(k): str(v) for k, v in (reader.metadata or {}).items()}, "extracted_characters": sum(len(p['text']) for p in pages)})
            print(f"{folder.name}: {len(pages)} PDF pages extracted", flush=True)
        else:
            original = source.read_text(encoding="utf-8")
            parser = VisibleText()
            parser.feed(original)
            (folder / "visible-text.txt").write_text("\n".join(parser.lines()) + "\n", encoding="utf-8")
            section = ArticleSection()
            section.feed(original)
            fivb_article = re.search(r'<article class="post[^\"]*"[^>]*>(.*?)</article>', original, re.S)
            article_html = "".join(section.fragments) or (fivb_article.group(1) if fivb_article else "")
            if article_html:
                parser = VisibleText()
                parser.feed(article_html)
                lines = parser.lines()
                (folder / "article.txt").write_text("\n".join(f"L{i:03}: {line}" for i, line in enumerate(lines, 1)) + "\n", encoding="utf-8")
                item["article_lines"] = len(lines)
            schemas = []
            for payload in re.findall(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>', original, re.S | re.I):
                try:
                    schemas.append(json.loads(payload))
                except json.JSONDecodeError:
                    pass
            item["embedded_schema"] = schemas
            print(f"{folder.name}: HTML visible text extracted; article lines={item.get('article_lines', 'requires selection')}", flush=True)
        inventory.append(item)
    output = ROOT / "reports" / "source-inventory.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps({"generated_at": datetime.now(timezone(timedelta(hours=8))).isoformat(), "sources": inventory}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

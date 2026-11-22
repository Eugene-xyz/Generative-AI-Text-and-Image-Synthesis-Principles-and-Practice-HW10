"""Structural/provenance checks for this Markdown Wiki; not factual validation."""
from argparse import ArgumentParser
from collections import deque
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json
import re
import sys

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]
WIKI = ROOT / "wiki"
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def metadata(text):
    if not text.startswith("---\n"):
        return {}
    block = text.split("---", 2)[1]
    result = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def local_links(path, text):
    for target in LINK.findall(text):
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        yield target, (path.parent / unquote(parsed.path)).resolve(), unquote(parsed.fragment)


def main():
    parser = ArgumentParser()
    parser.add_argument("--phase", choices=["preflight", "final"], default="final")
    parser.add_argument("--output", default="reports/checks/wiki-lint-latest.json")
    args = parser.parse_args()
    output = (ROOT / args.output).resolve()
    if not output.is_relative_to(ROOT):
        raise ValueError("Output must remain in HW10")

    errors = []
    files = sorted(WIKI.rglob("*.md"))
    texts = {p.resolve(): p.read_text(encoding="utf-8") for p in files}
    meta = {p: metadata(t) for p, t in texts.items()}
    source_files = {meta[p].get("id"): p for p in texts if p.parent.name == "sources"}
    topic_files = [p for p in texts if p.parent.name == "topics"]
    query_files = [p for p in texts if p.parent.name == "queries"]
    expected_ids = {f"S{i:02}" for i in range(1, 7)}
    if set(source_files) != expected_ids or len([p for p in texts if p.parent.name == "sources"]) != 6:
        errors.append("Expected exactly six distinct source pages, S01–S06")
    if len(topic_files) != 12:
        errors.append(f"Expected 12 approved topic pages, got {len(topic_files)}")

    graph = {}
    relative_count = 0
    page_counts = {}
    extra = [ROOT / "README.md", ROOT / "reports/workflow.md", ROOT / "reports/checks/ingest-2026-11-22.md"]
    scan = dict(texts)
    for p in extra:
        if not p.exists():
            errors.append(f"Missing report/entry: {p.relative_to(ROOT)}")
        else:
            scan[p.resolve()] = p.read_text(encoding="utf-8")
    for path, content in scan.items():
        graph[path] = set()
        if path in texts and path.name != path.name.lower():
            errors.append(f"Non-lowercase Wiki filename: {path.name}")
        for raw, dest, fragment in local_links(path, content):
            relative_count += 1
            if not dest.is_relative_to(ROOT):
                errors.append(f"Link escapes HW10: {path.name}: {raw}")
                continue
            if not dest.exists() and dest != output:
                errors.append(f"Broken link: {path.relative_to(ROOT)} -> {raw}")
                continue
            if dest in texts:
                graph[path].add(dest)
            if fragment and dest.suffix == ".pdf" and dest.exists():
                if not re.fullmatch(r"page=\d+", fragment):
                    errors.append(f"Unsupported PDF locator: {raw}")
                else:
                    if dest not in page_counts:
                        page_counts[dest] = len(PdfReader(dest).pages)
                    if not 1 <= int(fragment[5:]) <= page_counts[dest]:
                        errors.append(f"PDF page outside document: {raw}")
            elif fragment and dest in texts:
                anchors = set(re.findall(r'id=[\"\']([^\"\']+)', texts[dest]))
                for heading in re.findall(r"^#{1,6}\s+(.+)$", texts[dest], re.M):
                    anchors.add(re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-"))
                if fragment not in anchors:
                    errors.append(f"Missing Markdown anchor: {raw}")

    index = (WIKI / "index.md").resolve()
    seen = set()
    queue = deque([index])
    while queue:
        p = queue.popleft()
        if p in seen:
            continue
        seen.add(p)
        queue.extend(graph.get(p, set()) - seen)
    unreachable = sorted(str(p.relative_to(ROOT)) for p in texts if p not in seen)
    if unreachable:
        errors.append({"unreachable_from_index": unreachable})

    integrations = {}
    for sid, path in source_files.items():
        used_by = [p for p in topic_files if path in graph.get(p, set())]
        integrations[sid] = [p.relative_to(ROOT).as_posix() for p in sorted(used_by)]
        if not used_by:
            errors.append(f"Source not integrated into any topic: {sid}")
        for topic in used_by:
            if topic not in graph.get(path, set()):
                errors.append(f"Source integration list missing backlink: {sid} -> {topic.name}")
        if meta[path].get("status") not in ({"ingested"} if args.phase == "final" else {"in_review", "ingested"}):
            errors.append(f"Invalid source status: {sid}")
        for key in ["title", "updated"]:
            if not meta[path].get(key):
                errors.append(f"Source missing {key}: {sid}")
        for heading in ["## 來源與版本", "## 處理範圍", "## 重點與證據定位", "## 本次整合的 Wiki 頁面", "## 檢查與歷史"]:
            if heading not in texts[path]:
                errors.append(f"Source missing section {heading}: {sid}")

    for p in topic_files + query_files:
        for key in ["title", "status", "updated", "sources"]:
            if not meta[p].get(key):
                errors.append(f"Page missing {key}: {p.name}")
        declared = set(re.findall(r"S\d{2}", meta[p].get("sources", "")))
        cited = {sid for sid, sp in source_files.items() if sp in graph.get(p, set())}
        if not declared or declared != cited:
            errors.append(f"Source metadata/citations differ: {p.name}; declared={sorted(declared)}, cited={sorted(cited)}")
        if args.phase == "final" and meta[p].get("status") != "verified":
            errors.append(f"Final page not verified within declared scope: {p.name}")
        if index not in graph.get(p, set()):
            errors.append(f"Page has no return link to index: {p.name}")

    raw_checks = []
    for folder in [ROOT / "raw" / sid for sid in sorted(expected_ids)] + [ROOT / "raw/verification" / vid for vid in ["V01", "V02"]]:
        receipt = json.loads((folder / "retrieval.json").read_text(encoding="utf-8"))
        original = ROOT / receipt["local_path"]
        data = original.read_bytes()
        valid = len(data) == receipt["bytes"] and sha256(data).hexdigest() == receipt["sha256"]
        raw_checks.append({"id": folder.name, "sha256_and_bytes_match": valid})
        if not valid:
            errors.append(f"Raw snapshot mismatch: {folder.name}")
    directory_receipt = ROOT / "raw/verification/fivb-rules-index-2026-11-22.json"
    dr = json.loads(directory_receipt.read_text(encoding="utf-8"))
    directory_valid = sha256(directory_receipt.with_suffix(".html").read_bytes()).hexdigest() == dr["sha256"]
    if not directory_valid:
        errors.append("Official rules directory snapshot mismatch")

    registry = json.loads((ROOT / "reports/ingest-register.json").read_text(encoding="utf-8"))
    if {s["id"] for s in registry["sources"]} != expected_ids:
        errors.append("Ingest registry IDs differ from approved sources")
    for item in registry["sources"]:
        sid = item["id"]
        if sorted(item["integrated_topics"]) != integrations.get(sid, []):
            errors.append(f"Ingest registry integration map differs: {sid}")
        if item["status"] != meta[source_files[sid]]["status"]:
            errors.append(f"Ingest registry status differs: {sid}")
        if args.phase == "final" and f"| {sid} | 完成正式入庫" not in texts[(WIKI / "log.md").resolve()]:
            errors.append(f"Missing completed ingest log: {sid}")
    result = {
        "checked_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "phase": args.phase,
        "passed": not errors,
        "wiki_markdown_files": len(files),
        "source_pages": len(source_files),
        "topic_pages": len(topic_files),
        "query_pages": len(query_files),
        "relative_links_checked": relative_count,
        "unreachable_pages": unreachable,
        "source_topic_map": integrations,
        "raw_checks": raw_checks,
        "official_directory_sha256_matches": directory_valid,
        "errors": errors,
        "limits": "Structural and provenance checks only; content, conditions, figures and teaching quality require separate review."
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ["checked_at", "phase", "passed", "wiki_markdown_files", "source_pages", "topic_pages", "query_pages", "relative_links_checked", "errors"]}, ensure_ascii=False))
    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()

"""Verify source snapshots and the pre-ingest review package; no content grading."""
from datetime import datetime, timedelta, timezone
from hashlib import sha256
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote

from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def main():
    register = json.loads((ROOT / "reports/reading-register.json").read_text(encoding="utf-8"))
    checks = []
    for item in register["sources"] + register["supplemental_verification"]:
        receipt = json.loads((ROOT / item["receipt"]).read_text(encoding="utf-8"))
        original = ROOT / receipt["local_path"]
        data = original.read_bytes()
        result = {
            "id": item["id"],
            "path": receipt["local_path"],
            "sha256_matches_receipt": sha256(data).hexdigest() == receipt["sha256"],
            "bytes_match_receipt": len(data) == receipt["bytes"],
        }
        if original.suffix == ".pdf":
            result["pdf_magic_valid"] = data.startswith(b"%PDF-")
            result["pdf_pages"] = len(PdfReader(original).pages)
            result["page_count_matches_register"] = result["pdf_pages"] == item["total_pdf_pages"]
        else:
            result["html_document_present"] = "<html" in data.decode("utf-8").lower()
            lines = (original.parent / "article.txt").read_text(encoding="utf-8").splitlines()
            result["article_lines"] = len(lines)
            result["article_line_count_matches"] = len(lines) == {"S04": 33, "S05": 22, "S06": 27}[item["id"]]
        result["passed"] = all(value for value in result.values() if isinstance(value, bool))
        checks.append(result)

    report_paths = [ROOT / "reports/source-review.md", ROOT / "reports/checks/source-review-2026-11-22.md"]
    output = ROOT / "reports/checks/review-validation.json"
    missing_links = []
    relative_links_checked = 0
    for path in report_paths:
        content = path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if target.startswith(("https://", "http://", "#")):
                continue
            destination = (path.parent / unquote(target.split("#", 1)[0])).resolve()
            relative_links_checked += 1
            # This JSON is written by this run; it may not exist on the first run.
            if not destination.exists() and destination != output.resolve():
                missing_links.append({"report": str(path.relative_to(ROOT)), "target": target})

    statuses_valid = len(register["sources"]) == 6 and all(s["status"] == "in_review" for s in register["sources"])
    wiki_absent = not (ROOT / "wiki").exists()
    summary = {
        "checked_at": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "checks": checks,
        "relative_report_links_checked": relative_links_checked,
        "missing_relative_links": missing_links,
        "six_sources_in_review": statuses_valid,
        "wiki_directory_not_created": wiki_absent,
        "all_passed": all(r["passed"] for r in checks) and not missing_links and statuses_valid and wiki_absent,
        "limits": "Checks file integrity, locatable local outputs and review state; does not validate facts, all PDF images, remote links, Wiki or slides."
    }
    output.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k != "checks"}, ensure_ascii=False))
    if not summary["all_passed"]:
        sys.exit(1)


if __name__ == "__main__":
    main()

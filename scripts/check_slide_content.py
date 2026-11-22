"""Cross-check authored content against the approved outline and Wiki links.

This validates structure and consistency, not volleyball facts or browser layout.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from urllib.parse import unquote
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def pages(text):
    return re.findall(r"^## (\d{2})｜([^\n]+)\n(.*?)(?=^## |\Z)", text, re.M | re.S)


def meta(text, key):
    match = re.search(r"^" + re.escape(key) + r": (.+)$", text, re.M)
    return match.group(1).strip() if match else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="reports/checks/content-review-latest.json")
    args = parser.parse_args()
    outline, content, mapping = (read("slides/" + n) for n in ("outline.md", "content.md", "source-map.md"))
    checks = []

    def check(name, ok, detail):
        checks.append({"check": name, "passed": bool(ok), "detail": detail})

    op, cp = pages(outline), pages(content)
    check("approved_outline", meta(outline, "status") == "approved", meta(outline, "approved_on"))
    content_status = meta(content, "status")
    check("content_review_status", content_status in {"pending-user-confirmation", "approved"}, content_status)
    if content_status == "approved":
        check("H2_approval_date_recorded", bool(meta(content, "approved_on")), meta(content, "approved_on"))
    check("page_titles_and_order", [(n, t) for n, t, _ in cp] == [(n, t) for n, t, _ in op] and len(cp) == 18, len(cp))
    rows = re.findall(r"^\| (C\d{2}\.\d+) \|", mapping, re.M)
    referenced = set(re.findall(r"\bC\d{2}\.\d+\b", content))
    check("claim_map_unique", len(rows) == len(set(rows)), len(rows))
    check("claim_map_coverage", referenced == set(rows), {"unmapped": sorted(referenced-set(rows)), "unused": sorted(set(rows)-referenced)})
    times, ids, sizes = [], [], []
    required = ["主頁文字", "展開補充", "講解提示", "圖解規格", "頁尾來源"]
    for (n, title, body), (_, _, obody) in zip(cp, op):
        sid = re.search(r"固定 ID：`([^`]+)`", body)
        oid = re.search(r"固定 ID：`([^`]+)`", obody)
        check(n+"_stable_id", bool(sid and oid) and sid.group(1) == oid.group(1), sid.group(1) if sid else None)
        if sid:
            ids.append(sid.group(1))
        ct = re.search(r"預估時間：(\d+):(\d{2})（(\d+) 秒）", body)
        ot = re.search(r"預估時間：(\d+):(\d{2})（(\d+) 秒）", obody)
        check(n+"_time_matches_outline", bool(ct and ot) and ct.groups() == ot.groups(), ct.groups() if ct else None)
        if ct:
            val = int(ct[1])*60+int(ct[2])
            times.append(val)
            check(n+"_time_arithmetic", val == int(ct[3]), val)
        check(n+"_complete_sections", all("### "+label+"\n" in body for label in required), required)
        specs = body.split("### 圖解規格", 1)[-1].split("### 頁尾來源", 1)[0]
        check(n+"_diagram_spec", all(x in specs for x in ["教學目的／視角", "元素／標籤", "狀態／條件", "圖說／替代文字", "依據"]), "purpose/view, elements, states/conditions, caption/alt, evidence")
        check(n+"_wiki_and_claims", "../wiki/" in body and bool(re.search(r"C"+n+r"\.\d+",body)), title)
        main_text = body.split("### 主頁文字",1)[-1].split("### 展開補充",1)[0]
        sizes.append({"page":n,"main_text_characters_approx":len(re.sub(r"〔[^〕]+〕|[\s*|#-]", "", main_text))})
    check("unique_slide_ids", len(ids) == len(set(ids)) == 18, ids)
    check("total_time", sum(times) == int(meta(outline,"estimated_total_seconds")) == int(meta(content,"estimated_total_seconds")) == 1100, sum(times))
    map_slide_ids = re.findall(r"^\| (\d{2}) `([^`]+)` \|",mapping,re.M)
    check("map_page_ids", map_slide_ids == [(n,sid) for (n,_,_),sid in zip(cp,ids)], len(map_slide_ids))

    # Compare the two authored rotation states, not a hard-coded expected picture.
    clockwise = {2:1,1:6,6:5,5:4,4:3,3:2}
    for number, before_re, after_re in [
        ("06", r"輪轉前為 ([^；]+)", r"輪轉後為 ([^。]+)"),
        ("13", r"例 A：([^；]+)", r"例 B 為一次輪轉後：([^。]+)"),
    ]:
        body = next(b for n,_,b in cp if n == number)
        bm, am = re.search(before_re,body), re.search(after_re,body)
        before = {int(k):v for k,v in re.findall(r"([1-6])=([A-Z]+[12]?)",bm[1])} if bm else {}
        after = {int(k):v for k,v in re.findall(r"([1-6])=([A-Z]+[12]?)",am[1])} if am else {}
        check(number+"_rotation_states", len(before)==6 and len(after)==6 and len(set(before.values()))==6 and after=={clockwise[k]:v for k,v in before.items()}, {"before":before,"after":after})

    quiz = next(b for n,_,b in cp if n == "17")
    qs = re.findall(r"\*\*(Q[1-3])｜.*?\*\*.*?\n\n- A．([^\n]+)\n- B．([^\n]+)",quiz,re.S)
    keys = re.findall(r"^\| (Q[1-3]) \| \*\*([AB])\*\*。([^|]+)\|",quiz,re.M)
    check("quiz_has_questions_and_explanations", {q for q,_,_ in qs}=={q for q,_,_ in keys}=={"Q1","Q2","Q3"}, {"options":qs,"answer_keys":keys})
    if content_status == "pending-user-confirmation":
        check("HTML_not_created_before_H2", not (ROOT/"slides/index.html").exists(), "H2 is pending")
    else:
        check("HTML_permitted_after_H2", True, "Approved content permits the next build phase; browser checks are separate")
    check("no_placeholder_copy", not re.search(r"TODO|TBD|待填|待撰寫|稍後補上",content), "complete authored text")

    documents = sorted(set(list((ROOT/"slides").glob("*.md"))+list((ROOT/"wiki").rglob("*.md"))+[ROOT/p for p in ["AGENTS.md","README.md","reports/slides-graph.md","reports/workflow.md","reports/checks/content-review-2026-11-22.md"]]))
    missing, count = [], 0
    for path in documents:
        text = re.sub(r"```.*?```","",path.read_text(encoding="utf-8"),flags=re.S)
        for raw in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",text):
            target = raw.strip().split("#",1)[0]
            if not target or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:",target):
                continue
            count += 1
            dest = (path.parent/unquote(target)).resolve()
            if not dest.exists():
                missing.append({"file":str(path.relative_to(ROOT)),"target":raw})
    check("local_markdown_links", not missing, {"checked":count,"missing":missing})
    status_errors = []
    for path in (ROOT/"wiki").rglob("*.md"):
        if path.name=="log.md":
            continue
        expected = "ingested" if path.parent.name=="sources" else "verified"
        if meta(path.read_text(encoding="utf-8"),"status") != expected:
            status_errors.append(str(path.relative_to(ROOT)))
    check("wiki_states", not status_errors, status_errors)
    failures=[c["check"] for c in checks if not c["passed"]]
    result={"checked_at":datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds"),"timezone":"Asia/Taipei","status":"failed" if failures else "passed","scope":"content v0.1; outline v0.1; source-map v0.2; affected Wiki and project links","slide_count":len(cp),"claim_count":len(rows),"estimated_total_seconds":sum(times),"relative_links_checked":count,"check_count":len(checks),"failures":failures,"checks":checks,"main_text_sizes":sizes,"input_sha256":[{"path":str(p.relative_to(ROOT)).replace("\\","/"),"sha256":hashlib.sha256(p.read_bytes()).hexdigest()} for p in documents],"not_tested":["final rendered images","browser interaction and layout","rehearsal duration","real beginner comprehension"]}
    output=(ROOT/args.output).resolve()
    output.relative_to(ROOT)
    output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({k:result[k] for k in ["checked_at","status","slide_count","claim_count","estimated_total_seconds","relative_links_checked","check_count","failures"]},ensure_ascii=True))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

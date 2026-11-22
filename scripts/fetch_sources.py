"""Save the six approved source snapshots without overwriting existing originals."""
from datetime import datetime, timedelta, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
TZ = timezone(timedelta(hours=8), "Asia/Taipei")
SOURCES = [
    ("S01", "FIVB Official Volleyball Rules 2025-2028", "https://www.fivb.com/wp-content/uploads/2025/01/FIVB-Volleyball_Rules2025_2028-EN-v05.pdf", "pdf"),
    ("S02", "FIVB Coaches Manual Level I", "https://www.fivb.com/wp-content/uploads/2024/03/FIVB_Coach_Manual_EN.pdf", "pdf"),
    ("S03", "FIVB Coaches Manual Level II", "https://www.fivb.com/wp-content/uploads/2024/03/Coaches_Manual_Level_II_EN.pdf", "pdf"),
    ("S04", "USA Volleyball - Recipe for a Setter", "https://usavolleyball.org/resource/recipe-for-a-setter/", "html"),
    ("S05", "USA Volleyball - Defense is More Than Just Another Team System", "https://usavolleyball.org/resource/defense/", "html"),
    ("S06", "FIVB Board of Administration approves rule tests for 2026 competitions", "https://www.fivb.com/fivb-board-of-administration-approves-rule-tests-for-2026-competitions/", "html"),
]
VERIFICATION_SOURCES = [
    ("V01", "VNL 2026 Competition Regulations - verification of S06", "https://images.volleyballworld.com/image/upload/fl_attachment/fivb-prd/b1wtfxzi6hf0wuwcbvos.pdf", "pdf"),
    ("V02", "CEV European Volleyball Cups 2027 Official Communication 1-4 - verification of S06", "https://inside.prod.cev.eu/media/0kjb1dta/cev-european-volleyball-cups-2027-official-communication-1-4-web.pdf", "pdf"),
]


def main():
    checks = ROOT / "reports" / "checks"
    checks.mkdir(parents=True, exist_ok=True)
    failed = []
    verification = "--verification" in sys.argv
    for sid, title, url, kind in (VERIFICATION_SOURCES if verification else SOURCES):
        folder = ROOT / "raw" / "verification" / sid if verification else ROOT / "raw" / sid
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / f"original.{kind}"
        receipt = folder / "retrieval.json"
        if target.exists():
            if not receipt.exists():
                raise RuntimeError(f"{sid}: original exists but retrieval receipt is missing")
            saved = json.loads(receipt.read_text(encoding="utf-8"))
            if sha256(target.read_bytes()).hexdigest() != saved["sha256"]:
                raise RuntimeError(f"{sid}: original no longer matches saved hash")
            print(f"{sid}: existing snapshot verified; skipped", flush=True)
            continue
        event = {"id": sid, "title": title, "requested_url": url, "attempted_at": datetime.now(TZ).isoformat()}
        try:
            if "--curl" in sys.argv:
                marker = b"\n__HW10_CURL_METADATA__"
                fetched = subprocess.run(["curl.exe", "--silent", "--show-error", "--fail", "--location", "--max-time", "60", "--write-out", marker.decode() + "%{json}", url], capture_output=True, check=True)
                body, metadata = fetched.stdout.rsplit(marker, 1)
                details = json.loads(metadata)
                event.update({"download_engine": "curl", "resolved_url": details["url_effective"], "http_status": details["http_code"], "content_type": details["content_type"]})
            else:
                request = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; VolleyballWikiSourceReview/1.0)"})
                with urlopen(request, timeout=45) as response:
                    body = response.read()
                    event.update({"download_engine": "urllib", "resolved_url": response.geturl(), "http_status": response.status, "content_type": response.headers.get("Content-Type"), "last_modified": response.headers.get("Last-Modified"), "etag": response.headers.get("ETag")})
            if kind == "pdf" and not body.startswith(b"%PDF-"):
                raise ValueError("Downloaded response is not a PDF")
            if kind == "html" and b"<html" not in body[:20000].lower():
                raise ValueError("Downloaded response does not look like HTML")
            with target.open("xb") as stream:
                stream.write(body)
            event.update({"result": "downloaded", "retrieved_at": datetime.now(TZ).isoformat(), "bytes": len(body), "sha256": sha256(body).hexdigest(), "local_path": target.relative_to(ROOT).as_posix()})
            with receipt.open("x", encoding="utf-8") as stream:
                json.dump(event, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
            print(f"{sid}: saved {len(body):,} bytes; SHA256 {event['sha256'][:12]}", flush=True)
        except (OSError, HTTPError, URLError, ValueError, subprocess.CalledProcessError) as error:
            event.update({"result": "failed", "error_type": type(error).__name__, "error": str(error)})
            failed.append(sid)
            print(f"{sid}: FAILED {type(error).__name__}: {error}", flush=True)
        with (checks / "fetch-attempts.jsonl").open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(event, ensure_ascii=False) + "\n")
    if failed:
        print("Failed sources: " + ", ".join(failed), flush=True)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

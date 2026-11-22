"""Display selected PDF pages from the local extraction, using 1-based PDF pages."""
import json
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[1]
source_id = sys.argv[1]
pages = json.loads((root / "raw" / source_id / "pages.json").read_text(encoding="utf-8"))
selected = []
for token in sys.argv[2].split(","):
    if "-" in token:
        first, last = map(int, token.split("-"))
        selected.extend(range(first, last + 1))
    else:
        selected.append(int(token))
for number in selected:
    page = pages[number - 1]
    print(f"\n[{source_id} | PDF page {number}]\n")
    print("\n".join(re.sub(r" {2,}", " ", line).strip() for line in page["text"].splitlines() if line.strip()))

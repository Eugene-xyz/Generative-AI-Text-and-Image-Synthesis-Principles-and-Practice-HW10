"""Read S02's two-column chapters left column first, after visual verification."""
import json
from pathlib import Path
import pdfplumber

root = Path(__file__).resolve().parents[1]
source = root / "raw" / "S02"
selected = list(range(129, 140)) + list(range(147, 152))
records = []


def ordered_text(words):
    lines = []
    for word in sorted(words, key=lambda w: (round(w["top"] / 3), w["x0"])):
        if not lines or abs(lines[-1][0] - word["top"]) > 3:
            lines.append((word["top"], [word]))
        else:
            lines[-1][1].append(word)
    return "\n".join(" ".join(w["text"] for w in sorted(line, key=lambda w: w["x0"])) for _, line in lines)


with pdfplumber.open(source / "original.pdf") as pdf:
    for number in selected:
        page = pdf.pages[number - 1]
        # Facing-page margins shift the gutter: odd pages ~290pt, even ~304pt.
        # Verified against the original page and word coordinates, not page midpoint.
        middle = 290 if number % 2 else 304
        words = page.extract_words()
        # Assign complete words rather than clipping glyphs at the gutter.
        left = ordered_text([word for word in words if word["x0"] < middle])
        right = ordered_text([word for word in words if word["x0"] >= middle])
        records.append({"pdf_page": number, "printed_page": number - 4, "left": left, "right": right})
(source / "columns.json").write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(source / "text-by-columns.txt").write_text("\n\n".join(f"===== PDF PAGE {p['pdf_page']} / PRINTED {p['printed_page']} =====\nLEFT COLUMN\n{p['left']}\nRIGHT COLUMN\n{p['right']}" for p in records) + "\n", encoding="utf-8")
print(f"Extracted {len(records)} selected two-column pages; originals unchanged.")

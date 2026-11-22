"""Render selected original pages for source verification with bundled Poppler."""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
poppler = shutil.which("pdftoppm")
if not poppler:
    raise SystemExit("pdftoppm is required")
output = root / "reports" / "checks" / "figures"
output.mkdir(parents=True, exist_ok=True)
jobs = {"S01": [27, 36, 44, 45, 66, 68, 72], "S02": [3, 86, 133, 149], "S03": [47, 51, 55]}
for sid, pages in jobs.items():
    for page in pages:
        prefix = output / f"{sid}-pdf{page:03}"
        if not prefix.with_suffix(".png").exists():
            subprocess.run([poppler, "-f", str(page), "-l", str(page), "-r", "105", "-singlefile", "-png", str(root / "raw" / sid / "original.pdf"), str(prefix)], check=True, capture_output=True)
        print(prefix.relative_to(root).as_posix() + ".png", flush=True)

"""Rend chaque <section class="slide"> d'un fichier HTML en PNG 1080x1350 compressé.

Usage : python3 kit/render.py <fichier.html> <dossier_sortie> <prefixe>
Sortie : <dossier_sortie>/<prefixe>-1.png, -2.png, ...
Prérequis : pip install playwright pillow --break-system-packages && python3 -m playwright install chromium
"""
import sys, pathlib
from playwright.sync_api import sync_playwright
from PIL import Image

html, outdir, prefix = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
outdir.mkdir(parents=True, exist_ok=True)
paths = []
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(pathlib.Path(html).resolve().as_uri())
    pg.wait_for_timeout(1000)
    for i, el in enumerate(pg.query_selector_all(".slide"), 1):
        f = outdir / f"{prefix}-{i}.png"
        el.screenshot(path=str(f))
        Image.open(f).convert("RGB").quantize(colors=32, method=Image.Quantize.MEDIANCUT).save(f, optimize=True)
        paths.append(str(f))
    b.close()
print("\n".join(paths))

"""Generate the responsive WebP variants of the hero photo.

The source file (media/younes.png) is a 4253x5434 PNG (~4.9 MB) that was being sent
as-is to phones, where it is only displayed ~390 CSS px wide.  These variants keep the
desktop rendering on the untouched original while giving mobile a file that is ~30x
smaller.

Usage:  python scripts/make_hero_variants.py
"""

from pathlib import Path

from PIL import Image

BASE_DIR = Path(__file__).resolve().parent.parent
SOURCE = BASE_DIR / "media" / "younes.png"
OUT_DIR = BASE_DIR / "static" / "img"

# (target width in px, webp quality) -- 900w covers small phones, 1400w covers phones
# with a 3x DPR at full viewport width and 2560w covers landscape phones / very high DPR
# screens, so no phone ever has to fall back to the original 4.9 MB PNG.
VARIANTS = [(900, 82), (1400, 82), (2560, 80)]


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with Image.open(SOURCE) as img:
        rgb = img.convert("RGB")
        for width, quality in VARIANTS:
            height = round(rgb.height * width / rgb.width)
            resized = rgb.resize((width, height), Image.LANCZOS)
            out = OUT_DIR / f"younes-{width}.webp"
            resized.save(out, "WEBP", quality=quality, method=6)
            print(f"{out.relative_to(BASE_DIR)}  {resized.size}  {out.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    main()

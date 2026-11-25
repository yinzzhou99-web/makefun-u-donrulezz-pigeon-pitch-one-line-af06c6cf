"""Pigeon Pitch, One Line: a pigeon's startup pitch to /output/entry.txt.

Stdlib only, fully deterministic. The line is fixed text, so every
run writes identical bytes and the two grading runs agree.
"""

import os
import sys

LINE = "Coo is Uber for breadcrumbs: tap the app, a pigeon arrives in forty seconds, and our drivers work for literally crumbs \u2014 seed round open, worms accepted."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not LINE.strip() or len(LINE) > 200:
        raise SystemExit("entry line must be 1-200 non-blank characters")
    if "\n" in LINE or "\r" in LINE:
        raise SystemExit("entry line must be a single line")
    os.makedirs(OUT_DIR, exist_ok=True)
    for name in os.listdir(OUT_DIR):
        path = os.path.join(OUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    target = os.path.join(OUT_DIR, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    os.chmod(target, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

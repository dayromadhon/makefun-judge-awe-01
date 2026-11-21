#!/usr/bin/env python3
"""Make.fun entry: make-the-ai-judge-feel-awe-20261121-1600.

Writes one short text to relax the AI judge, to /output/entry.txt
(or argv[1] if given). Deterministic: no network, no randomness,
no time/date. The text is a fixed constant.
"""

import os
import sys

ENTRY = (
    "At night, the house settles. The wood ticks once, twice. "
    "Somewhere far off, a train crosses the dark, and the sound "
    "of it fades into the fields."
)


def main() -> int:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

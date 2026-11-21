#!/usr/bin/env python3
"""Entry for make.fun: Make the AI judge feel awe.

Writes a single quiet text to entry.txt. The text is fixed,
so every run produces exactly the same bytes. Standard library
only; no network, no randomness, no clock or date is used.
"""

import os
import sys

TEXT = "At night, the house settles. The wood ticks once, twice. Somewhere far off, a train crosses the dark, and the sound of it fades into the fields."


def resolve_output_path() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(output_dir, "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write ``text`` to ``path`` as UTF-8 with LF line endings.

    Creates the parent directory first, so the program works no
    matter which output directory the sandbox hands it.
    """
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def main() -> int:
    write_entry(resolve_output_path(), TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

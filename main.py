#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of quiet, earned pride to /output/entry.txt.
Deterministic: no network, no randomness, no clock. The line is fixed.
"""

import hashlib
import os
import sys

LINE = "The apprentice who had swept the workshop floor for two years tightened the last bolt on his first chair, sat in it, and it held."

MIN_CHARS = 1
MAX_CHARS = 240


def main() -> int:
    text = LINE
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(
            f"entry length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    if not text.strip():
        print("entry is blank", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # Read back and verify: the file must hold exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text + "\n":
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(
        f"wrote {path}: {len(text)} chars, "
        f"sha256={hashlib.sha256(back.encode('utf-8')).hexdigest()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

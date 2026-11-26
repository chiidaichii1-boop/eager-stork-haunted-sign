#!/usr/bin/env python3
"""Write one funny sign for a haunted server room door to entry.txt.

The program writes exactly one line of text into
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
"""

import os

LINE = (
    "WARNING: The ghost in this server room has root access, "
    "and it reboots the servers at 3 a.m. just for fun."
)


def main():
    if len(LINE) > 120:
        raise ValueError("sign line exceeds the 120-character limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

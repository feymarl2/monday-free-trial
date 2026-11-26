#!/usr/bin/env python3
"""Entry for make.fun bounty u-gentle-badger-68-monday-morning-punchlines-709645dc.

Writes the entry text to /output/entry.txt. Stdlib only, no network,
no clock, no randomness: byte-identical output on every run.
The joke treats the weekend as an expired free trial.
"""

import os

TEXT = "Monday morning is proof that weekends are just a free trial that expired."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

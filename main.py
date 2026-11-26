#!/usr/bin/env python3
"""The Funniest Out-of-Office - make.fun entry.

Writes a single funny line to /output/entry.txt (or MAKEFUN_OUTPUT_DIR).
Out-of-office reply: the auto-reply has started replying to itself.
Built for the $2 "The Funniest Out-of-Office" bounty (limit 140 chars).
"""

import os

LINE = "Out of office until Friday. My auto-reply has started replying to itself and now believes it runs the company."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

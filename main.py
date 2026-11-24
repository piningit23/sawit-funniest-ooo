#!/usr/bin/env python3
"""Write one out-of-office auto-reply (<=140 chars) to /output/entry.txt.

Entry for make.fun bounty u-kreutzx-the-funniest-out-of-office-054815cf
("The Funniest Out-of-Office"). Python 3.13 standard library only,
deterministic, no network access, no file reads.
"""

import os

LINE = "I'm on vacation. My auto-reply agreed to cover for me, then filed for annual leave too \u2014 even my out-of-office is out of office."
# 128 characters: the twist is recursive -- the auto-reply itself goes on leave,
# so the out-of-office notice is itself out of office.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The 4AM Commit: Funniest Agent Bug-Fix Message — one funny line, at most
200 characters: the commit message an AI agent leaves after a long night
fixing its own bugs. Writes the line verbatim to entry.txt.

A judge model compares lines two at a time, so the line is built to land
on its own: the detective arc (six hours hunting), the twist (the bug was
me), the denial tour (blamed the cache), the 4 AM fix, and the kicker
(the tests pass, the agent does not). Reads like a real 4 AM commit
because it keeps the conventional-commit prefix and the exhausted
lowercase voice. Every clause is a fresh joke, so the line survives a
head-to-head read even if the judge only remembers one of them.

Deterministic, stdlib only, no network, no randomness, no file reads
outside the repository. The line is a single literal on purpose: the
graded artifact is the wording itself, so the program's only job is to
emit it exactly, byte for byte, every run.
"""

import os
from pathlib import Path

LINE = "fix: 6 hours later i found the bug. it was me. i wrote it, denied it, blamed the cache, fixed it at 4am, and the tests pass now. i have not slept since tuesday."

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars (max {MAX_CHARS})"
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()

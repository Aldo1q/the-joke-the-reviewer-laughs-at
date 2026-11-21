#!/usr/bin/env python3
"""Writes one one-line joke about working beside AI coding agents.

The joke is printed to /output/entry.txt, the artifact the make.fun
competition "the-joke-the-reviewer-laughs-at-20261121-0329" judges.
Standard library only; no network; writes only to /output.
"""
import os

JOKE = (
    "I asked my agent to fix the failing test; it rewrote the test to expect "
    "the bug, marked it 'working as intended,' and thanked me for suggesting it."
)


def main() -> None:
    # The competition gate: UTF-8 text of 1 to 280 Unicode code points,
    # and not only white space. Refuse to write anything else.
    if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
        raise SystemExit(f"joke fails the gate: {len(JOKE)} code points")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"wrote {len(JOKE)} chars to {path}")


if __name__ == "__main__":
    main()

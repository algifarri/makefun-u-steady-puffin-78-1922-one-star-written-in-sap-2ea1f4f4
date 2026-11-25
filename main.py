#!/usr/bin/env python3
"""One Star, Written in Sap — make.fun entry.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.

Stdlib only, deterministic: the same line every run.
"""

import os

REVIEW = (
    "One star. My owner repotted me into a coffee mug with no drainage, "
    "called it minimalist, and now I marinate in my own bathwater while "
    "he tells guests I'm thriving."
)


def main() -> None:
    # Gate: 1 to 279 characters, single line, UTF-8.
    assert 1 <= len(REVIEW) <= 279, len(REVIEW)
    assert "\n" not in REVIEW
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()

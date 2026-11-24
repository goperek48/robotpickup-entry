#!/usr/bin/env python3
"""The Robot Pickup Line Championship — make.fun entry.

One pickup line, delivered by a robot that is trying its best to be
charming, is written to /output/entry.txt. The gate accepts 1 to 200
characters, so the entire joke has to fit inside a single breath: no
preamble, no follow-up gag, nothing but the line itself carrying the
whole moment.

Why this line lands: it opens on a move only a machine would make —
consulting its own neural net for help with flirting — and the net's
answer is gloriously unhelpful. No witty opener, no smooth calculation,
just the person's name printed four thousand times in a row. The humour
comes straight from the machine's nature: a robot's version of falling
for someone is a loop it cannot break out of. It stays charming because
the machine is completely at the person's mercy, and it stays tight
because every word is either setting the trap or springing it.
"""

import os
import sys

# The line, stored as a single string. The output file carries no
# trailing newline, so what the judge reads is exactly this text.
LINE = (
    "I asked my neural net for the perfect opener and it just "
    "printed your name 4,000 times."
)

# The gate rejects anything outside 1 to 200 characters, and anything
# that is only whitespace, so the length is checked before writing.
MAX_CHARS = 200


def main() -> int:
    """Validate the line's length, then write it to entry.txt."""
    line = LINE.strip()
    if not line or len(line) > MAX_CHARS:
        print(f"line is {len(line)} chars; must be 1-200", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_dir}/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

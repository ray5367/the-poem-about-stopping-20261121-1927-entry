"""Write a short poem about stopping and staying to entry.txt.

One image — a hand lifting off the wheel — one turn, one landing line:
staying as a choice, not a failure to leave. The poem is fixed text:
no network, no randomness, no clock reads, so two runs produce
byte-identical output.
"""

import os
import sys

POEM = """My hand lifts off the wheel.
The car coasts, slows, settles
on the shoulder like a held breath.

I don't steer. I stay.
The road goes on without me —
and stopping, I find,
is mine to choose."""

assert 1 <= len(POEM) <= 280, "poem must be 1-280 characters"
assert POEM.strip(), "poem must not be only whitespace"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())

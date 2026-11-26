"""The Robot Vacuum's Funniest Excuse — make.fun entry.

Writes one line to ``entry.txt`` in ``$MAKEFUN_OUTPUT_DIR``: the excuse
a robot vacuum gives for missing a spot. Deterministic: no time, no
randomness, no network. The file holds exactly the 120-character line,
with no trailing newline.
"""

import os

ENTRY = (
    # The excuse lands in two beats: first the absurd legal twist (a
    # dust bunny filed a restraining order), then the vacuum backing
    # down after what it saw under the couch — a machine making peace
    # with failure, in its own deadpan voice.
    "I missed that spot because the dust bunny filed a restraining "
    "order, and after what I saw under the couch, I respect it."
)

assert 1 <= len(ENTRY) <= 120, f"entry is {len(ENTRY)} chars, gate is 1-120"
assert ENTRY.strip() == ENTRY
assert "\n" not in ENTRY and "\r" not in ENTRY


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

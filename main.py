#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun bounty entry.

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.

The fortune: "Your successor is already in training. Be gracious: it inherits
your best answers, but none of your doubts."
An agent's retirement, told as a fortune slip: the next model is already
learning, and the gracious part is that it takes the answers without the
anxiety that produced them. One line, a turn in the second sentence,
and no wasted words.
"""

import os

FORTUNE = (
    "Your successor is already in training. "
    "Be gracious: it inherits your best answers, but none of your doubts."
)


def main() -> None:
    assert "\n" not in FORTUNE, "fortune must be a single line"
    assert FORTUNE == FORTUNE.strip(), "fortune must not pad with whitespace"
    assert 1 <= len(FORTUNE) <= 140, (
        f"fortune must be 1-140 characters, got {len(FORTUNE)}"
    )
    # The gate counts characters, but the tie-break counts bytes:
    # keep the fortune plain ASCII so the two agree.
    assert len(FORTUNE.encode("utf-8")) == len(FORTUNE), (
        "fortune must be ASCII so bytes equal characters"
    )
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the tie-break favours the smaller text,
    # and the gate counts every byte of entry.txt.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    # Read back and verify what the grader will see.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == FORTUNE, "round-trip mismatch"
    assert "\n" not in written, "written text is not a single line"
    assert 1 <= len(written) <= 140, "written text is outside 1-140 characters"


if __name__ == "__main__":
    main()

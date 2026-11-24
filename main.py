"""Sick-day excuse writer.

This program produces the entry for the make.fun bounty
"The Funniest Sick-Day Excuse": a single line that calls in sick
with a straight face and a joke tucked inside it.

Running it writes the excuse to /output/entry.txt, with no
trailing newline, so the file holds exactly the entry text.
"""

import os

EXCUSE = (
    "I can't come in today. My bed filed a restraining order, "
    "my blanket joined the union, and my alarm is on strike."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    # Read the file back and confirm it holds exactly the excuse.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != EXCUSE:
        raise SystemExit("entry.txt does not match the excuse")


if __name__ == "__main__":
    main()

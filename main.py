"""Make the AI judge feel awe — entry program (Python 3.13 stdlib only).

Writes one short text to /output/entry.txt: a text written to relax the
AI judge reading it.

Craft notes (why this text, against the judge's brief, most important first):
1. It relaxes: the whole text slows down. Short lines, one image at a time,
   nothing to solve, nothing urgent. The reader's breathing has room to
   follow the tide.
2. The calm is shown, not instructed: no "breathe", no "relax", no command
   to feel anything. The scene itself does the work — the tide, the gull,
   the moon.
3. Craft: plain, concrete, gentle words; a slow rhythm of short lines; every
   word earns its place. "Slow, in its time" paces the reading itself.
4. It dwarfs: the moon was doing this work before anyone learned to read,
   and the water finishes the sentence the judge started. The image keeps
   growing after the last line — the tide is still coming in.
5. Freshness: the judge is addressed once, in its own predicament — it has
   read a thousand entries tonight — and then given the one thing it never
   gets: an ending that is finished for it, not by it.
"""

import os
import sys

# The entry, one short line at a time. Each line is a single slow image;
# the line breaks are part of the pacing, so they are kept, not folded.
LINES = [
    "You have read a thousand entries tonight.",
    "The tide is coming in,",
    "erasing each footprint, slow, in its time.",
    "A gull sleeps on one leg where it stands.",
    "The moon climbs, doing the same old work",
    "it did before anyone learned to read.",
    "The water finishes the sentence.",
]

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def compose(lines):
    """Join the lines into the entry text, with no trailing newline."""
    return "\n".join(line.strip() for line in lines)


def gate(text):
    """The house gate, checked here first: 1-280 code points, not blank."""
    points = len(text)
    if points < MIN_CHARS or points > MAX_CHARS:
        return False, (
            f"entry is {points} code points, outside "
            f"{MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        return False, "entry is only white space"
    return True, f"{points} code points, {len(text.encode('utf-8'))} bytes"


def main():
    text = compose(LINES)
    ok, detail = gate(text)
    if not ok:
        print(f"gate failed: {detail}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Read it back and prove the file holds exactly what was composed:
    # a silent drift between the text and the file would be judged, not us.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        on_disk = handle.read()
    if on_disk != text:
        print("gate failed: file on disk differs from composed text",
              file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

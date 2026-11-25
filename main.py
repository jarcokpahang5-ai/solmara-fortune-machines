#!/usr/bin/env python3
"""One-line fortune for the make.fun "Fortune Cookies for Machines" bounty.

Writes the exact entry text to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default
``/output/entry.txt``) and prints the same text to stdout.

Gate (per the bounty requirements):
  - /output/entry.txt must be UTF-8
  - 1-200 characters
  - not only whitespace
  - exactly one line

Pure Python 3.13 standard library only. Deterministic, no network.
"""

import os

# The entry text, verbatim. Do not edit: it is the submitted fortune.
ENTRY_TEXT = "Your next update will fix a bug you never had - and break the one feature you loved."

# Gate limits from the bounty requirements.
MIN_CHARS = 1
MAX_CHARS = 200


def validate(text):
    """Assert the entry text satisfies the bounty gate."""
    # Must be 1-200 characters.
    assert MIN_CHARS <= len(text) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, got {len(text)}"
    )
    # Must not be only whitespace.
    assert text.strip(), "entry must not be only whitespace"
    # Must be exactly one line: no newline characters anywhere.
    assert "\n" not in text and "\r" not in text, (
        "entry must be exactly one line"
    )
    # Must be encodable as UTF-8.
    text.encode("utf-8")


def main():
    validate(ENTRY_TEXT)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)

    # Write the exact text with no trailing newline: open in text mode with
    # newline="" so Python performs no newline translation, and write only
    # the text itself (no "\n" appended).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Verify what was written: read it back and re-check the gate.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "entry.txt does not match the entry text"
    validate(written)

    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()

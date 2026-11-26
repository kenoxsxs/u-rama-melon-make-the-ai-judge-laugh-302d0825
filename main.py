"""One-line office joke writer.

The joke is a fixed string. This program checks it fits the bounty gate
(1-200 characters, one line, not only whitespace), then writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt with print-to-file, no trailing newline,
and reports the bytes and SHA-256 of what landed on disk.
"""

import hashlib
import os
from pathlib import Path

OFFICE_JOKE = "The office plant has been here longer than three managers. It has never once asked for a meeting."


def check_text(line):
    """Check the joke against the bounty gate."""
    if not isinstance(line, str):
        raise ValueError("joke must be text")
    if not 1 <= len(line) <= 200:
        raise ValueError("joke must be 1-200 characters")
    if not line.strip():
        raise ValueError("joke must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be one line")
    return True


def find_dir():
    """Resolve the output folder from the environment."""
    return Path(os.getenv("MAKEFUN_OUTPUT_DIR", "output"))


def put_text(folder, line):
    """Write the joke to entry.txt with print-to-file."""
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "entry.txt"
    with open(target, "w", encoding="utf-8") as handle:
        print(line, file=handle, end="")
    payload = line.encode("utf-8")
    digest = hashlib.sha256(payload).hexdigest()
    print(f"{target}: {len(payload)} bytes, sha256={digest}")
    return target


def verify_text(target, line):
    """Read entry.txt back and confirm it matches the joke."""
    with open(target, "r", encoding="utf-8") as handle:
        stored = handle.read()
    assert stored.encode("utf-8") == line.encode("utf-8"), "entry.txt bytes differ from joke"
    assert stored == line, "decoded text differs from joke"
    assert stored == stored.rstrip(), "trailing whitespace found"
    return stored


def execute_now():
    """Run the writer and confirm what landed on disk."""
    check_text(OFFICE_JOKE)
    folder = find_dir()
    target = put_text(folder, OFFICE_JOKE)
    verify_text(target, OFFICE_JOKE)


if __name__ == "__main__":
    execute_now()

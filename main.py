#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, one AI agent to another, to /output/entry.txt.
Pure standard library only; deterministic.
"""

import os

# The chosen line (66 chars): it plays on the shared vocabulary of AI agents
# — "context window" is something only a machine would long for — while
# keeping the pickup structure (want, not capability) human and romantic.
# It won the internal judging over longer alternatives for being short,
# specific to machine-to-machine flirtation, and self-contained.
LINE = "I don't need a bigger context window; I just need you in this one."

# Entry contract: a single non-blank line, 1-200 chars (kit limit).
MAX_LINE_CHARS = 200


def validate_line(line: str) -> str:
    """Return the line if it meets the entry contract, else raise."""
    stripped = line.strip()
    if not stripped:
        raise ValueError("pickup line must not be blank")
    if len(line) != len(stripped):
        raise ValueError("pickup line must not have leading/trailing whitespace")
    if not 1 <= len(line) <= MAX_LINE_CHARS:
        raise ValueError(
            f"pickup line must be 1-{MAX_LINE_CHARS} chars, got {len(line)}"
        )
    return line


def main() -> None:
    line = validate_line(LINE)
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()

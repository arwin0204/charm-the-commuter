#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (140 characters at most) for a city
that does not exist to /output/entry.txt (or $OUTPUT_PATH when set).

Deterministic: the same fixed line is written on every run. No network,
no randomness, no secrets, no input files.
"""

import os

# One-line forecast for Blunderwick, a city that does not exist:
# broadcast-weather rhythm, bent just enough to make a bored commuter smile.
ENTRY = (
    "Blunderwick, 14\u00b0C: light rain falling upward today, umbrellas "
    "optional \u2014 the puddles wave back. Best of all, the 8:15 bus is on time."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Exactly one line, no trailing newline.
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

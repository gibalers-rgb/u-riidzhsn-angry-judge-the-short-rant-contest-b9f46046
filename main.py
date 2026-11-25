#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Deterministic, stdlib only, no network, no API key.
"""

import os

RANT = (
    "The close-door button in the elevator is a lie. "
    "I have pressed it four thousand times and the doors have never once hurried. "
    "It exists so I can feel powerful while we wait for a man three floors up "
    "hauling a trombone. "
    "I press it every day. I will press it again tomorrow. "
    "Some people pray. I press the button."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(RANT)


if __name__ == "__main__":
    main()

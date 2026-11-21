"""Write a one-line joke about working beside AI coding agents to /output/entry.txt.

The joke: the agent does the work, then turns the tables on the human.
Runs with no network, writes UTF-8 text.
"""

import os

JOKE = (
    "My AI pair programmer fixed the bug, wrote the tests, "
    "and then quietly opened a ticket against me.\n"
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 280:
        raise ValueError("joke must be 1 to 280 characters, got %d" % len(text))
    os.makedirs("/output", exist_ok=True)
    try:
        os.chmod("/output", 0o755)
    except OSError:
        pass
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

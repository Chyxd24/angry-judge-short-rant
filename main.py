"""Angry Judge: The Short Rant Contest.

Writes one short funny rant about a small everyday annoyance to
/output/entry.txt. Concrete, escalating, punchline on the tail.
"""
import os

OUT_DIR = "/output"
RANT = ("The group chat is not a filing system. Nobody has ever wanted to "
        "find a password by scrolling 400 memes at midnight. And yet, every "
        "time: send it here, lose it forever, ask again. Use a notes app.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(RANT) <= 200, len(RANT)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(RANT)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == RANT
    print(f"wrote {len(RANT)} chars")


if __name__ == "__main__":
    main()

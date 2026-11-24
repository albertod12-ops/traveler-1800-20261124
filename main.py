"""One sentence for a traveler from 1800 (v1, original).

Writes one sentence to /output/entry.txt: a window in the wall through
which the traveler may speak with any soul on earth and read more books
than the greatest library holds. One image (the window), two things the
internet does (speak across the world, read without limit), every word
in use before 1800. One sentence, 131 characters. The gate check is the
200-character cap and the single full stop; the program asserts both
before it writes.
"""

import os

TEXT = (
    "It is a window in your wall through which you may speak with any "
    "soul on earth and read more books than the greatest library holds."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

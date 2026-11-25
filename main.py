"""Famous Last Words: The Funniest Epitaph — make.fun entry.

Writes one line of famous last words, a tombstone epitaph of at most
150 characters, to /output/entry.txt.
"""

import os

EPITAPH = "I died as I lived: on mute."
MAX_CHARS = 150


def output_path() -> str:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def write_epitaph(text: str, path: str) -> None:
    """Atomically write the epitaph, then verify it by reading it back."""
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == text, "read-back mismatch"


def main() -> None:
    text = EPITAPH.strip()
    assert 1 <= len(text) <= MAX_CHARS, "epitaph out of bounds"
    assert "\n" not in text and "\r" not in text, "epitaph must be one line"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_epitaph(text, path)


if __name__ == "__main__":
    main()

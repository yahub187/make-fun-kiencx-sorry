"""Entry for make.fun bounty "Sorry, I Heard That Wrong".

Writes the winning one-line apology to the output directory as entry.txt,
with no trailing newline.
"""

import os

ENTRY_FILENAME = "entry.txt"

ENTRY = (
    "Sorry, I heard 'call Mum' and nearly rang the mob. "
    "Your mother is safe. My contact list is not."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()

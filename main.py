"""One Line to Your Younger Self: writes the line to /output/entry.txt.

Why this line: three concrete pieces of advice a younger self would actually
need, and the punch is the 2 a.m. text that was never going to be answered.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'Buy the boring index fund, learn to cook one real meal, and stop texting her back at 2 a.m. She was never going to reply properly.'

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote entry.txt", len(ENTRY), "chars")


if __name__ == "__main__":
    main()

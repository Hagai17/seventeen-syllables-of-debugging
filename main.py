"""Write one haiku about debugging to /output/entry.txt.

The haiku is three lines in the 5-7-5 syllable shape, at most 200
characters including the newline separators, with no trailing newline.
"""

import os

HAIKU = (
    "Ship day: I strip out\n"
    "each print line I used to hunt\n"
    "one rides along, live"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()

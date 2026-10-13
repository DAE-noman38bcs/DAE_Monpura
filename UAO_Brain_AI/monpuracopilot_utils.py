# Developer: Mahmud Abdullah Al Naman (মাহমুদ আব্দুল্লাহ আল নোমান)
# Email: noman38bcs@gmail.com
# Phone: 01623015273
# File: monpuracopilot_utils.py
"""Small utility helpers."""

def normalize_bn_digits(text: str) -> str:
    mapping = str.maketrans("০১২৩৪৫৬৭৮৯", "0123456789")
    return text.translate(mapping)


def chunk(seq, size=50):
    for i in range(0, len(seq), size):
        yield seq[i:i + size]

import pytest


# Make a function that reverses a string
def rev_str(s: str) -> str:
    return s[::-1]


def rev_strV2(s: str) -> str:
    new_s = ""
    for i in range(len(s)):
        new_s = s[i] + new_s

    return new_s


def test_reverse():
    assert rev_str("Gabriel") == "leirbaG"
    assert rev_str("Macbook") == "koobcaM"


def test_reverseV2():
    assert rev_strV2("Gabriel") == "leirbaG"
    assert rev_strV2("Macbook") == "koobcaM"

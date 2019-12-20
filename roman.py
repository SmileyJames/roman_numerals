#!/usr/bin/python3


alphabet = [
    (1000, "M"),
    (500, "D"),
    (100, "C"),
    (50, "L"),
    (10, "X"),
    (5, "V"),
    (1, "I"),
]


def numerals(integer):
    assert integer > 0 and integer < 4000
    return _numerals(integer)


def _numerals(integer):
    for i, (value, char) in enumerate(alphabet):
        multiple = integer // value
        remainder = integer % value
        is_even = i % 2 == 0

        def subtractive(diff):
            _char = alphabet[i - diff][1]
            return char + _char + _numerals(remainder)

        if multiple == 4 and is_even and i > 0:
            return subtractive(1)

        if multiple == 9 and is_even and i > 1:
            return subtractive(2)

        try:
            next_is_nine = (integer // alphabet[i + 1][0]) == 9
        except IndexError:
            next_is_nine = False
        if multiple != 0 and not next_is_nine:
            return char * multiple + _numerals(remainder)
    return ""


if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Generate roman numerals.")
    parser.add_argument(
        "integer",
        metavar="N",
        type=int,
        nargs=1,
        help="An integer to convert to roman numerals.",
    )
    args = parser.parse_args()
    try:
        print(numerals(args.integer[0]))
    except AssertionError:
        print("Integer must be greater than 0 and less than 4000", file=sys.stderr)
        sys.exit(1)

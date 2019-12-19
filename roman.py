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
    assert integer >= 0 and integer < 5000

    if integer <= 0:
        return ""

    for i, (num0, char) in enumerate(alphabet):

        def subtractive(n):
            rem = integer % n
            return numerals(num0 + rem - integer) + char + numerals(rem)

        mul0 = integer // num0
        if mul0 == 0:  # We might have to do subtractive notation...
            num1, _ = alphabet[i + 1]
            mul1 = integer // num1
            is_even = i % 2 == 0

            # ...for multiples of 4 e.g. IV, XL
            if not is_even and mul1 == 4:
                return subtractive(num1)

            # ...or multiples of 9 e.g. IX, XC
            try:
                num2, _ = alphabet[i + 2]  # IndexError
                mul2 = integer // num2
                if is_even and mul1 == 1 and mul2 == 9:
                    return subtractive(num2)
            except IndexError:
                pass
        else:
            # ...otherwise additive notation.
            return char * mul0 + numerals(integer % num0)


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
        print(
            "Integer must be greater than 0 and less than 5000",
            file=sys.stderr)
        sys.exit(1)

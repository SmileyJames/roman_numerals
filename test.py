#!/usr/bin/python3

import unittest
from roman import numerals


class TestRomanNumeral(unittest.TestCase):
    def test_one(self):
        self.assertEqual(numerals(1), "I")

    def test_three(self):
        self.assertEqual(numerals(3), "III")

    def test_four(self):
        self.assertEqual(numerals(4), "IV")

    def test_five(self):
        self.assertEqual(numerals(5), "V")

    def test_eight(self):
        self.assertEqual(numerals(8), "VIII")

    def test_nine(self):
        self.assertEqual(numerals(9), "IX")

    def test_ten(self):
        self.assertEqual(numerals(10), "X")

    def test_fourteen(self):
        self.assertEqual(numerals(14), "XIV")

    def test_ninety_nine(self):
        self.assertEqual(numerals(99), "XCIX")

    def test_two_thousand_and_nineteen(self):
        self.assertEqual(numerals(2019), "MMXIX")

    def test_three_thousand_four_hundred_and_seventy_nine(self):
        self.assertEqual(numerals(3479), "MMMCDLXXIX")


if __name__ == "__main__":
    unittest.main()

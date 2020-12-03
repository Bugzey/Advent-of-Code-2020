import unittest

from aoc2020.day_2 import *

class ParseRowTestCase(unittest.TestCase):
    def setUp(self):
        self.rows = [
            "1-3 a: abcde",
            "1-3 b: cdefg",
            "2-9 c: ccccccccc",
        ]

    def test_parse_row(self):
        result = list(map(lambda x: parse_row(x), self.rows))
        expected = [
            (1, 3, "a", "abcde"),
            (1, 3, "b", "cdefg"),
            (2, 9, "c", "ccccccccc"),
        ]

        self.assertEqual(result, expected)

class ValidatePasswordTestCase(unittest.TestCase):
    def setUp(self):
        self.parsed_rows = [
            (1, 3, "a", "abcde"),
            (1, 3, "b", "cdefg"),
            (2, 9, "c", "ccccccccc"),
        ]

    def test_validate_password(self):
        result = list(map(lambda x: validate_password(*x), self.parsed_rows))
        expected = [True, False, True]

        self.assertEqual(result, expected)

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.args = {
            "-": [
                "1-3 a: abcde",
                "1-3 b: cdefg",
                "2-9 c: ccccccccc",
            ]
        }

    def test_main(self):
        result = main(self.args)
        expected = 2

        self.assertEqual(result, expected)


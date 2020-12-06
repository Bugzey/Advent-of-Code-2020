import logging
import unittest

logger = logging.getLogger("aoc2020.day_5")
logger.setLevel(logging.DEBUG)

from aoc2020.day_5 import *

class ParseBinaryTestCase(unittest.TestCase):
    def setUp(self):
        self.binary = "FBFBBFFRLR"

    def test_parse_column(self):
        result = parse_binary(self.binary[:7], symbols = "FB")
        expected = 44
        self.assertEqual(result, expected)

    def test_parse_row(self):
        result = parse_binary(self.binary[7:], symbols = "LR")
        expected = 5
        self.assertEqual(result, expected)

class ReadBoardingPassTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [
            "FBFBBFFRLR",
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL",
        ]

    def test_single_boarding_pass(self):
        result = list(map(lambda x: read_boarding_pass(x), self.input_list))

        expected = (357, 567, 119, 820)
        for index, item in enumerate(expected):
            with self.subTest(i = index):
                self.assertEqual(result[index], item)


class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [
            "FBFBBFFRLR",
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL",
        ]

    def test_main(self):
        args = {
            "-": self.input_list,
        }
        result = main(args)
        expected = 820
        self.assertEqual(result, expected)

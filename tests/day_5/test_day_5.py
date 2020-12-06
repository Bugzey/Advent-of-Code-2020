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
                self.assertEqual(result[index]["seat_id"], item)

class FindMissingTestCase(unittest.TestCase):
    def setUp(self):
        self.seat_ids = [
            dict(seat_id = 44),
            dict(seat_id = 46),
            dict(seat_id = 47),
            dict(seat_id = 48),
            dict(seat_id = 49),
        ]
            
    def test_find_missing(self):
        result = find_missing(seat_ids = self.seat_ids)
        expected = 45
        self.assertEqual(result, expected)

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [
            "FBFBBFFRLR",
            "BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL",
        ]

    def test_main_find_max(self):
        args = {
            "-": self.input_list,
            "--find-missing": False,
        }
        result = main(args)
        expected = 820
        self.assertEqual(result, expected)

    def test_main_find_missing(self):
        args = {
            "-": self.input_list,
            "--find-missing": True,
        }
        result = main(args)
        expected = 120
        self.assertEqual(result, expected)


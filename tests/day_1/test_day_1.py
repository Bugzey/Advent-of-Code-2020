import unittest
import sys

from aoc2020.day_1 import *

class FindQuotientTestCase(unittest.TestCase):
    def setUp(self):
        self.demo_numbers = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]
        self.n5 = [
            1000,
            500,
            250,
            125,
            12,
            999,
            (2020 - 1000 - 500 - 250 - 125),
        ]


    def test_n2(self):
        result = find_quotient(
            input_list = self.demo_numbers,
            sum_to = 2020,
            n = 2,
        )
        expected = (299, 1721)
        self.assertEqual(result, expected)

    def test_n3(self):
        result = find_quotient(
            input_list = self.demo_numbers,
            sum_to = 2020,
            n = 3,
        )
        expected = (366, 675, 979)
        self.assertEqual(result, expected)

    def test_n5(self):
        result = find_quotient(
            input_list = self.n5,
            sum_to = 2020,
            n = 5,
        )
        expected = (125, 145, 250, 500, 1000)
        self.assertEqual(result, expected)

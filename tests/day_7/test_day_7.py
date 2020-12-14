import logging
import unittest

from aoc2020.day_7 import *

logger = logging.getLogger("aoc2020.day_7")
logger.setLevel(logging.DEBUG)

ITEMS = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]

class ParseInputTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = ITEMS

    def test_parse_input(self):
        result = parse_input(self.input_list)
        logger.debug(result)

        self.assertEqual(type(result), dict)
        self.assertIn("faded blue bag", result.keys())
        
        self.assertTrue(all((type(item) == dict for item in result.values())))

class CheckContainsTestCase(unittest.TestCase):
    def setUp(self):
        self.bags = parse_input(ITEMS)
        self.target_bag = "shiny gold bag"

    def test_check_contains(self):
        result_list = list(map(lambda x: \
            check_contains(
                bags = self.bags,
                source_bag = x,
                target_bag = self.target_bag,
            )[0],
            self.bags.keys()
        ))
        logger.debug("result_list: {}".format(result_list))
        expected = 4
        result = sum(result_list)
        self.assertEqual(result, expected)

class CountPossibilitiesTestCase(unittest.TestCase):
    def setUp(self):
        self.bags = parse_input(ITEMS)
        self.target_bag = "shiny gold bag"

    def test_count_possibilities(self):
        result = count_possibilities(self.bags, self.target_bag)
        expected = 4
        self.assertEqual(result, expected)

class SumContainsTestCase(unittest.TestCase):
    def setUp(self):
        contains_input = [
            "shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags.",
            "dark orange bags contain 2 dark yellow bags.",
            "dark yellow bags contain 2 dark green bags.",
            "dark green bags contain 2 dark blue bags.",
            "dark blue bags contain 2 dark violet bags.",
            "dark violet bags contain no other bags.",
        ]
        self.bags = parse_input(contains_input)
        self.target_bag = "shiny gold bag"

    def test_sum_contains(self):
        result = sum_contains(bags = self.bags, target_bag = self.target_bag)
        expected = 126
        self.assertEqual(result, expected)

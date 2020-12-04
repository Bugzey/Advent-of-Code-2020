import logging
import unittest

from aoc2020.day_3 import *

logger = logging.getLogger("aoc2020.day_3")
logger.setLevel(logging.DEBUG)

class ParseMapTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [
            "..##.......",
            "#...#...#..",
        ]

    def test_parse_map(self):
        map_width, map_height, parsed_map = parse_map(self.input_list)

        expected_map_width = len(self.input_list[0])
        self.assertEqual(map_width, expected_map_width)

        expected_map_height = len(self.input_list)
        self.assertEqual(map_height, expected_map_height)

        expected_parsed_map = [
            (2, 3),
            (0, 4, 8),
        ]
        self.assertEqual(parsed_map, expected_parsed_map)


class CountTreesTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#",
        ]
        self.map_width, self.map_height, self.parsed_map = parse_map(
            self.input_list
        )
        self.step_right = 3
        self.step_down = 1

    def test_count_trees(self):
        result = count_trees(
            map_width = self.map_width,
            map_height = self.map_height,
            parsed_map = self.parsed_map,
            step_down = self.step_down,
            step_right = self.step_right,
        )
        expected_result = 7
        self.assertEqual(result, expected_result)

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#",
        ]
        self.step_right = 3
        self.step_down = 1

        self.args = {
            "-": self.input_list,
            "--step-right": self.step_right,
            "--step-down": self.step_down,
        }

    def test_main(self):
        result = main(self.args)
        expected_result = 7
        self.assertEqual(result, expected_result)

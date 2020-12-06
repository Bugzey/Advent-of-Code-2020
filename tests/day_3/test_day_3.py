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


class GetPositionsTestCase(unittest.TestCase):
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

    def test_get_positions(self):
        result = get_positions(
            map_width = self.map_width,
            map_height = self.map_height,
            parsed_map = self.parsed_map,
            step_down = self.step_down,
            step_right = self.step_right,
        )
        expected_result = [
            (0, 0), (1, 3), (2, 6), (3, 9), (4, 1), (5, 4), (6, 7),
            (7, 10), (8, 2), (9, 5), (10, 8),
        ]
        self.assertEqual(result, expected_result)

class MainTestCase(unittest.TestCase):
    def setUp(self):
        self.args = {
            "-": [
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
            ],
            "--step-right": [1, 3, 5, 7, 1],
            "--step-down": [1, 1, 1, 1, 2],
            "--visualise": False,
            "--save-to": None,
        }


    def test_main(self):
        args = self.args
        args["--step-right"] == args["--step-right"][1]
        args["--step-down"] == args["--step-down"][1]
        result = main(args)
        expected_result = 336
        self.assertEqual(result.pop(), expected_result)

    def test_multiple_steps(self):
        args = self.args
        result = main(args)
        expected_result = 336
        self.assertEqual(result.pop(), expected_result)


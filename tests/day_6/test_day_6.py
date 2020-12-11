import logging
import unittest

from aoc2020.day_6 import *

logger = logging.getLogger("aoc2020.day_6")
logger.setLevel(logging.DEBUG)

SINGLE_GROUP = [
    "abcx",
    "abcy",
    "abcz",
]
MANY_GROUPS = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b",
]


class SplitGroupsTestCase(unittest.TestCase):
    def setUp(self):
        self.one_group = SINGLE_GROUP
        self.many_groups = MANY_GROUPS

    def test_split_single(self):
        result = split_groups(self.one_group)
        expected = [["abcx", "abcy", "abcz"]]
        logger.debug("result: {}".format(result))
        self.assertEqual(expected, result)

    def test_split_multiple(self):
        result = split_groups(self.many_groups)
        logger.debug("result: {}".format(result))
        expected_len = 5
        self.assertEqual(len(result), expected_len)

class GetGroupSetsTestCase(unittest.TestCase):
    def setUp(self):
        self.single_list = split_groups(SINGLE_GROUP)
        self.multiple_list = split_groups(MANY_GROUPS)

    def test_get_group_sets_single(self):
        result = get_group_sets(self.single_list)
        expected = [set("abcxyz")]
        self.assertEqual(result, expected)

    def test_get_group_sets_multiple(self):
        result = get_group_sets(self.multiple_list)
        expected = [set("abc"), set("abc"), set("abc"), set("a"), set("b")]
        self.assertEqual(result, expected)

class SumUniqueAnswersTestCase(unittest.TestCase):
    def setUp(self):
        single_list = split_groups(SINGLE_GROUP)
        multiple_list = split_groups(MANY_GROUPS)
        self.single_groups = get_group_sets(single_list)
        self.multiple_groups = get_group_sets(multiple_list)

    def test_sum_answers_single(self):
        result = sum_unique_answers(self.single_groups)
        expected = 6
        self.assertEqual(result, expected)

    def test_sum_answers_multiple(self):
        result = sum_unique_answers(self.multiple_groups)
        expected = 11
        self.assertEqual(result, expected)

class GetCommonAnswers(unittest.TestCase):
    def setUp(self):
        self.single_list = split_groups(SINGLE_GROUP)
        self.multiple_list = split_groups(MANY_GROUPS)

    def test_get_common_answers_single(self):
        result = get_common_answers(self.single_list)
        expected = [set("abc")]
        self.assertEqual(result, expected)

    def test_get_common_answers_multiple(self):
        result = get_common_answers(self.multiple_list)
        expected = [set("abc"), set(), set("a"), set("a"), set("b")]
        self.assertEqual(result, expected)


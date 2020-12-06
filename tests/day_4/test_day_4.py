import logging
import unittest

from aoc2020.day_4 import *

logger = logging.getLogger("aoc2020.day_4")
logger.setLevel(logging.DEBUG)

INPUT_LIST = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in",
]

class SplitPassportsTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = INPUT_LIST

    def test_split_passports(self):
        result = split_passports(
            input_list = self.input_list,
        )
        logger.debug("result: {}".format(result))
        
        expected_length = 4
        self.assertEqual(expected_length, len(result))

class ParsePassportTestCase(unittest.TestCase):
    def setUp(self):
        passports = split_passports(INPUT_LIST)
        self.passport = passports[0]

    def test_parse_passports(self):
        result = parse_passport(self.passport)
        self.assertEqual(type(result), dict)

        all_keys = KEY_MAP.keys()
        self.assertTrue(result.keys() == all_keys)

        self.assertTrue(all(result.values())) # valid passport with no missing fields

class ValidatePassportTestCase(unittest.TestCase):
    def setUp(self):
        passports = split_passports(INPUT_LIST)
        self.passports = map(lambda x: parse_passport(x), passports)

    def test_validate_passport(self):
        result = list(map(lambda x: validate_passport(x), self.passports))
        logger.debug("result: {}".format(result))

        expected_results = [
            ("valid", True),
            ("invalid", False),
            ("ignored", True),
            ("ignored and misisng", False),
        ]
        for index, item in enumerate(expected_results):
            message = item[0]
            test = self.assertTrue if item[1] else self.assertFalse
            with self.subTest(msg = message, i = index):
                test(result[index])

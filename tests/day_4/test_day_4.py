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

class ValidateFieldsTestCase(unittest.TestCase):
    def setUp(self):
        raw_valid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""
        raw_valid_passports = raw_valid_passports.split("\n")

        raw_invalid_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""
        raw_invalid_passports = raw_invalid_passports.split("\n")

        self.valid_passports = map(
            lambda x: parse_passport(x), 
            split_passports(raw_valid_passports)
        )
        self.invalid_passports = map(
            lambda x: parse_passport(x), 
            split_passports(raw_invalid_passports)
        )

    def test_valid_passports(self):
        field_results = list(map(lambda x: validate_fields(x), self.valid_passports))
        logger.debug("result: {}".format(result))
        self.assertTrue(all(result))

    def test_invalid_passports(self):
        result = list(map(lambda x: validate_fields(x), self.invalid_passports))
        logger.debug("result: {}".format(result))
        self.assertTrue(not any(result))


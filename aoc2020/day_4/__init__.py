"""
Advent of code day 4

Usage:
    day_4 [-]

"""
import logging
import re

logger = logging.getLogger("aoc2020.day_4")

KEY_MAP = dict(
    byr = "Birth Year",
    iyr = "Issue Year",
    eyr = "Expiration ",
    hgt = "Height",
    hcl = "Hair Co",
    ecl = "Eye Colo",
    pid = "Passport ",
    cid = "Country ID",
)

def split_passports(input_list: list) -> list:
    """
    Split a list of input passport data into separate complete passports

    Args:
        input_list: list of raw input data

    Returns:
        A list of strings where all fields of a passport are joined together
    """
    which_blank = list(filter(
        lambda x: input_list[x] == "", range(len(input_list))
    ))
    logger.debug("which_blank: {}".format(which_blank))
    
    join_indices = list(zip(
        (0, *which_blank),
        (*which_blank, len(input_list))
    ))
    logger.debug("join_indices: {}".format(join_indices))

    passports = [
        input_list[first:second] for first, second in join_indices
    ]
    passports = [item.strip() if type(item) == str else " ".join(item).strip() for item in passports]
    return(passports)

def parse_passport(passport: list) -> dict:
    """
    Get the values of each input field given for a passport. Missing fields return None

    Args:
        passport: string of all passport items

    Returns:
        Dictionary of parsed values for each key
    """
    item_matches = {
        key: re.search("{}:(\S+)".format(key), passport)\
        for key in KEY_MAP
    }
    logger.debug("item_matches: {}".format(item_matches))

    items = {
        key: value.group(1) if value else None \
        for key, value in item_matches.items()
    } 

    logger.debug("items: {}".format(items))
    return(items)

def validate_passport(passport :dict, ignore_fields = "cid") -> bool:
    """
    Assess whether a given passport has all required field while ignoring some fields

    Args:
        passport: dict of all expectd keys and their parsed values for a passport
        ignore_fields: string of a single field or a list of fields to ignnore when assessing
            passport validity

    Returns:
        Boolean of whether the passport is valid
    """
    #   Works one passport at a time
    if type(ignore_fields) == str:
        ignore_fields = [ignore_fields]

    expected_fields = set(KEY_MAP.keys()) - set(ignore_fields)

    valid_fields = map(
        lambda x: passport.get(x, None) is not None,
        expected_fields
    )

    return(all(valid_fields))

def main(args):

    raw_passports = split_passports(args["-"])
    passports = map(lambda x: parse_passport(x), raw_passports)
    valid_passports = map(lambda x: validate_passport(x), passports)

    result = sum(valid_passports)
    return(result)

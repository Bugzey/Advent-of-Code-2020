"""
Advent of code day 4

Usage:
    day_4 [options] [-]

Options
    -f, --validate-fields   Whether to validate separate fields
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

def validate_fields(passport :dict) -> bool:
    """
    Apply a set of nearly standardised rules to validate each passport field

    Args:
        passport: dictionary of all parssport fields for a given passport

    Returns:
        Bool of whether all fields pass the validation tests
    """
    def validate_number(item :str, lower :int, upper :int, prefix = "", suffix = ""):
        if not item:
            return(False)

        has_prefix = item.startswith(prefix)
        has_suffix = item.endswith(suffix)
        
        number_part = item[len(prefix):][:(-len(suffix) if suffix else None)]
        number_part = int(number_part) if number_part.isdigit() else None

        if number_part:
            right_range = number_part >= lower and number_part <= upper
        else:
            right_range = False

        result = has_prefix and has_suffix and right_range
        return(result)

    def validate_value(
        item :str,
        length = None,
        pattern = None,
        prefix = "",
        suffix = ""
    ):
        if not item:
            return(False)

        assert (length is not None and not pattern) or \
            (length is None and pattern)

        has_prefix = item.startswith(prefix)
        has_suffix = item.startswith(suffix)

        core_part = item[len(prefix):][:(-len(suffix) if suffix else None)]
        
        if length is not None:
            right_length = len(core_part) == length
        else:
            right_length = True

        if pattern:
            right_pattern = re.search(pattern, core_part) is not None
        else:
            right_pattern = True

        result = has_suffix and has_prefix and right_length and right_pattern
        return(result) 

    validation_map = dict(
        byr = lambda x: validate_number(x, lower = 1920, upper = 2002),
        iyr = lambda x: validate_number(x, lower = 2010, upper = 2020),
        eyr = lambda x: validate_number(x, lower = 2020, upper = 2030),
        hgt = lambda x: \
            validate_number(x, lower = 150, upper = 193, suffix = "cm") | \
            validate_number(x, lower = 59, upper = 76, suffix = "in"),
        hcl = lambda x: validate_value(x, pattern = r"[0-9a-f]{6}", prefix = "#"),
        ecl = lambda x: validate_value(
            x,
            pattern = r"^amb|blu|brn|gry|grn|hzl|oth$"
        ),
        pid = lambda x: validate_value(x, pattern = r"^\d{9}$"),
        cid = lambda x: True,
    )

    valid_fields = {
        key: validation_map[key](x = value) for key, value in passport.items()
    }
    logger.debug("valid_fields: {}".format(
        {key: (passport[key], valid_fields[key]) for key in passport}
    ))
    all_valid_fields = all(valid_fields.values())
    logger.debug(all_valid_fields)
    return(all_valid_fields)

def main(args):

    raw_passports = split_passports(args["-"])
    passports = list(map(lambda x: parse_passport(x), raw_passports))
    valid_passports = map(lambda x: validate_passport(x), passports)

    if args["--validate-fields"]:
        valid_passports = list(valid_passports)
        valid_fields = map(lambda x: validate_fields(x), passports)
        valid_passports = map(lambda x, y: x and y, valid_passports, valid_fields)

    result = sum(valid_passports)
    return(result)

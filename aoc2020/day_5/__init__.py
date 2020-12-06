"""
Advent of code 2020 - Day 5

Usage:
    day_5 [options] [-]

Options:
    -f, --find-missing  Whether to search for the missing in-between seat ID
    -h, --help  Print this help message and exit
"""
from functools import reduce
from typing import Union
import logging

logger = logging.getLogger(__name__)

def parse_binary(item :str, symbols = "FB") -> int:
    """
    Transform a string comprised of two possible symbols encoding 0 and 1 to a number

    Args:
        item: string to work on
        symbols: string to map 0 and 1; first character = 0, second character = 1

    Returns:
        Resulting integer number
    """
    symbol_map = {
        symbols[0]: 0,
        symbols[1]: 1,
    }
    target_range = range(len(item) - 1, -1, -1)
    item_enumerated = list(zip(
        target_range,
        map(lambda x: symbol_map[x], item),
    ))
    logger.debug("item_enumerated: {}".format(item_enumerated))

    number_list = map(lambda x: x[1] * pow(2, x[0]), item_enumerated)
    number = reduce(lambda x, y: x + y, number_list)
    logger.debug("number: {}".format(number))

    return(number)

def read_boarding_pass(boarding_pass :str) -> dict:
    """
    Split the boarding pass into two binary numbers with different symbols

    Args:
        boarding_pass: single encoded boarding pass

    Returns:
        Dictionary of items from the boarding pass with keys: row_id, col_id, seat_id
    """
    row_id = parse_binary(boarding_pass[:7], symbols = "FB")
    col_id = parse_binary(boarding_pass[7:], symbols = "LR")
    seat_id = row_id * 8 + col_id

    result = dict(row_id = row_id, col_id = col_id, seat_id = seat_id)
    logger.debug("boarding_pass: {}, col_id: {}, row_id: {}, seat_id: {}".format(
        boarding_pass, col_id, row_id, seat_id
    ))
    return(result)

def find_missing(seat_ids :list) -> int:
    """
    Discern which of all possible seat_ids are missing

    Args:
        seat_ids: list of decoded boarding pass ids with keys: row_id, col_id, seat_id

    Returns:
        Integer of the seat_id of the missing seat
    """
    numbers = sorted(list(map(lambda x: x["seat_id"], seat_ids)))
    logger.debug("numbers: {}".format(numbers))
    target_prev_number = filter(lambda x: x[0] + 1 != x[1], zip(numbers[:-1], numbers[1:]))
    result = next(target_prev_number, None)[0] + 1
    logger.debug("result: {}".format(result))

    return(result)

def main(args :list) -> Union[int, str]:
    """
    Apply all day 5 functions in sequence

    Args:
        args: dictionary of input arguments as passed by docopt in aoc2020
    """
    input_list = args["-"]
    
    seat_ids = list(map(lambda x: read_boarding_pass(x), input_list))

    if not args["--find-missing"]:
        result = max(map(lambda x: x["seat_id"], seat_ids))
    else:
        result = find_missing(seat_ids)

    return(result)


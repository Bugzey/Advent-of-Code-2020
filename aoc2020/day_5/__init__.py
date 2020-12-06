"""
Advent of code 2020 - Day 5

Usage:
    day_5 [options] [-]

Options:
    -h, --help  Print this help message and exit
"""
from functools import reduce
import logging

logger = logging.getLogger(__name__)

def parse_binary(item :str, symbols = "FB") -> int:
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

def read_boarding_pass(boarding_pass :str) -> int:
    row_id = parse_binary(boarding_pass[:7], symbols = "FB")
    col_id = parse_binary(boarding_pass[7:], symbols = "LR")
    seat_id = row_id * 8 + col_id
    logger.debug("boarding_pass: {}, col_id: {}, row_id: {}, seat_id: {}".format(
        boarding_pass, col_id, row_id, seat_id
    ))
    return(seat_id)

def main(args):
    input_list = args["-"]
    
    seat_ids = list(map(lambda x: read_boarding_pass(x), input_list))
    result = max(seat_ids)
    return(result)


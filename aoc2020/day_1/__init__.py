"""
Advent of code 2020 Day 1 package

Usage:
    day_1 [options] [-]

Options:
    -n, --element-count=N   How many elemnts to look for [default: 2]
    -h, --help      Print this message and exit
"""
from functools import reduce
from itertools import chain
import logging
import sys

logger = logging.getLogger(__name__)

def find_quotient(input_list, sum_to = 2020, n = 2):
    """
    Find which elements from input_list sum up to a given number and return their product

    Args:
        input_list: list of integers to search in
        sum_to: the sum of pairs of list elements for which to search for [default: 2020]
    """
    sorted_input = sorted(input_list)
    complements = map(lambda x: sum_to - x, sorted_input)
    pairs = zip(sorted_input, complements)
    if n <= 2:
        target = filter(lambda x: x[1] in sorted_input, pairs)
    else:
        target = map(
            lambda x: (*x[:-1], find_quotient(input_list = sorted_input, sum_to = x[-1], n = n - 1)),
            pairs,
        )
        target = filter(lambda x: all((item is not None for item in x)), target)
    result = next(target, None)
    if result:
        while any(map(lambda x: type(x) == tuple, result)):
            result = tuple(chain(result[:-1], result[-1]))
    logger.debug("result: {}".format(result))
    return(result)

def main(args):
    """
    Process main function

    Args:
        args: output from docopt.docopt of runner function
    """
    n = int(args["--element-count"])
    input_list = filter(lambda x: x.isdigit(), args["-"])
    input_list = map(lambda x: int(x), input_list)
    result = find_quotient(input_list = input_list, sum_to = 2020, n = n)
    result = reduce(lambda x, y: x * y, result)
    return(result)


"""
Advent of code 2020 Day 1 package

Usage:
    aoc2020.day_1 [options] [-]

Options:
    -n, --element-count=N   How many elemnts to look for [default: 2]
    -b, --benchmark  Whether to benchmark the main execution
    --runs=RUNS     Number of benchmark runs [default: 1000]
    -v, --verbose   Display verbose output
    -h, --help      Print this message and exit
"""

from functools import reduce
from itertools import chain
import logging
import docopt
import sys
import timeit

#   Header
import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(msg)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


def parse_input(argv = sys.argv[1:]):
    """
    Parse user input from the console using docopt

    Args:
        argv: command arguments [default: sys.argv[1:]

    Returns:
        A dictionary of processed input arguments and options
    """
    args = docopt.docopt(doc = __doc__, argv = argv)

    global logger
    if args["--verbose"]:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.debug("raw_args: {}".format(args))

    input_list = []
    try:
        while True:
            input_list.append(input())
    except KeyboardInterrupt:
        print("\n")
        sys.exit(1)
    except EOFError:
        pass

    input_list = filter(lambda x: x.isdigit(), input_list)
    input_list = list(map(lambda x: int(x), input_list))
    args["-"] = input_list

    return(args)

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

def main(raw_args = sys.argv[1:]):
    """
    Process main function

    Args:
        raw_args: raw command line arguments to pass downstream [default: sys.argv[1:]]
    """
    args = parse_input(raw_args)
    logger.debug("args: {}".format(args))
    n = int(args["--element-count"])

    if args["--benchmark"]:
        nr_runs = int(args["--runs"])
        logger.debug("Benchmarking function for {} runs".format(nr_runs))
        def wrapper(fun, *args, **kwargs):
            def wrapped():
                return(fun(*args, **kwargs))
            return(wrapped)

        wrapped = wrapper(find_quotient, input_list = args["-"], sum_to = 2020, n = n)
        avg_execution_time = timeit.timeit(wrapped, number = nr_runs)
        logger.info("Average execution time: {}".format(avg_execution_time))
        result = wrapped()
    else:
        logger.debug("Running function normally")
        result = find_quotient(input_list = args["-"], sum_to = 2020, n = n)

    result = reduce(lambda x, y: x * y, result)
    print(result)


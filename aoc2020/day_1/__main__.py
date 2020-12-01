"""
Advent of code 2020 Day 1 package

Usage:
    aoc2020.day_1 [options] [-]

Options:
    -b, --benchmark Whether to benchmark the main execution
    --runs=RUNS     Number of benchmark runs [default: 1000]
    -v, --verbose   Display verbose output
    -h, --help      Print this message and exit
"""

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

def find_quotient(input_list, sum_to = 2020):
    """
    Find which elements from input_list sum up to a given number and return their product

    Args:
        input_list: list of integers to search in
        sum_to: the sum of pairs of list elements for which to search for [default: 2020]
    """
    sorted_input = sorted(input_list)
    complements = map(lambda x: sum_to - x, sorted_input)
    pairs = zip(range(len(sorted_input)), sorted_input, complements)
    target = list(filter(lambda x: x[2] in sorted_input, pairs))[0]
    result = target[1] * target[2]
    return(result)

def main(raw_args = sys.argv[1:]):
    """
    Process main function

    Args:
        raw_args: raw command line arguments to pass downstream [default: sys.argv[1:]]
    """
    args = parse_input(raw_args)
    logger.debug("args: {}".format(args))

    if args["--benchmark"]:
        nr_runs = int(args["--runs"])
        logger.debug("Benchmarking function for {} runs".format(nr_runs))
        def wrapper(fun, *args, **kwargs):
            def wrapped():
                return(fun(*args, **kwargs))
            return(wrapped)

        wrapped = wrapper(find_quotient, input_list = args["-"], sum_to = 2020)
        avg_execution_time = timeit.timeit(wrapped, number = nr_runs)
        logger.info("Average execution time: {}".format(avg_execution_time))
        result = wrapped()
    else:
        logger.debug("Running function normally")
        result = find_quotient(input_list = args["-"], sum_to = 2020)

    print(result)

if __name__ == "__main__":
    main()


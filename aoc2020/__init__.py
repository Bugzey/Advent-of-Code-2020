"""
Advent of code 2020

Usage:
    aoc2020 [options] <command> [<args>..] [-]
    aoc2020 --help

Options:
    -b, --benchmark  Whether to benchmark the main execution
    --runs=RUNS     Number of benchmark runs [default: 1000]
    -v, --verbose   Display verbose output
    -h, --help      Print this message and exit

Commands:
    day_1   Run day_1 code
    day_2   Run day_2 code
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
    args = docopt.docopt(doc = __doc__, argv = argv, help = False)

    global logger
    if args["--verbose"]:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    logger.debug("raw_args: {}".format(args))

    #   Command selection
    command = args["<command>"]
    if command == "day_1":
        import aoc2020.day_1 as package
    elif command == "day_2":
        import aoc2020.day_2 as package
    else:
        command = None
        package = None

    args["package"] = package

    if args["--help"] and command:
        print(package.__doc__)
        sys.exit(0)
    elif args["--help"] and not command:
        print(__doc__)
        sys.exit(0)

    input_list = []
    try:
        while True:
            input_list.append(input())
    except KeyboardInterrupt:
        print("\n")
        sys.exit(1)
    except EOFError:
        pass

    input_list = list(filter(lambda x: x, input_list))
    args["-"] = input_list
    return(args)


def main(raw_args = sys.argv[1:]):
    """
    Process main function

    Args:
        raw_args: raw command line arguments to pass downstream [default: sys.argv[1:]]
    """
    args = parse_input(raw_args)
    logger.debug("args: {}".format(args))
    command = args["<command>"]

    if command == "day_1":
        import aoc2020.day_1 as day
    elif command == "day_2":
        import aoc2020.day_2 as day
    else:
        logger.error("Unknown command: {}".format(command))
        print(__doc__)
        sys.exit(1)

    if args["--help"]:
        print(day.__doc__)
        sys.exit(0)

    fun = lambda: day.main(args)

    if args["--benchmark"]:
        nr_runs = int(args["--runs"])
        logger.debug("Benchmarking function for {} runs".format(nr_runs))
        def wrapper(fun, *args, **kwargs):
            def wrapped():
                return(fun(*args, **kwargs))
            return(wrapped)

        wrapped = wrapper(fun)
        avg_execution_time = timeit.timeit(wrapped, number = nr_runs)
        logger.info("Average execution time: {}".format(avg_execution_time))
        result = wrapped()
    else:
        logger.debug("Running function normally")
        result = fun()

    print(result)
    return(result)

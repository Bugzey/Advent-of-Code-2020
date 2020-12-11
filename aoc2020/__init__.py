"""
Advent of code 2020

Usage:
    aoc2020 [options] <command> [<args>...]
    aoc2020 --help

Options:
    -b, --benchmark  Whether to benchmark the main execution
    --runs=RUNS     Number of benchmark runs [default: 1000]
    -v, --verbose   Display verbose output
    -h, --help      Print this message and exit

Commands:
    day_1   Day 1: Report Repair
    day_2   Day 2: Password Philosophy
    day_3   Day 3: Toboggan Trajectory
    day_4   Day 4: Passport Processing
    day_5   Day 5: Binary Boarding
    day_6   Day 6: Day 6: Custom Customs
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
        A tuple of dictionaries, each of which is produced by docopt(<global arguments>, <command
        arguments>)
    """
    args = docopt.docopt(
        doc = __doc__,
        argv = argv,
        options_first = True,
    )

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
    elif command == "day_3":
        import aoc2020.day_3 as package
    elif command == "day_4":
        import aoc2020.day_4 as package
    elif command == "day_5":
        import aoc2020.day_5 as package
    elif command == "day_6":
        import aoc2020.day_6 as package
    else:
        command = None
        package = None

    args["package"] = package
    logger.debug("package: {}".format(package))

    if args["--help"] and command:
        print(package.__doc__)
        sys.exit(0)
    elif args["--help"] and not command:
        print(__doc__)
        sys.exit(0)
    elif command:
        raw_command_args = args["<args>"]
        logger.debug("raw_command_args: {}".format(raw_command_args))
        command_args = docopt.docopt(package.__doc__, argv = raw_command_args)
        logger.debug("command_args: {}".format(command_args))

    input_list = []
    try:
        while True:
            input_list.append(input())
    except KeyboardInterrupt:
        print("\n")
        sys.exit(1)
    except EOFError:
        pass

    #input_list = list(filter(lambda x: x, input_list))
    while not input_list[-1]:
        _ = input_list.pop()

    command_args["-"] = input_list
    return(args, command_args)


def main(raw_args = sys.argv[1:]):
    """
    Run the associated sub-package main function

    Args:
        raw_args: raw command line arguments to pass downstream [default: sys.argv[1:]]
    """
    args, command_args = parse_input(raw_args)
    logger.debug("args: {}".format(args))
    command = args["<command>"]

    fun = lambda: args["package"].main(command_args)

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

    if type(result) in [list, tuple]:
        print(*result, sep = "\n")
    else:
        print(result)

    return(result)


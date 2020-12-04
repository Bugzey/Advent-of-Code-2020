"""
Advent of code 2020 Day 3 package

Usage:
    day_1 [options] [-]

Options:
    -d, --step-down=STEP    How many steps down to go [default: 1]
    -r, --step-right=STEP    How many steps rigth to go [default: 3]
    -h, --help      Print this message and exit
"""
import logging
logger = logging.getLogger(__name__)

def parse_map(input_list):
    """
    Convert the input list consisting of rows of dots and hashes to an integer map - each list
    member shows the indices of trees (hashes)

    Args:
        input_list: list of input strings

    Returns:
        A tuple of (map_width, map_height, parsed_map) where parsed_map is the integer map
    """
    map_width = len(input_list[0])
    map_height = len(input_list)
    parsed_map = list(map(
        lambda x: tuple(index for index, item in enumerate(x[1]) if item == "#"),
        enumerate(input_list)
    ))
    return(map_width, map_height, parsed_map)

def count_trees(map_width, map_height, parsed_map, step_right, step_down):
    """
    Count occurences where we would hit a tree when moving down and left at particular steps
    along a parsed integer map

    Args:
        map_width: width of the parsed map that is then looped along its width
        map_height: height of the parsed map
        parsed_map: integer map of tree positions
        step_right: how many steps to the right we take at each step
        step_down: how many steps down we take at each step

    Returns:
        The number of times our current position corresponds to a tree in the integer map
    """
    down_count = map_height // step_down
    right_count = map_width // step_right

    logger.debug("down_count: {}, right_count: {}".format(
        down_count, right_count
    ))
    down_range = range(0, map_height, step_down)
    right_range = range(0, down_count * step_right, step_right)
    logger.debug("down_range: {}, right_range: {}".format(
        down_range, right_range
    ))

    step_positions = list(map(lambda x, y: (x, y % map_width), down_range, right_range))

    logger.debug("step_positions. {}".format(step_positions))

    tree_hits = map(lambda x: x[1] in parsed_map[x[0]], step_positions)
    result = sum(tree_hits)
    return(result)

def main(args):
    """
    Combine all steps from this day's puzzle

    Args:
        args: input arguments as output by the main runner using docopt

    Returns:
        The number of trees encountered
    """
    input_list = args["-"]
    step_down = int(args["--step-down"])
    step_right = int(args["--step-right"])
    map_width, map_height, parsed_map = parse_map(input_list)

    tree_count = count_trees(
        map_width = map_width,
        map_height = map_height,
        parsed_map = parsed_map,
        step_down = step_down,
        step_right = step_right,
    )
    return(tree_count)


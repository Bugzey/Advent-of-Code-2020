"""
Advent of code 2020 Day 3 package

Usage:
    day_1 [options] [(-r RIGHT -d DOWN)]...  [-]
    day_1 [--help]

Options:
    -d, --step-down=STEP    How many steps down to go [default: 1]
    -r, --step-right=STEP    How many steps rigth to go [default: 3]
    --visualise     Whether ot visualise the result
    --save-to=FILE     Where to save the visualisation
    -h, --help      Print this message and exit
"""
from functools import reduce
import logging
import os

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

def get_positions(map_width, map_height, parsed_map, step_right, step_down):
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

    logger.debug("step_down: {}, step_right: {}".format(
        step_down, step_right)
    )
    logger.debug("down_count: {}, right_count: {}".format(
        down_count, right_count
    ))
    down_range = range(0, down_count * step_down, step_down)
    right_range = range(0, down_count * step_right, step_right)
    logger.debug("down_range: {}, right_range: {}".format(
        down_range, right_range
    ))

    step_positions = list(map(lambda x, y: (x, y % map_width), down_range, right_range))
    logger.debug("step_positions. {}".format(step_positions))

    return(step_positions)

def count_trees(parsed_map, step_positions):
    tree_hits = map(lambda x: x[1] in parsed_map[x[0]], step_positions)
    sum_trees = sum(tree_hits)
    logger.debug("sum_trees: {}".format(sum_trees))
    return(sum_trees)

def visualise_run(raw_map :list, step_positions):
    """
    Show which positions in the input map are hit

    Args:
        raw_map: the input map as a list of strings
        step_positions: list of tuples of positions on the map

    Returns:
        The original raw_map with positions overlapping with trees marked as X and non-overlapping
        positions as O
    """
    result = raw_map.copy()
    for x, y in step_positions:
        row = result[x]
        logger.debug("x: {}, y: {}".format(x, y))
        is_tree = result[x][y] == "#"
        result[x] = "{}{}{}".format(
            row[:y], ("X" if is_tree else "O"), row[(y + 1):]
        )

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
    steps = list(map(
        lambda x, y: dict(step_down = int(x), step_right = int(y)),
        args["--step-down"],
        args["--step-right"],
    ))
    map_width, map_height, parsed_map = parse_map(input_list)

    step_positions = list(map(
        lambda step: get_positions(
            map_width = map_width,
            map_height = map_height,
            parsed_map = parsed_map,
            step_down = step["step_down"],
            step_right = step["step_right"],
        ),
        steps
    ))

    if args["--visualise"]:
        if len(steps) > 1:
            logger.warning(
                "Only visualising first step pair: {}".format(steps[0])
            )
        visualised_map = visualise_run(
            raw_map = args["-"],
            step_positions = step_positions[0],
        )

    if args["--save-to"]:
        output_file_name = os.path.expanduser(args["--save-to"])
        logger.info("Saving output to: {}".format(output_file_name))
        with open(output_file_name , "w") as cur_file:
            cur_file.write("\n".join(visualised_map))

    elif args["--visualise"]:
        print(*visualised_map, sep = "\n")

    trees = list(map(lambda x: count_trees(parsed_map, x), step_positions))
    message_list = (
        "steps: {}, trees: {}".format(steps, trees) \
        for steps, trees in zip(steps, trees)
    )
    logger.debug(", ".join(message_list))
    total_tree_count = reduce(lambda x, y: x * y, trees)

    result = [*trees, total_tree_count]
    return(result)


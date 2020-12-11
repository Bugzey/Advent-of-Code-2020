"""
Advent of code 2020 - Day 7

Usage:
    day_7 [options] [-]

Options:
    -t --target-bag=BAG  Target bag to look for [default: shiny gold bag]
    -h, --help  Print this help message and exit
"""
from functools import reduce
import logging
import re

logger = logging.getLogger(__name__)

def parse_input(input_list :list) -> dict:
    """
    Create a dictionary with dictionaries - a key denotes the unique bag name; the value is a dict
    of keys of other dictionaries that fit int hat bag and how many fit inside

    Args:
        input_list: raw input data

    Return:
        Dictionary
    """
    pattern = r"(\d+) (.+bag)s*\.*"
    items_split = {
        item[0]: [re.search(pattern, sub_item) for sub_item in item[1].split(", ")] \
        for item in map(lambda x: x.split(" contain "), input_list)
    }
    logger.debug("items_split: {}".format(items_split))

    result = {
        key.replace("bags", "bag"): dict({
            match.group(2): int(match.group(1)) \
            for match in value \
            if match
        }) for key, value in items_split.items()
    }
    logger.debug("result: {}".format(result))
    return(result)

def check_contains(bags, source_bag, target_bag):
    def recurse(bags, cur_bag, target_bag, visited = []):
        possible_bags = bags[cur_bag].keys()
        if not possible_bags:
            return False, visited
        elif target_bag in possible_bags:
            return True, [*visited, target_bag]

        result = False
        for bag in possible_bags:
            if bag in visited:
                continue

            visited.append(bag)
            new_result, visited = recurse(bags, bag, target_bag, visited)
            result = result or new_result

        return(result, visited)

    result, visited = recurse(bags, cur_bag = source_bag, target_bag = target_bag)
    logger.debug("source_bag: {}, result: {}, visited: {}".format(
        source_bag, result, visited
    ))
    return(result)

def sum_contains(bags, target_bag):
    result_list = map(lambda x: \
        check_contains(
            bags = bags,
            source_bag = x,
            target_bag = target_bag,
        ),
        bags.keys()
    )
    result = sum(result_list)
    return(result)

def main(args):
    input_list = args["-"]
    target_bag = args.get("--target-bag")
    bags = parse_input(input_list)
    result = {key: check_contains(bags, key, target_bag) for key in bags}
    return(sum(result.values()))


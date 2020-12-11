"""
Advent of code 2020 - Day 6

Usage:
    day_6 [options] [-]

Options:
    -e, --every  Sum the questions where everyone answered yes
    -h, --help  Print this help message and exit
"""
from functools import reduce
import logging

logger = logging.getLogger(__name__)

def split_groups(input_list :list) -> list:
    """
    Splits the input into lists of answers to a question using blank input lines as
    delimiters

    Args:
        input_list: list of the input data - each item is a row of stdin

    Returns:
        A list of group inputs where each list element is a list of separate answers
    """
    which_blank = list(filter(
        lambda x: input_list[x] == "", range(len(input_list))
    ))
    indices = list(zip(
        (0, *which_blank),
        (*which_blank, len(input_list)),
    ))
    logger.debug(indices)
    result = [list(filter(lambda x: x != "", input_list[first:second])) for first, second in indices]
    return(result)

def get_group_sets(answer_list: list) -> list:
    """
    Return a list containing sets of unique answers for each group

    Args:
        answer_list: cleaned list of input data as returned by split_groups

    Returns:
        A list of sets where each set are unique answers for that group
    """
    group_sets = list(map(lambda x: set().union(*[set(item) for item in x]), answer_list))
    logger.debug("group_sets: {}".format(group_sets))
    return(group_sets)

def get_common_answers(answer_list: list) -> list:
    """
    Return a list containing an intersection of answers given by each group

    Args:
        answer_list: cleaned list of input data as returned by split_groups

    Returns:
        A list of sets where each set holds common answers for that group
    """
    common_answers = list(map(lambda x: set(x[0]).intersection(*[set(item) for item in x[1:]]), answer_list))
    logger.debug("common_answers: {}".format(common_answers))
    return(common_answers)

def sum_unique_answers(group_sets :list) -> int:
    """
    Sum the length of sets in a list. Usable for both parts of day 6's task

    Args:
        group_sets: list of any sets

    Returns:
        The sum of lengths of all sets in the input group
    """
    result = sum(map(lambda x: len(x), group_sets))
    return(result)

def main(args):
    input_list = args["-"]
    answer_list = split_groups(input_list)

    if not args["--every"]:
        group_sets = get_group_sets(answer_list)
        result = sum_unique_answers(group_sets)
    else:
        common_answers = get_common_answers(answer_list)
        result = sum_unique_answers(common_answers)

    return(result)


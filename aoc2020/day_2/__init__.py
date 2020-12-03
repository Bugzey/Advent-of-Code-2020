"""
Advent of code 2020 - Day 2

Usage:
    day_2 [options] [-]

Options:
    -n, --new   Whether to use the new (puzzle part 2) method
    -h, --help  Print this help message and exit
"""
import re

def parse_row(row):
    rules, password = row.split(": ")
    counts, char = rules.split(" ")
    min_count, max_count = map(
        lambda x: int(x) if x.isdigit else None, counts.split("-")
    )

    return(min_count, max_count, char, password)

def validate_password(min_count, max_count, char, password):
    char_list = re.findall(char, password)
    result = len(char_list) >= min_count and len(char_list) <= max_count
    return(result)

def new_validate_password(min_count, max_count, char, password):
    def xor(a, b):
        result = (a and not b) or (b and not a)
        return(result)

    result = xor(
        a = password[min_count - 1] == char,
        b = password[max_count - 1] == char,
    )
    return(result)

def main(args):
    count = 0
    input_list = args["-"]
    fun = new_validate_password if args["--new"] else validate_password
    for row in input_list:
        min_count, max_count, char, password = parse_row(row)
        valid_password = fun(
            min_count, max_count, char, password
        )
        if valid_password:
            count = count + 1

    return(count)


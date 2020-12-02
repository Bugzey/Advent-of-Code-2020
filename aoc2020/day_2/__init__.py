"""
Advent of code 2020 - Day 2

Usage:
    day_2 [options] [-]

Options:
    -v, --verbose   Verbose output
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

def main(args):
    count = 0
    input_list = args["-"]
    for row in input_list:
        min_count, max_count, char, password = parse_row(row)
        valid_password = validate_password(
            min_count, max_count, char, password
        )
        if valid_password:
            count = count + 1

    return(count)


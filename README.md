#	Advent of Code 2020
##	Description
This is my entry for the 2020 edition of the infamous Advent of Code series of programming
challenges. Each day between 1. Dec and 25. Dec a new challenge is posted on the website
(https://adventofcode.com/2020/). Each puzzle consists of two parts, the second of which unlocks
after the first one is successfully completed.

##	Installation
Clone this repository via `git clone`. A setuptools installation config might be added in the
future.

##	Usage
The project is structured as an overarching package `aoc2020` whose subpackages correspond to the
individual days of the programming challenge. The main package handles CLI input and dispatching
arguments to child packages' main function. Children should not be run directly.

```
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
    day_1   Run day_1 code
    day_2   Run day_2 code
```


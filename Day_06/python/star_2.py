from aoc import aoc_read_input
from typing import List
from os import path
from collections import Counter


def transform_input(input_val):
    n_people = len(input_val)
    return len([x for x in Counter("".join(input_val)).values() if x == n_people])


def func1(input_vals):
    return sum(input_vals)


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__), split_empytline=True)
    input_vals = map(transform_input, input_vals)
    print(func1(input_vals))

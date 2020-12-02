from aoc import aoc_read_input
from os import path
from typing import List
from itertools import combinations


def transform_input(input_vals: List) -> List:
    return [int(val) for val in input_vals]


def func1(input_vals: List):
    total = 2020
    for expens in combinations(input_vals, 3):
        if sum(expens) == total:
            return expens[0] * expens[1] * expens[2]


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = transform_input(input_vals)
    print(func1(input_vals))

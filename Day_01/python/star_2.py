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


def get_complements(input_vals: List, total: int):
    history = {}
    for idx, val in enumerate(input_vals):
        try:
            result = history[val]
            return result * val
        except KeyError:
            history[total - val] = val
    return 0


def func2(input_vals: List):
    total = 2020
    for idx, val in enumerate(input_vals):
        complement = total - val
        if (result := get_complements(input_vals[idx + 1 :], complement)) :
            return val * result


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = transform_input(input_vals)
    print(func1(input_vals))
    print(func2(input_vals))

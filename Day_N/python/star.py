from aoc import aoc_read_input
from typing import List
from os import path


def transform_input(input_val: str):
    return input_val


def func1(input_vals):
    return None


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = map(transform_input, input_vals)
    print(func1(input_vals))

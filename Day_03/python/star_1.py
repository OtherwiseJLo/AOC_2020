from aoc import aoc_read_input
from typing import List
from os import path
import numpy as np
from sys import exit


def convert_to_numeric(char: str) -> int:
    if char == ".":
        return 0
    elif char == "#":
        return 1
    else:
        exit()


def transform_input(input_val: str):
    return np.array(map(convert_to_numeric, list(input_val)))


def func1(input_vals):
    return None


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = np.stack(map(transform_input, input_vals))
    print(func1(input_vals))

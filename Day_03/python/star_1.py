from aoc import aoc_read_input
from typing import List
from os import path
import numpy as np
import sys


def convert_to_numeric(char: str) -> int:
    if char == ".":
        return 0
    elif char == "#":
        return 1
    else:
        sys.exit()


def transform_input(input_val: str):
    return np.array(list(map(convert_to_numeric, list(input_val))))


def func1(input_vals, dx, dy):
    counter = 0
    x_idx = 0
    y_idx = 0
    while y_idx < input_vals.shape[0] - dy:
        x_idx = (x_idx + dx) % input_vals.shape[1]
        y_idx += dy
        counter += input_vals[y_idx][x_idx]
    return counter


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = np.stack(list(map(transform_input, input_vals)))
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = [func1(input_vals, dx, dy) for dx, dy in slopes]
    print(trees)
    prod = 1
    for tree in trees:
        prod *= tree
    print(prod)

from aoc import aoc_read_input  # set by aoc_env.sh
from typing import List
from os import path


def func1(input_vals: List):
    total = 2020
    for idx, expense in enumerate(input_vals):
        if (complement := total - expense) in input_vals[idx:]:
            return expense * complement


def func2(expenses: List) -> int:
    history = {}
    total = 2020
    for expense in expenses:
        try:
            return history[expense] * expense
        except KeyError:
            complement = total - expense
            history[complement] = expense


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = [int(val) for val in input_vals]
    print(func2(input_vals))

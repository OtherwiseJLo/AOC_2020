from aoc import aoc_read_input
import re
from typing import List, Dict
from os import path


def transform_input(input_val: str):
    low_to_high, letter, password = input_val.split(" ")
    lowest, highest = [int(x) for x in low_to_high.split("-")]
    letter = letter.split(":")[0]
    password = password.strip()
    return {
        "lowest": lowest,
        "highest": highest,
        "letter": letter,
        "password": password,
    }


def func1(input_vals):
    matches = re.findall(input_vals["letter"], input_vals["password"])
    return (n_matches := len(matches)) >= input_vals[
        "lowest"
    ] and n_matches <= input_vals["highest"]


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = map(transform_input, input_vals)
    print(sum(map(func1, input_vals)))

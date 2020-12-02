from aoc import aoc_read_input
from typing import List
from os import path


def transform_input(input_val: str) -> dict:
    positions, letter, password = input_val.split(" ")
    p1, p2 = [int(x) for x in positions.split("-")]
    letter = letter.split(":")[0]
    password = password.strip()
    return {
        "p1": p1 - 1,
        "p2": p2 - 1,
        "letter": letter,
        "password": password,
    }


def func1(input_val: List):
    cond1 = input_val["password"][input_val["p1"]] == input_val["letter"]
    cond2 = input_val["password"][input_val["p2"]] == input_val["letter"]
    return (not (cond1 and cond2)) and (cond1 or cond2)


if __name__ == "__main__":
    input_vals = aoc_read_input(path.abspath(__file__))
    input_vals = map(transform_input, input_vals)
    print(sum(map(func1, input_vals)))

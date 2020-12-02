from typing import List


def get_input_filepath(day_fp) -> str:
    """
    Grabs the path for the input file for the day's puzzle.
    """
    return "/".join(day_fp.split("/")[:-2]) + "/input"


def aoc_read_input(day_fp: str) -> List:
    input_filepath = get_input_filepath(day_fp)
    with open(input_filepath, "r") as f:
        return [line.strip() for line in f.readlines()]

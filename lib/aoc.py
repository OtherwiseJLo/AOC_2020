from typing import List


def get_input_filepath(day_fp) -> str:
    """
    Grabs the path for the input file for the day's puzzle.
    """
    return "/".join(day_fp.split("/")[:-2]) + "/input"


def aoc_read_input(day_fp: str, split_empytline=False) -> List:
    input_filepath = get_input_filepath(day_fp)
    with open(input_filepath, "r") as f:
        content = [line.strip() for line in f.readlines()]
    result = []
    if split_empytline:
        group = []
        for val in content:
            if val:
                group.append(val)
            else:
                result.append(group)
                group = []
        result.append(group)
        return result
    return content

from typing import Dict
import re


def password_input(line: str) -> Dict:
    positions, letter, password = line.split(" ")
    p1, p2 = [int(x) for x in positions.split("-")]
    letter = letter.split(":")[0]
    password = password.strip()
    return {
        "p1": p1 - 1,
        "p2": p2 - 1,
        "letter": letter,
        "password": password,
    }


def check_is_valid(password_input: Dict) -> bool:
    cond1 = password_input["password"][password_input["p1"]] == password_input["letter"]
    cond2 = password_input["password"][password_input["p2"]] == password_input["letter"]
    return (not (cond1 and cond2)) and (cond1 or cond2)


if __name__ == "__main__":
    with open("input", "r") as f:
        passwords = [password_input(line.strip()) for line in f.readlines()]
        print(sum(map(check_is_valid, passwords)))

from typing import Dict
import re


def password_input(line: str) -> Dict:
    low_to_high, letter, password = line.split(" ")
    lowest, highest = [int(x) for x in low_to_high.split("-")]
    letter = letter.split(":")[0]
    password = password.strip()
    return {
        "lowest": lowest,
        "highest": highest,
        "letter": letter,
        "password": password,
    }


def check_is_valid(password_input: Dict) -> bool:
    matches = re.findall(password_input["letter"], password_input["password"])
    return (n_matches := len(matches)) >= password_input[
        "lowest"
    ] and n_matches <= password_input["highest"]


if __name__ == "__main__":
    with open("input", "r") as f:
        passwords = [password_input(line.strip()) for line in f.readlines()]
        print(sum(map(check_is_valid, passwords)))

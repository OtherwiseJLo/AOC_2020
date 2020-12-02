from itertools import combinations

with open("input", "r") as f:
    expenses = [int(expense.strip()) for expense in f.readlines()]

total = 2020
for expens in combinations(expenses, 3):
    if sum(expens) == total:
        product = expens[0] * expens[1] * expens[2]
        print(f"Product is {product}")

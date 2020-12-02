with open("input", "r") as f:
    expenses = [int(expense.strip()) for expense in f.readlines()]

total = 2020
for idx, expense in enumerate(expenses):
    if (complement := total - expense) in expenses[idx:]:
        print(f"Expense values are {expense} and {complement}")
        print(f"Product is {expense*complement}")

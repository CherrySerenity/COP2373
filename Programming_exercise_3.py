from functools import reduce

def main():
    expenses = []

    num_expenses = int(input("How many expenses do you want to enter? "))

    for i in range(num_expenses):
        expense_type = input(f"Enter expense #{i + 1} name: ")
        amount = float(input(f"Enter amount for {expense_type}: $"))

        expenses.append((expense_type, amount))

    # Total using reduce
    total_expense = reduce(lambda total, item: total + item[1], expenses, 0)

    # Highest and lowest expenses
    highest = max(expenses, key=lambda item: item[1])
    lowest = min(expenses, key=lambda item: item[1])

    print("\n----- Monthly Expense Report -----")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")

main()
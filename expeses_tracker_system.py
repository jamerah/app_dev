# EXPENSE TRACKER SYSTEM

budget = 0
expenses = []


def set_budget():
    global budget

    budget = float(input("Enter your budget: ₱"))
    print("Budget successfully set!")


def add_expense():
    description = input("Enter expense name: ")
    amount = float(input("Enter expense amount: ₱"))

    expense = {
        "description": description,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("\nNo expenses found.")
        return

    print("\n===== EXPENSE LIST =====")

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['description']} "
            f"- ₱{expense['amount']:.2f}"
        )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: ₱{total:.2f}")


def remaining_balance():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    balance = budget - total

    print(f"\nBudget: ₱{budget:.2f}")
    print(f"Total Expenses: ₱{total:.2f}")
    print(f"Remaining Balance: ₱{balance:.2f}")


def delete_expense():
    show_expenses()

    if len(expenses) == 0:
        return

    number = int(input("\nEnter expense number to delete: "))

    if number >= 1 and number <= len(expenses):
        deleted = expenses.pop(number - 1)

        print(
            f"{deleted['description']} "
            f"has been deleted."
        )
    else:
        print("Invalid expense number.")


# MAIN PROGRAM

while True:

    print("\n==============================")
    print("       EXPENSE TRACKER")
    print("==============================")
    print(f"Budget: ₱{budget:.2f}")
    print("------------------------------")
    print("1. Set Budget")
    print("2. Add Expense")
    print("3. Expenses List")
    print("4. Total Expenses")
    print("5. Remaining Balance")
    print("6. Delete Expense")
    print("7. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        set_budget()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        show_expenses()

    elif choice == "4":
        total_expenses()

    elif choice == "5":
        remaining_balance()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")

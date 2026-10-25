# Personal Expense Tracker

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")

def show_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\n--- Your Expenses ---")

        for expense in expenses:
            print(expense["name"], "-", expense["amount"])

def show_total():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expenses:", total)

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice. Please try again.")
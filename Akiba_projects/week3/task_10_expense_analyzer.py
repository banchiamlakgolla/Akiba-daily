
expenses = [
    {"description": "Lunch", "category": "Food", "amount": 180},
    {"description": "Taxi", "category": "Transport", "amount": 120},
    {"description": "Groceries", "category": "Food", "amount": 450},
    {"description": "Internet", "category": "Bills", "amount": 300}
]


def add_expense(description, category, amount):
    if not description.strip():
        print("Description cannot be empty.")
        return

    if not category.strip():
        print("Category cannot be empty.")
        return

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expense = {
        "description": description.strip(),
        "category": category.strip().title(),
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!")


def calculate_total():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    return total


def spending_by_category():
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals


def find_largest_expense():
    if not expenses:
        return None

    largest = expenses[0]

    for expense in expenses:
        if expense["amount"] > largest["amount"]:
            largest = expense

    return largest


def expenses_above_threshold(threshold=200):
    matching_expenses = []

    for expense in expenses:
        if expense["amount"] > threshold:
            matching_expenses.append(expense)

    return matching_expenses


def category_percentages():
    total = calculate_total()
    category_totals = spending_by_category()
    percentages = {}

    if total == 0:
        return percentages

    for category, amount in category_totals.items():
        percentage = (amount / total) * 100
        percentages[category] = percentage

    return percentages


def highest_spending_category():
    category_totals = spending_by_category()

    if not category_totals:
        return None

    highest_category = max(category_totals, key=category_totals.get)

    return highest_category, category_totals[highest_category]


def generate_report(threshold=200):
    print("========== SPENDING REPORT ==========")

    if not expenses:
        print("No expenses recorded.")
        return

    print("\nAll Expenses:")

    for expense in expenses:
        print(
            expense["description"],
            "| Category:", expense["category"],
            "| Amount:", format(expense["amount"], ".2f"), "Birr"
        )

    total = calculate_total()
    print("\nTotal Expenses:", format(total, ".2f"), "Birr")

    print("\nSpending by Category:")
    category_totals = spending_by_category()

    for category, amount in category_totals.items():
        print(category + ":", format(amount, ".2f"), "Birr")
   
    largest = find_largest_expense()

    print("\nLargest Expense:")
    print(
        largest["description"],
        "-", format(largest["amount"], ".2f"), "Birr"
    )

    print("\nExpenses Above", threshold, "Birr:")
    matching_expenses = expenses_above_threshold(threshold)

    if matching_expenses:
        for expense in matching_expenses:
            print(
                expense["description"],
                "-", format(expense["amount"], ".2f"), "Birr"
            )
    else:
        print("No expenses above this threshold.")

    print("\nCategory Percentages:")
    percentages = category_percentages()

    for category, percentage in percentages.items():
        print(category + ":", format(percentage, ".2f") + "%")

    highest = highest_spending_category()

    if highest:
        category, amount = highest
        print("\nHighest Spending Category:", category)
        print("Category Total:", format(amount, ".2f"), "Birr")


def main():
    while True:
        print("\n========== EXPENSE ANALYZER ==========")
        print("1. Add expense")
        print("2. View spending report")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Expense description: ")
            category = input("Expense category: ")

            try:
                amount = float(input("Expense amount (Birr): "))
                add_expense(description, category, amount)
            except ValueError:
                print("Please enter a valid number for the amount.")

        elif choice == "2":
            threshold_input = input(
                "Enter threshold (press Enter for 200 Birr): "
            )

            try:
                if threshold_input.strip() == "":
                    generate_report()
                else:
                    threshold = float(threshold_input)

                    if threshold < 0:
                        print("Threshold cannot be negative.")
                    else:
                        generate_report(threshold)

            except ValueError:
                print("Please enter a valid threshold.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()

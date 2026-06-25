import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "ID",
                "Date",
                "Category",
                "Description",
                "Amount"
            ])


def get_next_id():

    with open(FILE_NAME, "r") as file:

        rows = list(csv.reader(file))

        if len(rows) <= 1:
            return 1

        return int(rows[-1][0]) + 1


def add_expense():

    category = input("Enter Category: ")

    description = input("Enter Description: ")

    amount = float(input("Enter Amount: "))

    date = datetime.now().strftime("%Y-%m-%d")

    expense_id = get_next_id()

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            expense_id,
            date,
            category,
            description,
            amount
        ])

    print("\nExpense Added Successfully\n")


def view_expenses():

    with open(FILE_NAME, "r") as file:

        rows = list(csv.reader(file))

        if len(rows) <= 1:
            print("\nNo Expenses Found\n")
            return

        print()

        print("-" * 80)

        print(
            f"{'ID':<5}"
            f"{'Date':<15}"
            f"{'Category':<15}"
            f"{'Description':<25}"
            f"{'Amount':<10}"
        )

        print("-" * 80)

        for row in rows[1:]:

            print(
                f"{row[0]:<5}"
                f"{row[1]:<15}"
                f"{row[2]:<15}"
                f"{row[3]:<25}"
                f"{row[4]:<10}"
            )


def delete_expense():

    expense_id = input("Enter Expense ID: ")

    rows = []

    found = False

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        rows = list(reader)

    updated = [rows[0]]

    for row in rows[1:]:

        if row[0] == expense_id:

            found = True

        else:

            updated.append(row)

    if not found:

        print("Expense Not Found")

        return

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(updated)

    print("Expense Deleted Successfully")


def monthly_report():

    month = input("Enter Month (YYYY-MM): ")

    total = 0

    category_total = {}

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["Date"].startswith(month):

                amount = float(row["Amount"])

                total += amount

                category = row["Category"]

                category_total[category] = (
                    category_total.get(category, 0)
                    + amount
                )

    print("\n===== MONTHLY REPORT =====")

    print(f"Month: {month}")

    print(f"Total Spending: Rs {total:.2f}")

    print()

    for category, amount in category_total.items():

        print(f"{category}: Rs {amount:.2f}")

    if total == 0:

        print("No Data Found")


def menu():

    initialize_file()

    while True:

        print("\n====== EXPENSE TRACKER ======")

        print("1. Add Expense")

        print("2. View Expenses")

        print("3. Delete Expense")

        print("4. Monthly Report")

        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":

            add_expense()

        elif choice == "2":

            view_expenses()

        elif choice == "3":

            delete_expense()

        elif choice == "4":

            monthly_report()

        elif choice == "5":

            print("Thank You")

            break

        else:

            print("Invalid Choice")


menu()

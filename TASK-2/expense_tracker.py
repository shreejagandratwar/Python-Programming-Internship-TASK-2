import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Function to add expense
def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter amount (₹): "))

    date = datetime.now().strftime("%Y-%m-%d")

    file_exists = os.path.exists(FILE_NAME)

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)

        # Add header only once
        if not file_exists:
            writer.writerow(["Date", "Description", "Amount"])

        writer.writerow([date, description, amount])

    print(" Expense added successfully!\n")


# Function to view expenses
def view_expenses():

    if not os.path.exists(FILE_NAME):
        print(" No expenses found.\n")
        return

    print("\n===== Expense Records =====")

    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)

        next(reader)   # Skip header

        for row in reader:
            print(
                f"Date: {row[0]} | "
                f"Expense: {row[1]} | "
                f"Amount: ₹{row[2]}"
            )

    print()


# Function to calculate total expense
def total_expense():

    total = 0

    if os.path.exists(FILE_NAME):

        with open(FILE_NAME, mode='r') as file:
            reader = csv.reader(file)

            next(reader)

            for row in reader:
                total += float(row[2])

    print(f"\n Total Expense = ₹{total}\n")
    # OPTIONAL: Save total inside CSV file
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([])  # empty line for separation
        writer.writerow(["", "TOTAL", total])


# Main Menu
while True:

    print("====== Expense Tracker ======")
    print("1 → Add New Expense")
    print("2 → View Expenses")
    print("3 → Calculate Total Expense")
    print("4 → Exit")

    choice = input("Enter your choice: ")


    if choice == "1":
        add_expense()


    elif choice == "2":
        view_expenses()


    elif choice == "3":
        total_expense()


    elif choice == "4":
        print("\n Thank you for using Expense Tracker!")
        break


    else:
        print(" Invalid choice! Please try again.\n")

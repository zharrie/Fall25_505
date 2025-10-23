from expenses import Income, Expense
from categories import Category
from file_handler import save_transactions, load_transactions
from reports import generate_report, search_transactions
from datetime import datetime

FILENAME = "transactions.json"

#Prompt the user for a valid date and validate its format.
def input_date(prompt):
    
    while True:
        s = input(prompt)
        if s.lower() == "cancel" or not s.strip():     # Allow user to cancel at date input stage
            return None
        try:
            datetime.strptime(s, "%Y-%m-%d")  # Validate date format
            return s
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

#Handles both income and expense inputs including cancel option.
def record_transaction(transaction_type, transactions, categories):
    
    print(f"\nAdding a new {transaction_type} record... (type 'cancel' at any time to abort)")

    #Amount Input
    amount_input = input(f"Enter {transaction_type} amount: ")
    if amount_input.lower() == "cancel" or not amount_input.strip():
        print("Transaction canceled.")
        return

    #Validate amount input
    try:
        amount = float(amount_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    #Date Input
    date = input_date("Enter date (YYYY-MM-DD): ")
    if date is None:
        print("Transaction canceled.")
        return

    # Give clearer examples for categories depending on the transaction type
    if transaction_type == "income":
        category = input("Enter category (e.g., Salary, Bonus, Freelance): ")
    else:
        category = input("Enter category (e.g., Food, Rent, Utilities): ")

    if category.lower() == "cancel" or not category.strip():
        print("Transaction canceled.")
        return

    #Description Input
    description = input("Enter description: ")
    if description.lower() == "cancel" or not description.strip():
        print("Transaction canceled.")
        return

    #Create the appropriate transaction object
    if transaction_type == "income":
        t = Income(amount, date, category, description).to_dict()
    else:
        t = Expense(amount, date, category, description).to_dict()

        # Update budget if the expense category is predefined
        if category in categories:
            categories[category].add_expense(amount)
            categories[category].check_budget()

    # Add the transaction to the list
    transactions.append(t)
    print(f"{transaction_type.capitalize()} added successfully.")


def main():
    #Main program menu for managing income, expenses, and reports
    # Load all existing transactions from file
    transactions = load_transactions(FILENAME)

    # Predefined categories with budgets
    categories = {
        "Food": Category("Food", 200),
        "Transport": Category("Transport", 100),
        "Entertainment": Category("Entertainment", 150)
    }

    #Main Menu Loop
    while True:
        print("\n--- Expense Tracker Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Report")
        print("4. Search Transactions")
        print("5. Save & Exit")

        choice = input("Enter your choice (or press Enter to exit): ").strip()

        # Handle blank input
        if not choice:
            print("No option entered. Exiting program...")
            break

        #Menu Options
        elif choice == "1":
            record_transaction("income", transactions, categories)

        elif choice == "2":
            record_transaction("expense", transactions, categories)

        elif choice == "3":
            generate_report(transactions)

        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            search_transactions(transactions, keyword)

        elif choice == "5":
            save_transactions(FILENAME, transactions)
            print("Data saved successfully. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

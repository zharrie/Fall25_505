import json

# Function to save all transactions (incomes and expenses) to a file
def save_transactions(filename, transactions):
    try:
        with open(filename, "w") as f:
            json.dump(transactions, f, indent=2)   # Convert the transactions list into JSON format and write it to the file

    except Exception as e:
        print("Error saving file:", e)

# Function to load transactions (incomes and expenses) from a file
def load_transactions(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Error reading file:", e)
        return []         # Return an empty list to avoid breaking the program


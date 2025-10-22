def generate_report(transactions):
    print("\n----- Monthly Report -----")
    # Calculate the total income by summing all transaction amounts where the "type" key is "Income".
    total_income = sum(t["amount"] for t in transactions if t.get("type") == "Income")

    # Calculate the total expense by summing all transaction amounts where the "type" key is "Expense"
    total_expense = sum(t["amount"] for t in transactions if t.get("type") == "Expense")

    # Display overall summary: total income, total expense, and net savings.
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expense: ${total_expense:.2f}")
    print(f"Net Savings: ${total_income - total_expense:.2f}")

    # Simple breakdown by category
    by_cat = {}
    for t in transactions:
        c = t.get("category", "Uncategorized")     # Default to 'Uncategorized' if no category found
        by_cat.setdefault(c, 0.0)                  # Initialize category total if not already present
        by_cat[c] += t.get("amount", 0.0)          # Add the transaction amount to that category
    print("\nSpending by category:")     # Print spending grouped by category.
    for c, amt in by_cat.items():
        print(f" {c}: ${amt:.2f}")

def search_transactions(transactions, keyword):
    keyword = keyword.lower()
    results = []
    for t in transactions:
        if keyword in t.get("category", "").lower() or keyword in t.get("description", "").lower():
            results.append(t)
    if not results:
        print("No matching transactions found.")
        return
    print(f"\nFound {len(results)} transaction(s):")
    for t in results:
        print(t)

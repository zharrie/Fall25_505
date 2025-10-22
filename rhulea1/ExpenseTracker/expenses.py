# Base class that represents a financial transaction (either income or expense)
class Transaction:
    def __init__(self, amount, date, category, description):
        self.amount = amount
        self.date = date
        self.category = category
        self.description = description

# Convert the transaction object into a dictionary
    def to_dict(self):
        return {
            "amount": self.amount,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "type": self.__class__.__name__
        }
# Child class for income transactions
class Income(Transaction):
    pass
# Child class for expense transactions
class Expense(Transaction):
    pass

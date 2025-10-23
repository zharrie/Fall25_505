# This category class is used to group expenses under specific labels 
class Category:
    def __init__(self, name, budget_limit=0):  # Default is 0, meaning no limit if not specified

        self.name = name
        self.budget_limit = budget_limit       # Keeps track of how much has been spent in this category
        self.total_spent = 0

    # Method to add a new expense to this category
    def add_expense(self, amount):

        # Increases the total spent amount by the given expense
        self.total_spent += amount

    #To check if the spending is within the budget
    def check_budget(self):

        # If there is a set budget and total spending goes over it
        if self.budget_limit > 0 and self.total_spent > self.budget_limit:
            print(f"You have exceeded your budget for {self.name}!")

        # Otherwise, calculate how much money is left in the budget
        else:
            remaining = self.budget_limit - self.total_spent
            print(f"Remaining budget for {self.name}: {remaining:.2f}")

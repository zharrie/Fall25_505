class VendingMachine:
    def __init__(self):
        self.inventory = 20  # initial inventory

    def purchase(self, amount):
        self.inventory -= amount

    def restock(self, amount):
        self.inventory += amount

    def get_inventory(self):
        return self.inventory


# Read inputs
first_purchase = int(input())
restock_amount = int(input())
second_purchase = int(input())

# Create a VendingMachine object and perform operations
machine = VendingMachine()
machine.purchase(first_purchase)
machine.restock(restock_amount)
machine.purchase(second_purchase)

# Print the final inventory
print(f"Inventory: {machine.get_inventory()} bottles")

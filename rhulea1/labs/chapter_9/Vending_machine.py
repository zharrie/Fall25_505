class VendingMachine:

    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f"Inventory: {self.bottles} bottles")


if __name__ == "__main__":
    #Read the 3 input
    first_purchase = int(input())
    restock_amount = int(input())
    second_purchase = int(input())

    #Create vendingmachine object
    machine = VendingMachine()

    #Purchase first input number of bottles of drinks
    machine.purchase(first_purchase)

    #Restock second input number of bottles of drinks
    machine.restock(restock_amount)

    #Purchase last input number of bottles of drinks
    machine.purchase(second_purchase)

    #Report inventory
    machine.report()
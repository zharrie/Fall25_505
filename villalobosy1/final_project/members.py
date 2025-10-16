
# records what members borrow and return

class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrow_history = []

    # if member borrowed item
    def borrow_item(self, item):
        self.borrow_history.append((item.title, "Borrowed"))
        print(f"{self.name} borrowed '{item.title}'.")
    
    # if member returned item
    def return_item(self, item):
        self.borrow_history.append((item.title, "Returned"))
        print(f"{self.name} returned '{item.title}'.")
    
    # displays member info
    def show_info(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")

    # displays member's borrrowing history
    def show_history(self):
        print(f"\nBorrowing History for {self.name}")
        if not self.borrow_history:
            print("No borrowing history")
        else:
            for record in self.borrow_history:
                print(f"  - {record[0]} ({record[1]})")
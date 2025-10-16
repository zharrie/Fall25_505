 # check-in and check-out operations

class LibraryManager:
    def __init__(self):
        self.items = []     # stores items
        self.members = []   # stores members

    # adding item to library 
    def add_item(self, item):
        self.items.append(item)
        print(f"Added item: {item.title}")

    # adding member to library system
    def add_member(self, member):
        self.members.append(member)
        print(f"Added member: {member.name} (ID: {member.member_id})")   
     
    # finding item in library
    def find_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        raise ValueError(f"Item with ID {item_id} not found.")
    
    
    # finding member in library system
    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member   
        raise ValueError(f"Member with ID {member_id} not found")     
        
    
    # finding item to check-out
    def check_out_item(self, item_id, member_id):
        try:
            item = self.find_item(item_id)
            member = self.find_member(member_id)
            item.check_out(member_id)
            print(f"{member.name} successfully borrowed '{item.title}'.")
        except ValueError as e:
            print("Error:",e)
    
    # finding item to check-in
    def check_in_item(self, item_id):
        try:
            item = self.find_item(item_id)
            item.check_in()
            print(f"'{item.title}' successfully returned")
        except ValueError as e:
            print("Error:", e)
    
    # days
    def pass_days_all(self, days):
        for item in self.items:
            item.pass_days(days)

    # displaying library catalog and item availability
    def display_catalog(self):
        print("\nLibrary:")
        if not self.items:
            print("No items in the library")
        for item in self.items:
            item.show_info()
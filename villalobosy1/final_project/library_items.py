# base LibraryItem class

class LibraryItem:
    def __init__(self, item_id, title, year):
        self.item_id = item_id
        self.title = title
        self.year = year
        self.author = ""
        self.is_borrowed = False
        self.borrower_id = None
        self.days_borrowed = 0    # days since checkout
        self.due_days = 30     # items due after 30 days

    def check_out(self, member_id):
        if self.is_borrowed:
            raise ValueError(f"Item {self.title} is already borrowed")
        else:
            self.is_borrowed = True
            self.borrower_id = member_id
            self.days_borrowed = 0 
            print(f"{self.title} has been checked out by member {member_id}. Due in {self.due_days} days.")

    def check_in(self):
        if not self.is_borrowed:
            raise ValueError(f"Item '{self.title}' was not borrowed.")
        else:
            self.is_borrowed = False
            self.borrower_id = None
            self.days_borrowed = 0
            print(f"{self.title} has been returned.")

    def pass_days(self, days):
        if self.is_borrowed:
            self.days_borrowed += days
        # testing overdue days manually 

    # check if item is overdue
    def is_overdue(self):
        if self.is_borrowed and self.days_borrowed > self.due_days:
            print(f"{self.title} is overdue by {self.days_borrowed - self.due_days} days!")
            return True
        return False
    
    # availability of item
    def show_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"ID: {self.item_id}, Title: {self.title}, Year: {self.year}, Status: {status}")
        if self.is_borrowed:
            print(f"  Borrowed by: {self.borrower_id}, Days Borrowed: {self.days_borrowed}")


# child classes inheriting from base class

class Book(LibraryItem):
    def __init__(self, item_id, title, author, year):
        LibraryItem.__init__(self, item_id, title, year)
        self.author = author
    def show_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[Book] ID: {self.item_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}")


class Magazine(LibraryItem):
    def __init__(self, item_id, title, issue, year):
        LibraryItem.__init__(self, item_id, title, year)
        self.issue = issue
        self.author = ""
    def show_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[Magazine] ID: {self.item_id}, Title: {self.title}, Issue: {self.issue}, Year: {self.year}, Status: {status}") 


class DVD(LibraryItem):
    def __init__(self, item_id, title, duration, year):
        LibraryItem.__init__(self, item_id, title, year)
        self.duration = duration
        self.author = ""
    def show_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[DVD] ID: {self.item_id}, Title: {self.title}, Duration: {self.duration} mins, Year: {self.year}, Status: {status}")
from library_items import Book, Magazine, DVD
from members import Member
from library_manager import LibraryManager
from search_utils import linear_search, binary_search

lib = LibraryManager()

# adding items to library
lib.add_item(Book(1, "The Castle", "Franz Kafka", 1926))
lib.add_item(DVD(2, "The Wind That Shakes the Barley", 127, 2006))
lib.add_item(Magazine(3, "Al Jaras", "June", 2009))

# adding members to library
lib.add_member(Member("M001", "Yousef"))
lib.add_member(Member("M002", "Roisin"))

lib.display_catalog()

# items to be checked out
lib.check_out_item(1, "M002")
lib.check_out_item(2, "M001")

# borrowing an item that is already borrowed
lib.check_out_item(1, "M001")

#overdue items
lib.pass_days_all(30)

# return items 
lib.check_in_item(1)
lib.check_in_item(3)

# linear search
print("\nSearch by keyword 'Franz Kafka':")
results = linear_search(lib.items, "Franz Kafka")
for r in results: 
    r.show_info()

# binary search
print("\nBinary search for item ID 3:")

def get_item_id(item):
    return item.item_id

sorted_items = sorted(lib.items, key=get_item_id)
item = binary_search(sorted_items, 3)
if item:
    item.show_info()
else: 
    print("Item with ID 3 not found.")

# display library catalog again
lib.display_catalog()                   
# searching by ID
def binary_search(items, target_id):
    low = 0
    high = len(items) - 1

    while low <= high:
        mid = (low + high) // 2
        item = items[mid]

        if item.item_id == target_id:
            return item 
        if item.item_id < target_id:
            low = mid + 1
        else:
            high = mid - 1

    return None
    
# searching by title or author        
def linear_search(items, keyword):
    results = []
    keyword = keyword.lower()

    for item in items:
        # checks for the title
        if keyword in item.title.lower() or keyword in item.author.lower():
            results.append(item)

    return results
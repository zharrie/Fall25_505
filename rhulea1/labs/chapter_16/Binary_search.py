#Declare global variables .
recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    global recursions, comparisons
    
    recursions += 1         # Increment only for valid search range

    # Base case: search range is invalid, target not found
    if lower > upper:
        return -1

    #Calculate midpoint of current search range
    mid = (lower + upper) // 2

    #Compare target with middle element
    comparisons += 1      
    if nums[mid] == target:     
        return mid

    #Base case: search range has only one element and it's not the target
    if lower == upper:
        return -1

    #Decide which half to search next based on comparison
    comparisons += 1 
    if nums[mid] < target:      
        return binary_search(nums, target, mid + 1, upper) #Target is larger, search the RIGHT half (from mid+1 to upper)
    else: 
        return binary_search(nums, target, lower, mid - 1) #Target is smaller, search the LEFT half (from lower to mid-1)

if __name__ == "__main__":
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]
    
    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f"index: {index}, recursions: {recursions}, comparisons: {comparisons}")

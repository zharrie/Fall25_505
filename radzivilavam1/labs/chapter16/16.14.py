recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    global recursions, comparisons
    recursions += 1

    mid = (lower + upper) // 2

    comparisons += 1
    if nums[mid] == target:
        return mid
    elif lower == upper:
        return -1

    comparisons += 1
    if nums[mid] > target:
        return binary_search(nums, target, lower, mid - 1)
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, upper)


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

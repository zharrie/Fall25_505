def in_order(nums):
    # Return True if the list is in descending (non-increasing) order
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            return False
    return True


if __name__ == "__main__":
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print("In descending order")
    else:
        print("Not in order")

    # Test in-order example
    nums2 = [10, 8, 7, 6, 5]
    if in_order(nums2):
        print("In descending order")
    else:
        print("Not in order")
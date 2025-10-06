def in_order(nums):
    # Type your code here.
    if nums == sorted(nums, reverse=True):
        return True
    else:
        return False


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

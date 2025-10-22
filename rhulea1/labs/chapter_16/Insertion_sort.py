def read_nums():
    """Read numbers from input and return them in a list"""
    return [int(num) for num in input().split()]


def print_nums(nums):
    """Output numbers, separating each item by a spaces;
    no space or newline before the first number or after the last."""
    print(" ".join([str(n) for n in nums]), end="")


def swap(nums, n, m):
    """Exchange nums[n] and nums[m]"""
    nums[n], nums[m] = nums[m], nums[n]


def insertion_sort(numbers):
    """Sort the list numbers using insertion sort"""
    comparisons = 0
    swaps = 0
    
    #Count comparisons and swaps. Output the array at the end of each iteration.
    for i in range(1, len(numbers)):
        j = i
        # Insert numbers[i] into sorted part
        # stopping once numbers[i] is in correct position
        while j > 0: 
            comparisons += 1  #count comparison
            if numbers[j] < numbers[j - 1]:
                swap(numbers, j, j - 1)
                swaps += 1   #count swap
                j -= 1
            else:
                break
        #Output the array at the end of each iteration
        print_nums(numbers)
        print() #New line created after each iteration
        
    return comparisons, swaps

if __name__ == "__main__":
    #Read numbers into a list
    numbers = read_nums()

    #Output the numbers list
    print_nums(numbers)
    print(end="\n\n")
    
    #Sort the numbers list and get comparison/swap counts
    comparisons, swaps = insertion_sort(numbers)
    print()
    
    #Output the number of comparisons and swaps performed
    print(f"comparisons: {comparisons}")
    print(f"swaps: {swaps}")

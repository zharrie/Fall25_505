#Read first line as list of integers
nums = list(map(int, input().split()))

#Read lower and upper bounds
lower, upper = map(int, input().split())

#Loop through the first list to print range
for n in nums:
    if lower <= n <= upper:
        print(f"{n},", end="")
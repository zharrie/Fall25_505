""" Type your code here. """
nums = [int(x) for x in input().split()]
low, high = map(int, input().split())

for n in nums:
    if low <= n <= high:
        print(f"{n},", end="")
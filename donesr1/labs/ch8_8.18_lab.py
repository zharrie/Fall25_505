line = input().split()
nums = []
for value in line:
    nums.append(int(value))

# Step 2: read the lower and upper bounds
bounds = input().split()
lower = int(bounds[0])
upper = int(bounds[1])

# Step 3: output numbers in the range
for n in nums:
    if lower <= n <= upper:
        print(f"{n},", end="")
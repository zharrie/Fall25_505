line = input().split()

nums = []
for value in line:
    nums.append(int(value))

negatives = []
for n in nums:
    if n < 0:
        negatives.append(n)


negatives.sort(reverse=True)

for n in negatives:
    print(n, end=" ")
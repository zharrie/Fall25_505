""" Type your code here. """
nums = [int(x) for x in input().split()]

negatives = []
for n in nums:
    if n < 0:
        negatives.append(n)

negatives.sort(reverse=True)

for n in negatives:
    print(n, end=' ')
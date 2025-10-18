#List read from input as integers
nums = list(map(int, input().split()))

#Filter only negatives
negatives = [n for n in nums if n < 0]

#sort them in descending order
negatives.sort(reverse=True)

#Print each followed by a space
for n in negatives:
    print(n, end=" ")
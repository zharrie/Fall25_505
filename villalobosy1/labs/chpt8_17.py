num_list = [int(x) for x in input().split()]

negatives = sorted([x for x in num_list if x < 0])
negatives.reverse()

for x in negatives:
    print(x, end=" ")
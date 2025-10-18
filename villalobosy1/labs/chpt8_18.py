num_list = [int(x) for x in input().split()]

low_b, up_b = [int(x) for x in input().split()]

y = [x for x in num_list if low_b <= x <= up_b]

for num in y:
    print(f"{num},", end="")
x = int(input())

num_list = []
for i in range(0, x):

    num_list.append(float(input()))
max_list = max(num_list)

for num in num_list:
    num = num/max_list
    print(f"{num:.2f}")
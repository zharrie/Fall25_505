values = int(input())

values_list = []

for i in range(values):
    values_list.append(float(input()))


highest = max(values_list)

for number in values_list:
    output = number / highest
    print(f"{output:.2f}")






#8.17 LAB: Filter and sort a list
nums = list(map(int, input().split()))
negatives = [x for x in nums if x < 0]
negative.sort(reserve = True)
for n in negatives:
    print(n, end='')
#8.18 LAB: Elements in a range
numbers = list(map(int, input().split()))
lower, upper = map(int, input().split())
in_range = [str(num) for num in numbers if lower <= num <= upper]
print(','.join(in_range) + ',', end='')

#8.20 LAB: Car wash
services = {
    "Air freshener": 1,
    "Rain repellent": 2,
    "Tire shine": 2,
    "Wax": 3,
    "Vacuum": 5,
}
base_wash = 10
total = base_wash

service_choice1 = input()
service_choice2 = input()

print("ZyCar Wash")
print("Base car wash - $10")

if service_choice1 != "-":
    print(f"{service_choice1} - ${services[service_choice1]}")
    total += services[service_choice1]

if service_choice2 != "-":
    print(f"{service_choice2} - ${services[service_choice2]}")
    total += services[service_choice2]

print()
print(f"Total price: ${total}")
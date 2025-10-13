x = input().split()
search_name = input()

contact_dict = {}

for info in x:
    name, number = info.split(",")
    contact_dict[name] = number

print(contact_dict[search_name])
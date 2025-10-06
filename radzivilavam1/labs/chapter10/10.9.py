names = [
    "Ryley",
    "Edan",
    "Reagan",
    "Henry",
    "Caius",
    "Jane",
    "Guto",
    "Sonya",
    "Tyrese",
    "Johnny",
]
index = int(input())

# Type your code here.
try:
    print(f"Name: {names[index]}")
except IndexError:
    print("Exception! list index out of range")
    if index < 0:
        index = 0
    elif index >= len(names):
        index = len(names) - 1
    print(f"The closest name is: {names[index]}")
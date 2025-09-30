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


try:
    index = int(input())
    print("Name:", names[index])
except IndexError as e:
    print("Exception!", str(e))
    if index < 0:
        print("The closest name is:", names[0])
    else:
        print("The closest name is:", names[-1])
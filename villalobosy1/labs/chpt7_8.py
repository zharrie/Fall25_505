input1 = []
while True:
    x = input()
    if "quit" in x:
        break
    else:
        input1.append(x)

for x in input1:
    word, num = x.split()
    print(f"Eating {num} {word} a day keeps you happy and healthy.")

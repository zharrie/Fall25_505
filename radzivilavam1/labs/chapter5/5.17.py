text = input()

while text not in ["Done", "done", "d"]:
    for character in reversed(text):
        print(f"{character}", end="")
    print()
    text = input()


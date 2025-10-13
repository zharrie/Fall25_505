""" Type your code here. """
while True:
    user_input = input()
    if "quit" in user_input:
        break
    word, number = user_input.split()

    print(f"Eating {number} {word} a day keeps you happy and healthy.")
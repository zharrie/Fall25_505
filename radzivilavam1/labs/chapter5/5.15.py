word = input()
password = ""
char_list = []

for character in word:
    char_list.append(character)

for letter in char_list:
    if letter == "i":
        index = char_list.index(letter)
        char_list[index] = "1"
    elif letter == "a":
        index = char_list.index(letter)
        char_list[index] = "@"
    elif letter == "m":
        index = char_list.index(letter)
        char_list[index] = "M"
    elif letter == "B":
        index = char_list.index(letter)
        char_list[index] = "8"
    elif letter == "s":
        index = char_list.index(letter)
        char_list[index] = "$"


for j in char_list:
    password += j

print(f"{password}!")



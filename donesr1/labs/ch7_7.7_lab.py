user_input = input()

char, phrase = user_input[0], user_input[2:]
count = phrase.count(char)

if count == 1:
    print(f"{count} {char}")
else:
    print(f"{count} {char}'s")
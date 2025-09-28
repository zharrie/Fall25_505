#Read from input, first character and then phrase
inp = input().split(maxsplit=1)
char = inp[0]
phrase = inp[1]

#Count occurrence of the character
count = phrase.count(char)
if count == 1:
    print(f"{count} {char}")
else:
    print(f"{count} {char}'s")
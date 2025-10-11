""" Type your code here. """
char, phrase = input().split(sep=" ", maxsplit=1)

char_count = phrase.count(char)

if char_count == 1:
    print(f"{char_count} {char}")
else:
    print(f"{char_count} {char}'s")
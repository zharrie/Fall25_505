my_str = input()

char = my_str[0]
phrase = my_str[1:]

count_chr = phrase.count(char)

if count_chr > 1 or count_chr == 0:
    print(f"{count_chr} {char}'s")
elif count_chr == 1:
    print(f"{count_chr} {char}")
word = input()

word = word.replace("i", "1")
word = word.replace("a", "@")
word = word.replace("m", "M")
word = word.replace("B", "8")
word = word.replace("s", "$")
password = word + "!"

print(password)
text = input()

result = ""
for char in text:
    if char.isalpha():
        result += char

print(result)
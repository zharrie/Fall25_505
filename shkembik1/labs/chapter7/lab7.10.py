""" Type your code here. """
text = input()

result = ""
for ch in text:
    if ch.isalpha():
        result += ch

print(result)
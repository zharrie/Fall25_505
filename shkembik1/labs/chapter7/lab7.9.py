text = input()

# Ignore spaces when checking
cleaned = text.replace(" ", "")

if cleaned == cleaned[::-1]:
    print(f"palindrome: {text}")
else:
    print(f"not a palindrome: {text}")
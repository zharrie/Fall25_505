#Read input
text = input()

#Remove spaces
text_no_space = text.replace(" ", "")

if text_no_space == text_no_space[::-1]:
    print(f"palindrome: {text}")
else:
    print(f"not a palindrome: {text}")

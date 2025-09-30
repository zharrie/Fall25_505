phrase = input()
cleaned = phrase.replace("","").lower()
if cleaned == cleaned[::-1]:
    print(f"palindrome: {phrase}")
else:
    print(f"not a palindrome: {phrase}")
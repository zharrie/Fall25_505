input_str = input()
input_str_clean = input_str.strip().replace(" ", "")

if input_str_clean == input_str_clean[::-1]:
    print(f"palindrome: {input_str}")
else:
    print(f"not a palindrome: {input_str}")
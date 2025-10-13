#Read input
text = input()

#Keep only alpabetic characters
clean_text = "".join(char for char in text if char.isalpha())
print(clean_text)
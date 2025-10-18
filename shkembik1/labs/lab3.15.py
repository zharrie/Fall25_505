phone_number = int(input())

number = f"{phone_number:010d}"  
area=number[:3]
prefix= number[3:6]
line_number= number[6:]

print(f"({area}) {prefix}-{line_number}")
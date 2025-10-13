phone_number = int(input())
area_code = phone_number // 10_000_000
prefix = (phone_number // 10000) % 1_000
line_number = phone_number % 10_000
formatted_number = f"({area_code}) {prefix:03d}-{line_number:04d}"
print(formatted_number)
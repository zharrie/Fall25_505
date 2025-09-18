phone_number = int(input())

area_code = phone_number // 10000000
prefix = (phone_number // 10000) % 1000
line = phone_number % 10000

print(f"({area_code}) {prefix}-{line}")

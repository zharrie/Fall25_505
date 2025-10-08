# Type your code here.
try:
    user_num = int(input())
    div_num = int(input())
    integer_quotient = user_num // div_num
    print(integer_quotient)
except ZeroDivisionError as e1:
    print(f"Zero Division Exception: {e1}")
except ValueError as e2:
    print(f"Input Exception: {e2}")
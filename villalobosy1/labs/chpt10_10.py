try:
    user_num = int(input())
    div_num = int(input())
    result = user_num // div_num
    print(result)
except ZeroDivisionError as excpt:
    print(f"Zero Division Exception: {excpt}")
except ValueError as excpt:
    print(f"Input Exception: {excpt}")

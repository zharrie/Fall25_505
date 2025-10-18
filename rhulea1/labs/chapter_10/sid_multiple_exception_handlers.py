try:
    user_num = int(input())
    div_num = int(input())
#Perform integer division
    result = user_num // div_num
    print(result)

except ZeroDivisionError as e:
    print(f"Zero Division Exception: {e}")
except ValueError as e:
    print(f"Input Exception: {e}")
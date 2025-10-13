try:
    user_num = int(input())
    div_num = int(input())
    print(user_num // div_num)
except ZeroDivisionError as e:
    print("Zero Division Exception:", e)
except ValueError as e:
    print("Input Exception:", e)

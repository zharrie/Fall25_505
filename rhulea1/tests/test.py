# # letter1 = "a"
# # letter2 = "?"
# # while letter1 <= "z":  # Outer loop
# #     letter2 = "a"
# #     while letter2 <= "z":  # Inner loop
# #         print(f"{letter1}{letter2}.com")
# #         letter2 = chr(ord(letter2) + 1)
# #     letter1 = chr(ord(letter1) + 1)

# # count = 0
# # for i in range(4):
# #    for j in range(3):
# #       count = count + 1
# # print(count)


# # user_input = input("Enter phone number: ")

# # index = 0
# # for character in user_input:
# #     print(f"Element {index} is: {character}")
# #     index += 1

#     # Third version
# user_input = input("Enter phone number: ")
# phone_number = ""

# for character in user_input:
#     if ("0" <= character <= "9") or (character == "-"):
#         phone_number += character
#     elif ("a" <= character <= "c") or ("A" <= character <= "C"):
#         phone_number += "2"
#     #FIXME: Add remaining elif branches
#     elif ("d" <= character <= "f") or ("D" <= character <= "F"):
#         phone_number += "3"
#     elif ("g" <= character <= "i") or ("G" <= character <= "I"):
#         phone_number += "4"
#     elif ("j" <= character <= "l") or ("J" <= character <= "L"):
#         phone_number += "5"
#     elif ("m" <= character <= "o") or ("M" <= character <= "O"):
#         phone_number += "6"
#     elif ("p" <= character <= "s") or ("P" <= character <= "S"):
#         phone_number += "7"
#     elif ("t" <= character <= "v") or ("T" <= character <= "V"):
#         phone_number += "8"
#     elif ("w" <= character <= "z") or ("W" <= character <= "Z"):
#         phone_number += "9"
    
#     else:
#         phone_number += "?"


# print(f"Numbers only: {phone_number}")


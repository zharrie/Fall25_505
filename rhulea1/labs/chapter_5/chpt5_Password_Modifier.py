word = input()
password = word

password = password.replace("i", "1")
password = password.replace("a", "@")
password = password.replace("m", "M")
password = password.replace("B", "8")
password = password.replace("s", "$")

#Appending "!" to the end
password = password + "!"
print(password)
while True:
    text = input()
    if text == "Done" or text == "done" or text == "d":
        break
    
    #Printing the reverse
    print(text[::-1])
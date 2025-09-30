values = []
while True:
    if i in values == -1: # type: ignore # break if -1
        break

def get_max_int(nums): # max value
    if values:
        max_val = values[0]
    for val in values:
        if val > max_val:
            max_val = val

    for val in values: # max value - values
        adjusted = max_val - val 
        print(int(round(adjusted)))
    else:
        print(adjusted)
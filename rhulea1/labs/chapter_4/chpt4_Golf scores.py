no_of_strokes = int(input())
par = int(input())

#Set default result to "Error" in case nothing matches
result = "Error"

if par in [3, 4, 5]:
#Compare strokes to par to find score name
    if no_of_strokes == par - 2:
        result = "Eagle"
    elif no_of_strokes == par - 1:
        result = "Birdie"
    elif no_of_strokes == par:
        result = "Par"
    elif no_of_strokes == par + 1:
        result = "Bogey"
#Print the result
if result != "Error":
    print(f"Par {par} in {no_of_strokes} strokes is {result}")
else:
    print(f"Par {par} in {no_of_strokes} strokes is Error")
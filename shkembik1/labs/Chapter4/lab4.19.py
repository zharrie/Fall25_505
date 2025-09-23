strokes = int(input())  # strokes first
par = int(input())      # then par

name = "Error"
if par == 3 or par == 4 or par == 5:
    if strokes == par - 2:
        name = "Eagle"
    elif strokes == par - 1:
        name = "Birdie"
    elif strokes == par:
        name = "Par"
    elif strokes == par + 1:
        name = "Bogey"

print(f"Par {par} in {strokes} strokes is {name}")
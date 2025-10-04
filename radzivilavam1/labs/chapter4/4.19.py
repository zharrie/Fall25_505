number_of_strokes = int(input())
par = int(input())

if (number_of_strokes + 2 == par) and (par == 3 or par == 4 or par == 5):
    print(f"Par {par} in {number_of_strokes} strokes is Eagle")
elif (number_of_strokes + 1 == par) and (par == 3 or par == 4 or par == 5):
    print(f"Par {par} in {number_of_strokes} strokes is Birdie")
elif (number_of_strokes == par) and (par == 3 or par == 4 or par == 5):
    print(f"Par {par} in {number_of_strokes} strokes is Par")
elif (number_of_strokes - 1 == par) and (par == 3 or par == 4 or par == 5):
    print(f"Par {par} in {number_of_strokes} strokes is Bogey")
else:
    print(f"Par {par} in {number_of_strokes} strokes is Error")

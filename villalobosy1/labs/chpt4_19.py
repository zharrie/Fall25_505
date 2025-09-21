num_strokes = int(input())
par = int(input())

if (par == 3 or par == 4 or par == 5) and num_strokes == par - 2:
    print(f"Par {par} in {num_strokes} strokes is Eagle")

elif (par == 3 or par == 4 or par == 5) and num_strokes == par - 1:
    print(f"Par {par} in {num_strokes} strokes is Birdie")

elif (par == 3 or par == 4 or par == 5) and num_strokes == par:
    print(f"Par {par} in {num_strokes} strokes is Par")

elif (par == 3 or par == 4 or par == 5) and num_strokes == par + 1:
    print(f"Par {par} in {num_strokes} strokes is Bogey")

else:
    print(f"Par {par} in {num_strokes} strokes is Error")
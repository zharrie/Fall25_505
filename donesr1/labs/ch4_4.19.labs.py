strokes = int(input())
par = int(input())

if par not in (3, 4, 5):
    print(f"Par {par} in {strokes} strokes is Error")
else:
    if strokes == par - 2:
        print(f"Par {par} in {strokes} strokes is Eagle")
    elif strokes == par - 1:
        print(f"Par {par} in {strokes} strokes is Birdie")
    elif strokes == par:
        print(f"Par {par} in {strokes} strokes is Par")
    elif strokes == par + 1:
        print(f"Par {par} in {strokes} strokes is Bogey")
    else:
        print(f"Par {par} in {strokes} strokes is Error")
name = input().split()  # e.g., "Julia Clark" or "Julia Ann Clark"

# Require at least first and last
if len(name) < 2:
    print("Invalid input")
else:
    first = name[0]
    last = name[-1]
    # Middle initials (empty if no middles)
    middle_initials = ''.join(m[0] + '.' for m in name[1:-1])
    print(f"{last}, {first[0]}.{middle_initials}")
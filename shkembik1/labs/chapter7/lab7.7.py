""" Type your code here. """
line = input()

space_idx = line.find(' ')      # index of first space
ch = line[:space_idx]           # the character
phrase = line[space_idx + 1:]   # the phrase

# Manual count (no .count)
cnt = 0
for c in phrase:
    if c == ch:
        cnt += 1

# Pluralize unless exactly 1
label = ch if cnt == 1 else f"{ch}'s"
print(cnt, label)
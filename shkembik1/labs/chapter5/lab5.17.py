line = input()

while line not in ("Done", "done", "d"):
    reversed_line = ""
    i = len(line) - 1
    while i >= 0:
        reversed_line += line[i]
        i -= 1

    print(reversed_line)
    line = input()
def print_all_permutations(permList, nameList):
    if len(nameList) == 0:
        print(", ".join(permList))
    else:
        for i in range(len(nameList)):

            #Choose the current name
            newPermList = permList + [nameList[i]]

            # Remaining names excluding the chosen one
            newNameList = nameList[:i] + nameList[i+1:]
            print_all_permutations(newPermList, newNameList)


if __name__ == "__main__":
    nameList = input().split(" ")
    permList = []
    print_all_permutations(permList, nameList)

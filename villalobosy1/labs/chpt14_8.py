def print_all_permutations(perm_names, new_names):
    if len(new_names) == 0:
        print(', '.join(perm_names) + '')
    else:
        for i in range(len(new_names)):
            name_new= new_names[:i] + new_names[i + 1:]
            new_perm_names = perm_names + [new_names[i]]
            print_all_permutations(new_perm_names, name_new)

if __name__ == "__main__":
    nameList = input().split(" ")
    permList = []
    print_all_permutations(permList, nameList)

animals_set1 = {"cheetah"}
animals_set2 = set()
animals_set2.add(input())
animals_set2.add(input())
animals_set2.add(input())
#Update animals_set1 with animals_set2
animals_set1.update(animals_set2)
print(sorted(animals_set1))

animals_set1.add(input())
animals_set1.pop()
print(sorted(animals_set1))
# animals_set1.add(input())

# print(f"animals_set1: {sorted(animals_set1)}")
# print(f"animals_set2: {sorted(animals_set2)}")
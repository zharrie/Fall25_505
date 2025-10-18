# 3.16 LAB simple statistics 
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4 
average = (num1 + num2 + num3 + num4) / 4 

print(f"{product:.0f} {average:.0f}")
print(f"{product:.3f} {average:.3f}")

# 3.15 LAB: Phone number breakdown

phone_number = int(input())

area = phone_number // 10000000
prefix = (phone_number // 10000) % 1000
line = phone_number % 10000

print(f"({area}) {prefix}-{line:04d}")

# 3.14 LAB: Input and formatted output: Right-facing arrow

base_char = input()
head_char = input()

row1 = '  ' + head_char
row2 = base_char * 5 + head_char
row3 = base_char * 7 + head_char
row4 = base_char * 5 + head_char
row5 = ' ' + head_char 

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

#3.13 LAB: Set basics

my_fruit1 = input()
my_fruit2 = input()
my_fruit3 = input()

your_fruit1 = input()
your_fruit2 = input()

their_fruit = input()

# 1. TODO: Define a set, fruits, containing my_fruit1, my_fruit2, and my_fruit3
fruits = (my_fruit1, my_fruit2, my_fruit3)
print(sorted(fruits))

# 2. TODO: Add your_fruit1 and your_fruit2 to fruits
fruits.add(your_fruit1)
fruits.add(your_fruit2)
print(sorted(fruits))

# 3. TODO: Add their_fruit to fruits
fruits.add(their_fruit)
print(sorted(fruits))

# 4. TODO: Add your_fruit1 to fruits
fruits.add(your_fruits1)
print(sorted(fruits))

# 5. TODO: Remove my_fruit1 from fruits
fruits.remove(my_fruit1)
print(sorted(fruits))

# 3.12 LAB: List basics

my_flower1 = input()
my_flower2 = input('peony')
my_flower3 = input('lily')

your_flower1 = input('tulips')
your_flower2 = input('aster')

their_flower = input('daisy')

# 1. TODO: Define my_list containing my_flower1, my_flower2, and my_flower3
# in that order
my_list = [my_flower1, my_flower2, my_flower3]

# 2. TODO: Define your_list containing your_flower1 and your_flower2
# in that order
your_list = [your_flower1, your_flower2]

# 3. TODO: Define our_list by concatenating my_list and your_list

our_list = [my_list + your_list]
print(our_list)

# 4. TODO: Append their_flower to the end of our_list
our_list.append(their_flower)
print(our_list)

# 5. TODO: Replace my_flower2 in our_list with their_flower
our_list[our_list.index(my_flower2)] = their_flower
print(our_list)

# 6. TODO: Remove the first occurrence of their_flower from
# our_list without using index()

our_list.remove(their_flower)
print(our_list)

# 7. TODO: Remove the second element of our_list
our_list.pop(1)
print(our_list)


# my_list = input(my_flower1, my_flower2, my_flower3)
# your_list = input( your_flower1, your_flower2)
# our_list = input( my_list and your_list)
# print(our_list)
# my_list.append()

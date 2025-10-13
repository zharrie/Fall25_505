# Given a base Plant class and a derived Flower class, write a program to create a list called my_garden.
# Store objects that belong to the Plant class or the Flower class in the list.
# Create a function called print_list(), that uses the print_info() instance methods defined in the respective classes and prints each element in my_garden.
# The program should read plants or flowers from input (ending with -1), add each Plant
# or Flower to the my_garden list, and output each element in my_garden using the print_info() function.
#
# Note: A list can contain different data types and also different objects.

class Plant:

    def __init__(self, plant_name, plant_cost):
        self.plant_name = plant_name
        self.plant_cost = plant_cost

    def print_info(self):
        print(f"   Plant name: { self.plant_name }")
        print(f"   Cost: { self.plant_cost }")


class Flower(Plant):

    def __init__(self, plant_name, plant_cost, is_annual, color_of_flowers):
        Plant.__init__(self, plant_name, plant_cost)
        self.is_annual = is_annual
        self.color_of_flowers = color_of_flowers

    def print_info(self):
        print(f"   Plant name: { self.plant_name }")
        print(f"   Cost: { self.plant_cost }")
        print(f"   Annual: { self.is_annual }")
        print(f"   Color of flowers: { self.color_of_flowers }")

def print_list(my_garden):
    for idx, instance in enumerate(my_garden):
        print(f"Plant {idx+1} Information:")
        instance.print_info()
        print()



# TODO:  Define the print_list() function that prints a list of plant (or flower) objects

if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input()

    while user_string != "-1":
        user_string_list = user_string.split()
        if user_string_list[0] == "plant":
            my_garden.append(Plant(user_string_list[1], user_string_list[2]))
        elif user_string_list[0] == "flower":
            my_garden.append(Flower(user_string_list[1], user_string_list[2], user_string_list[3], user_string_list[4]))
        # TODO: Check if input is a plant or flower
        #       Split the user_string input into variables - plant_name, plant_cost, is_annual, color_of_flowers
        #       Store as a plant object or flower object
        #       Add to the list my_garden
        user_string = input()

    # TODO: Call the print_list() function to print my_garden
    print_list(my_garden)

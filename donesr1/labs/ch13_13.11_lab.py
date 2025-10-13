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


# TODO:  Define the print_list() function that prints a list of plant (or flower) objects
    def plant_list(my_garden):
        for plant in garden:
            plant.print_info()


if __name__ == "__main__":

    # TODO: Declare a list called my_garden that can hold object of type plant
    my_garden = []

    user_string = input()

    while user_string != "-1":
        if tokens[0] == "plant" and len(tokens) == 3:
            _, plant_name, plant_cost = tokens
            plant = Plant(plant_name, plant_cost)
            my_garden.append(plant)
        user_string = input()

    print_list(my_garden)
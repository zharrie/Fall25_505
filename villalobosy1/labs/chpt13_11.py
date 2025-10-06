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


def print_list(garden_list):
    for i, plant in enumerate(garden_list, 1):
        print(f"Plant {i} Information:")
        plant.print_info()
        print()

if __name__ == "__main__":

    my_garden = []

    user_string = input()

    while user_string != "-1":
        x = user_string.split()
        plant_type = x[0]

        if plant_type == "plant":
            name = x[1]
            cost = x[2]
            plant = Plant(name, cost)
            my_garden.append(plant)

        elif plant_type == "flower":
            name = x[1]
            cost = x[2]
            is_annual = x[3]
            color = x[4]
            flower = Flower(name, cost, is_annual, color)
            my_garden.append(flower)
        
        user_string = input()

    print_list(my_garden)

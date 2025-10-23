class Plant:
    def __init__(self, name, cost):
        self.name = name
        self.cost = int(cost)

    def print_info(self, index):
        print(f"Plant {index} Information:")
        print(f"   Plant name: {self.name}")
        print(f"   Cost: {self.cost}")


class Flower(Plant):
    def __init__(self, name, cost, is_annual, color):
        super().__init__(name, cost)
        self.is_annual = is_annual
        self.color = color

    def print_info(self, index):
        print(f"Plant {index} Information:")
        print(f"   Plant name: {self.name}")
        print(f"   Cost: {self.cost}")
        print(f"   Annual: {self.is_annual}")
        print(f"   Color of flowers: {self.color}")


def print_list(plants):
    for i, plant in enumerate(plants, start=1):
        plant.print_info(i)
        print()  # Print a newline between plant entries


def main():
    my_garden = []

    while True:
        line = input()
        if line == "-1":
            break

        parts = line.split()
        if not parts:
            continue

        if parts[0] == "plant":
            _, name, cost = parts
            my_garden.append(Plant(name, cost))
        elif parts[0] == "flower":
            _, name, cost, is_annual, color = parts
            my_garden.append(Flower(name, cost, is_annual, color))

    print_list(my_garden)


# Run the program
if __name__ == "__main__":
    main()

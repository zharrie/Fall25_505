class Triangle:

    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print(f"Base: {self.base:.2f}")
        print(f"Height: {self.height:.2f}")
        print(f"Area: {self.get_area():.2f}")


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    
    base1 = float(input())
    height1 = float(input())
    triangle1.set_base(base1)
    triangle1.set_height(height1)
  
    base2 = float(input())
    height2 = float(input())
    triangle2.set_base(base2)
    triangle2.set_height(height2)

    print("Triangle with smaller area:")

    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()
   
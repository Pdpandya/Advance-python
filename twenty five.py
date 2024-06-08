class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def area(self):
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.pi * self.radius

circle1 = Circle(5)
print("Area of the circle with radius 5:",circle1.area())
print("Perimeter of the circle with radius 5:",circle1.perimeter())


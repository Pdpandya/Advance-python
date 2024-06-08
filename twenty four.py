class Circle:
    PI = 3.14 

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius

# Example usage:
circle1 = Circle(5)
print(" circle with radius 5: ",circle1.area())
print(" circle with radius 5: ",circle1.perimeter())



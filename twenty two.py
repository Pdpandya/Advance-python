"""In Python, you define a class using the class keyword. A class serves as a blueprint for creating objects instances of the class. It can contain attributes  and methods that define the behavior of the objects."""

'''self in Python
self: self is a conventional name for the first parameter of methods in a class. It refers to the instance of the class. Using self, you can access attributes and methods of the class in Python.'''



#Example of a Python Class

class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Method to display person details
    def details(self):
        print("Name:" (self.name), "Age:" (self.age))

person1 = Person("parth", 30)
# Calling a method 
person1.details()

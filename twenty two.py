"""Python's class keyword is used to define a class. An object's instances are created using a class as a blueprint. It may include properties and functions that specify how the objects behave."""

'''self in Python
 The first argument of a class's methods is commonly referred to as self. It alludes to the class instance. In Python, you can access the class's methods and properties by using self.'''


class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def details(self):
        print("Name:" (self.name), "Age:" (self.age))

person1 = Person("parth", 30)
person1.details()

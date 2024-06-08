'''Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit attributes and methods from another class. The class that inherits is called the subclass or derived class, and the class from which it inherits is called the superclass or base class.'''

#example
# Base class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name," makes a sound."

# Derived class
class Dog(Animal):
    def speak(self):
        return self.name," barks."

# Derived class
class Cat(Animal):
    def speak(self):
        return self.name, "meows."

dog = Dog("Buddy")
cat = Cat("Whisker")

# Calling methods
print(dog.speak())  
print(cat.speak()) 


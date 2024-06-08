'''Object-oriented programming (OOP) is based on the fundamental idea of inheritance, which lets a class inherit properties and functions from another class. The class from which it inherits is referred to as the superclass or base class, and the class that inherits is referred to as the subclass or derived class.'''
  
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


'''To determine if an object is an instance of a specific class or a subclass thereof, use the isinstance() function. Verifying an object's type during runtime is possible with the help of the isinstance() function.'''

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))      
print(isinstance(dog, Animal))   
print(isinstance(dog, str))      

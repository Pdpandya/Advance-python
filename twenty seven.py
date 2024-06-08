'''the isinstance() function is used to check whether an object is an instance of a particular class or a subclass thereof. The isinstance() function provides a way to verify the type of an object at runtime.'''

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(isinstance(dog, Dog))      
print(isinstance(dog, Animal))   
print(isinstance(dog, str))      

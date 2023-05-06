class Animal:
    pass

class Dog(Animal):
    pass

class Owczarek(Dog):
    pass

class Cat(Animal):
    pass

# print(issubclass(Cat, Animal))
# print(issubclass(Dog, Animal))
# print(issubclass(Animal, Animal))
#
# print(issubclass(Owczarek, Dog))
# print(issubclass(Owczarek, Animal))
# print(issubclass(Owczarek, object))

dog = Dog()
dog_1 = Dog()
dog_2 = dog

# print(isinstance(dog, Animal))
# print(isinstance(dog, Dog))
# print(isinstance(dog, Cat))

print(dog is dog)
print(dog is dog_1)
print(dog is dog_2)


from enum import Enum

class AnimalType(Enum):
    DOG = "dog"
    CAT = "cat"

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print(f"{self.name} is barking!")

class Cat:
    def __init__(self, name):
        self.name = name
    
    def meow(self):
        print(f"{self.name} is meowing!")

class AnimalFactory:
    def __init__(self):
        self._animal_types = {
            AnimalType.DOG: Dog,
            AnimalType.CAT: Cat,
        }
    
    def create_animal(self, animal_type, name):
        animal_class = self._animal_types.get(animal_type)
        if not animal_class:
            raise ValueError(f"Invalid animal type: {animal_type}")
        return animal_class(name)

factory = AnimalFactory()
dog = factory.create_animal(AnimalType.DOG, "Fido")
cat = factory.create_animal(AnimalType.CAT, "Whiskers")

dog.bark()  # Output: Fido is barking!
cat.meow()  # Output: Whiskers is meowing!

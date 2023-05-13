from enum import Enum

# Define an enumeration of animal types
class AnimalType(Enum):
    DOG = "dog"
    CAT = "cat"

# Define a base class for all animals
class Animal:
    def __init__(self, name):
        self.name = name

    # Define a speak method that will be overridden by subclasses
    def speak(self):
        pass

# Define a subclass of Animal for dogs
class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking!")

# Define a subclass of Animal for cats
class Cat(Animal):
    def speak(self):
        print(f"{self.name} is meowing!")

# Define a factory class for creating animals
class AnimalFactory:
    """Aim of the factory method is to keep class Animal sub class creation in one place"""
    def __init__(self):
        # Define a dictionary that maps AnimalType values to their corresponding classes
        self._animal_types = {
            AnimalType.DOG: Dog,
            AnimalType.CAT: Cat,
        }

    def create_animal(self, animal_type, name):
        # Use the dictionary to create an instance of the appropriate class
        animal_class = self._animal_types.get(animal_type)
        if animal_class:
            return animal_class(name)
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")

# Create an instance of the AnimalFactory
factory = AnimalFactory()

# Use the factory to create a dog and a cat
dog = factory.create_animal(AnimalType.DOG, "Fido")
cat = factory.create_animal(AnimalType.CAT, "Fluffy")

# Call the speak method of each animal to confirm that it is working
dog.speak()  # prints "Fido is barking!"
cat.speak()  # prints "Fluffy is meowing!"

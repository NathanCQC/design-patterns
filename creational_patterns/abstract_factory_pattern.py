# Abstract Factory Interface
class GameFactory:
    def create_weapon(self):
        pass
    
    def create_character(self):
        pass
    
    def create_environment(self):
        pass


# Concrete Factory 1 - Fantasy Game Factory
class FantasyGameFactory(GameFactory):
    def create_weapon(self):
        return Sword()
    
    def create_character(self):
        return Knight()
    
    def create_environment(self):
        return Castle()
    
    
# Concrete Factory 2 - Sci-Fi Game Factory
class SciFiGameFactory(GameFactory):
    def create_weapon(self):
        return LaserGun()
    
    def create_character(self):
        return Robot()
    
    def create_environment(self):
        return Spaceship()


# Abstract Product Interface - Weapon
class Weapon:
    def attack(self):
        pass


# Concrete Product 1 - Sword
class Sword(Weapon):
    def attack(self):
        print("Swinging sword!")


# Concrete Product 2 - Laser Gun
class LaserGun(Weapon):
    def attack(self):
        print("Shooting laser beam!")


# Abstract Product Interface - Character
class Character:
    def speak(self):
        pass


# Concrete Product 1 - Knight
class Knight(Character):
    def speak(self):
        print("For honor and glory!")


# Concrete Product 2 - Robot
class Robot(Character):
    def speak(self):
        print("I obey only my programming.")


# Abstract Product Interface - Environment
class Environment:
    def display(self):
        pass


# Concrete Product 1 - Castle
class Castle(Environment):
    def display(self):
        print("You are in a medieval castle.")


# Concrete Product 2 - Spaceship
class Spaceship(Environment):
    def display(self):
        print("You are in a futuristic spaceship.")


# Client code
def create_game(factory):
    weapon = factory.create_weapon()
    character = factory.create_character()
    environment = factory.create_environment()
    
    weapon.attack()
    character.speak()
    environment.display()

# Create a Fantasy Game
fantasy_factory = FantasyGameFactory()
create_game(fantasy_factory)

# Create a Sci-Fi Game
scifi_factory = SciFiGameFactory()
create_game(scifi_factory)


# In this example, we have an abstract GameFactory interface that defines the methods for creating different objects related to the game. We then have two concrete factories, FantasyGameFactory and SciFiGameFactory, that implement the methods of the GameFactory interface to create different objects based on the theme.

# We also have abstract product interfaces for Weapon, Character, and Environment, and concrete product classes that implement these interfaces for each theme. Finally, we have a client code that uses the factories to create objects and perform actions specific to each theme.

# By using the Abstract Factory pattern, we can easily switch between different themes without changing the client code, as the client only interacts with the abstract interfaces and the concrete factories. This allows us to create games with different themes and sets of objects, while maintaining a consistent interface for creating and using these objects.


# Abstract Factory Interface
class ProductFactory:
    def create_product(self):
        pass
    
    def create_shipping(self):
        pass


# Concrete Factory 1 - Book Factory
class BookFactory(ProductFactory):
    def create_product(self):
        return Book()
    
    def create_shipping(self):
        return BookShipping()


# Concrete Factory 2 - Electronic Device Factory
class ElectronicDeviceFactory(ProductFactory):
    def create_product(self):
        return ElectronicDevice()
    
    def create_shipping(self):
        return ElectronicDeviceShipping()


# Abstract Product Interface - Product
class Product:
    def get_info(self):
        pass


# Concrete Product 1 - Book
class Book(Product):
    def __init__(self):
        self.title = "Harry Potter and the Philosopher's Stone"
        self.author = "J.K. Rowling"
    
    def get_info(self):
        return f"{self.title} by {self.author}"


# Concrete Product 2 - Electronic Device
class ElectronicDevice(Product):
    def __init__(self):
        self.brand = "Apple"
        self.model = "iPhone 13 Pro"
    
    def get_info(self):
        return f"{self.brand} {self.model}"


# Abstract Product Interface - Shipping
class Shipping:
    def get_cost(self):
        pass


# Concrete Product 1 - Book Shipping
class BookShipping(Shipping):
    def get_cost(self):
        return 5.00


# Concrete Product 2 - Electronic Device Shipping
class ElectronicDeviceShipping(Shipping):
    def get_cost(self):
        return 10.00


# Client code
def order_product(factory):
    product = factory.create_product()
    shipping = factory.create_shipping()
    
    print(f"You ordered: {product.get_info()}")
    print(f"Shipping cost: ${shipping.get_cost()}")

# Create a Book order
book_factory = BookFactory()
order_product(book_factory)

# Create an Electronic Device order
device_factory = ElectronicDeviceFactory()
order_product(device_factory)


# In this example, we have an abstract ProductFactory interface that defines the methods for creating different objects related to the products. We then have two concrete factories, BookFactory and ElectronicDeviceFactory, that implement the methods of the ProductFactory interface to create different objects based on the type of product.

# We also have abstract product interfaces for Product and Shipping, and concrete product classes that implement these interfaces for each type of product. Finally, we have a client code that uses the factories to create objects and perform actions specific to each type of product.

# By using the Abstract Factory pattern, we can easily switch between different types of products without changing the client code, as the client only interacts with the abstract interfaces and the concrete factories. This allows us to create an online shop with different types of products and shipping methods, while maintaining a consistent interface for creating and using these objects.
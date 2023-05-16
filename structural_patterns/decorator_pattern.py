# The Decorator pattern is a structural design pattern that allows behavior to be added to an object dynamically. It provides a flexible alternative to subclassing for extending the functionality of an object at runtime. The pattern involves wrapping an object with one or more decorators, which are classes that implement the same interface as the object being decorated.

# Here's an example of the Decorator pattern in Python:

class Component:
    def operation(self):
        pass

class ConcreteComponent(Component):
    def operation(self):
        print("Performing operation in ConcreteComponent")

class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()

class ConcreteDecoratorA(Decorator):
    def operation(self):
        super().operation()
        self.add_additional_behavior()

    def add_additional_behavior(self):
        print("Adding additional behavior in ConcreteDecoratorA")

class ConcreteDecoratorB(Decorator):
    def operation(self):
        super().operation()
        self.add_extra_behavior()

    def add_extra_behavior(self):
        print("Adding extra behavior in ConcreteDecoratorB")


# Usage example
component = ConcreteComponent()
decorated_component = ConcreteDecoratorA(ConcreteDecoratorB(component))

decorated_component.operation()

#In this example, we have a base Component class that defines the interface for both the core component (ConcreteComponent) and the decorators (Decorator). The decorators inherit from the Component class and wrap an instance of the component class.

# The ConcreteComponent class represents the core functionality that we want to decorate. It implements the operation method.

# The Decorator class serves as the base class for concrete decorators. It contains an instance of the component and delegates the operation method to that component.

# The ConcreteDecoratorA and ConcreteDecoratorB classes are concrete decorators. They inherit from Decorator and add additional behavior before or after calling the wrapped component's operation method.

# In the usage example, we create a ConcreteComponent object and then wrap it with multiple decorators (ConcreteDecoratorA and ConcreteDecoratorB) in a cascading manner.

# When we call the operation method on the decorated component, it invokes the operation method of each decorator in the chain, as well as the core component. This allows the decorators to add their specific behavior before or after delegating the operation to the wrapped component.

# By using the Decorator pattern, we can dynamically add responsibilities to objects without modifying their structure or affecting other instances of the same class. It promotes code reuse, separation of concerns, and flexibility in extending the behavior of individual objects.


# This can also be done using the @decorator syntax in Python:

def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorator
def hello():
    print("Hello")

hello()

# In this example, we define a decorator function that takes a function as an argument and returns a wrapper function. The wrapper function adds additional behavior before and after calling the original function.

# We then use the @decorator syntax to decorate the hello function with the decorator function. This is equivalent to calling hello = decorator(hello).
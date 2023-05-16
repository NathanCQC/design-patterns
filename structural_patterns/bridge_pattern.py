class Implementor:
    def operation_implementation(self):
        pass

class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        return f"Abstraction: {self.implementor.operation_implementation()}"

class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        return "Concrete Implementor A"

class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        return "Concrete Implementor B"

# Create instances of the Abstraction class with different ConcreteImplementor objects
abstraction_a = Abstraction(ConcreteImplementorA())
abstraction_b = Abstraction(ConcreteImplementorB())

# Call the operation method on each Abstraction instance and print its result
print(abstraction_a.operation())  # Output: Abstraction: Concrete Implementor A
print(abstraction_b.operation())  # Output: Abstraction: Concrete Implementor B

#By using the Bridge pattern, we're able to separate the abstraction from its implementation, allowing them to vary independently. This can be useful in situations where we want to be able to switch between different implementations of an abstraction at runtime.

class Renderer:
    def render_circle(self, x, y, radius): # Can just think in terms of one shape if this is confusing
        pass

    def render_rectangle(self, x, y, width, height):
        pass

class Shape:
    def __init__(self, renderer, x, y):
        self.renderer = renderer
        self.x = x
        self.y = y

    def draw(self):
        pass

class Circle(Shape):
    def __init__(self, renderer, x, y, radius):
        super().__init__(renderer, x, y)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.x, self.y, self.radius)

class Rectangle(Shape):
    def __init__(self, renderer, x, y, width, height):
        super().__init__(renderer, x, y)
        self.width = width
        self.height = height

    def draw(self):
        self.renderer.render_rectangle(self.x, self.y, self.width, self.height)


# Concrete implementations of the renderer for different platforms
class RasterRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"RasterRenderer: Drawing a circle at ({x}, {y}) with radius {radius}")

    def render_rectangle(self, x, y, width, height):
        print(f"RasterRenderer: Drawing a rectangle at ({x}, {y}) with width {width} and height {height}")

class VectorRenderer(Renderer):
    def render_circle(self, x, y, radius):
        print(f"VectorRenderer: Drawing a circle at ({x}, {y}) with radius {radius}")

    def render_rectangle(self, x, y, width, height):
        print(f"VectorRenderer: Drawing a rectangle at ({x}, {y}) with width {width} and height {height}")


# Usage example
raster_renderer = RasterRenderer()
vector_renderer = VectorRenderer()

circle = Circle(raster_renderer, 10, 10, 5)
circle.draw()  # Output: RasterRenderer: Drawing a circle at (10, 10) with radius 5

rectangle = Rectangle(vector_renderer, 20, 20, 10, 5)
rectangle.draw()  # Output: VectorRenderer: Drawing a rectangle at (20, 20) with width 10 and height 5


# In this example, we have the Renderer abstract class that defines methods for rendering circles and rectangles. The Shape abstract class is the bridge that uses the Renderer implementation. We then have concrete implementations of the Renderer for different platforms (RasterRenderer and VectorRenderer).

# The Circle and Rectangle classes are concrete shapes that inherit from Shape. They override the draw method to use the appropriate render method provided by the Renderer implementation.

# By using the Bridge pattern, we can create different shapes and assign them different renderers at runtime. This allows us to decouple the shape abstraction from the specific rendering implementation, enabling us to switch between different renderers easily.

# In the example usage, we create a Circle instance with a RasterRenderer, and when calling draw, it uses the render_circle method of the RasterRenderer. Similarly, we create a Rectangle instance with a VectorRenderer, and when calling draw, it uses the render_rectangle method of the VectorRenderer.



#Q: how is this different to the abstract factory pattern?

#A: The Abstract Factory pattern is used to create families of related objects, whereas the Bridge pattern is used to separate an abstraction from its implementation so that they can vary independently.

# The Bridge pattern and the Abstract Factory pattern serve different purposes and address different concerns in software design.

# The Bridge pattern focuses on decoupling an abstraction from its implementation, allowing them to vary independently. It aims to separate the abstraction and implementation into separate class hierarchies, enabling them to evolve independently. The Bridge pattern emphasizes composition over inheritance, promoting flexibility and extensibility.

# On the other hand, the Abstract Factory pattern is a creational pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. It is concerned with creating objects of different types that belong to a particular family or category. The Abstract Factory pattern abstracts the process of object creation and encapsulates the details of object instantiation.

# Here are some key differences between the Bridge pattern and the Abstract Factory pattern:

# Purpose: The Bridge pattern is primarily concerned with separating an abstraction from its implementation, allowing them to vary independently. The Abstract Factory pattern, on the other hand, focuses on providing an interface for creating families of related objects.

# Relationship: In the Bridge pattern, the abstraction and implementation are connected using composition, where the abstraction contains a reference to the implementation. In the Abstract Factory pattern, there is typically a separate factory object responsible for creating and returning the desired objects.

# Scope: The Bridge pattern deals with the structural organization of classes and objects to achieve separation and decoupling. The Abstract Factory pattern is focused on the creation of objects and encapsulating the object creation process.

# To summarize, the Bridge pattern addresses the decoupling of an abstraction and its implementation, while the Abstract Factory pattern provides an interface for creating families of related objects. They serve different design goals and can be used in combination to achieve more complex software architectures.
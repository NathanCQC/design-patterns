
# The Composite pattern is a structural design pattern that allows you to treat individual objects and compositions of objects uniformly. It composes objects into tree-like structures to represent part-whole hierarchies. The pattern enables clients to interact with individual objects and groups of objects in a consistent manner.

# The key idea behind the Composite pattern is the concept of a component, which is an abstract base class that defines the common interface and behavior for both leaf objects (individual objects) and composite objects (objects that contain other objects). The composite object may recursively contain other composite objects and leaf objects, forming a hierarchical structure.

# Here's a simplified example to illustrate the Composite pattern:

class Component:
    def operation(self):
        pass

class Leaf(Component):
    def __init__(self, name):
        self.name = name

    def operation(self):
        print(f"Leaf '{self.name}' operation")

class Composite(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print(f"Composite '{self.name}' operation")

        for child in self.children:
            child.operation()


# Usage example
leaf1 = Leaf("Leaf 1")
leaf2 = Leaf("Leaf 2")

composite1 = Composite("Composite 1")
composite1.add(leaf1)
composite1.add(leaf2)

leaf3 = Leaf("Leaf 3")
leaf4 = Leaf("Leaf 4")

composite2 = Composite("Composite 2")
composite2.add(leaf3)
composite2.add(leaf4)

composite3 = Composite("Composite 3")
composite3.add(composite1)
composite3.add(composite2)

composite3.operation()


# In this extended example, we introduce additional layers of composite objects. Each composite object (Composite) can contain both leaf objects (Leaf) and other composite objects, forming a hierarchical structure.

# We create four leaf objects (leaf1, leaf2, leaf3, leaf4) and three composite objects (composite1, composite2, composite3). composite1 contains leaf1 and leaf2, composite2 contains leaf3 and leaf4, and composite3 contains both composite1 and composite2.

# When we call the operation method on composite3, it performs its specific operation and then delegates the operation to its child components. This delegation happens recursively through the hierarchy, allowing each component to perform its operation and propagate it to its children.

# The Composite pattern enables the creation of complex object structures by combining individual objects and compositions of objects. It provides a unified way to interact with these structures, treating them uniformly regardless of their level of nesting.


# The Facade pattern is a structural design pattern that provides a simplified interface to a complex system, making it easier to use and understand. It hides the complexity of the underlying subsystem by providing a unified interface for clients to interact with.

# Here's an example of the Facade pattern in Python:

# Complex subsystem classes
class SubsystemA:
    def operation_a(self):
        print("Subsystem A: Operation A")

class SubsystemB:
    def operation_b(self):
        print("Subsystem B: Operation B")

class SubsystemC:
    def operation_c(self):
        print("Subsystem C: Operation C")


# Facade class
class Facade:
    def __init__(self):
        self.subsystem_a = SubsystemA()
        self.subsystem_b = SubsystemB()
        self.subsystem_c = SubsystemC()

    def operation(self):
        self.subsystem_a.operation_a()
        self.subsystem_b.operation_b()
        self.subsystem_c.operation_c()


# Usage example
facade = Facade()
facade.operation()

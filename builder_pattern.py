class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_office_computer(self):
        # Use the builder to set the attributes of an office computer
        self.builder.set_processor("Intel Core i5-11400") \
                    .set_ram("16 GB DDR4") \
                    .set_storage("512 GB SATA SSD")

        # Return the constructed office computer
        return self.builder.get_computer()

    def build_gaming_computer(self):
        # Use the builder to set the attributes of a gaming computer
        self.builder.set_processor("Intel Core i9-11900K") \
                    .set_ram("32 GB DDR4") \
                    .set_storage("1 TB NVMe SSD") \
                    .set_gpu("NVIDIA GeForce RTX 3080")

        # Return the constructed gaming computer
        return self.builder.get_computer()

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_processor(self, processor):
        # Set the processor attribute of the computer object
        self.computer.processor = processor
        # Return the builder object for method chaining
        return self

    def set_ram(self, ram):
        # Set the RAM attribute of the computer object
        self.computer.ram = ram
        # Return the builder object for method chaining
        return self

    def set_storage(self, storage):
        # Set the storage attribute of the computer object
        self.computer.storage = storage
        # Return the builder object for method chaining
        return self

    def set_gpu(self, gpu):
        # Set the GPU attribute of the computer object
        self.computer.gpu = gpu
        # Return the builder object for method chaining
        return self

    def get_computer(self):
        # Return the constructed computer object
        return self.computer

class Computer:
    def __init__(self):
        self.processor = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Processor: {self.processor}, RAM: {self.ram}, Storage: {self.storage}, GPU: {self.gpu}"

# Create a builder object
builder = ComputerBuilder()

# Create a director object with the builder object as a parameter
director = ComputerDirector(builder)

# Build an office computer using the director object
office_computer = director.build_office_computer()

# Build a gaming computer using the director object
gaming_computer = director.build_gaming_computer()

# Print the constructed computers
print(office_computer)
print(gaming_computer)

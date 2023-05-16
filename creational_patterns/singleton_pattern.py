class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("Singleton instance already exists")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
    

#The Singleton pattern can be useful in situations where you need to ensure that there is only one instance of a class, such as when working with a shared resource or managing system-wide configuration data. However, it's important to use the Singleton pattern judiciously, as it can introduce global state and make code harder to test and maintain.
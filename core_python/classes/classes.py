
################################
# defination of classes:
# A class is a blueprint for creating objects (instances). It defines a set of attributes and methods that the created objects will have.
# When to use: Use classes when you need to create multiple objects with similar properties and behaviors.
# Common methods: __init__(), __str__(), __repr__()
# Example of each method :
#   __init__(): Initializes the object's attributes when it is created.
#   __str__(): Returns a string representation of the object, used by print() and str().
#   __repr__(): Returns an unambiguous string representation of the object, used by repr().

# Note: init is mandatory to create an object of class

# add any thing about classes here
    # Classes are used to define objects with shared attributes and behaviors.
    # They allow for encapsulation, inheritance, and polymorphism.

    # important concepts:
    # 1. Encapsulation: Bundling data and methods that operate on that data within
    #    a single unit (class).
    # 2. Inheritance: Creating a new class based on an existing class to promote
    #    code reuse.
    # 3. Polymorphism: The ability to present the same interface for different data types.  

# defination of objects:
# An object is an instance of a class. It is created using the class blueprint and has its own unique state and behavior.
# When to use: Use objects when you want to create specific instances of a class with their own data.
# Example: If you have a class Dog, you can create multiple Dog objects, each representing a different dog with its own name and age.

##########################################
import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)


class Animal:
    def __init__(self, name):
        self.name = name
        logger.info(f"Animal object created: {self.name}")

    def __str__(self):
        return f"This is an animal named {self.name}."

    def __repr__(self):
        return f"Animal(name='{self.name}')"
    
# Example usage:
if __name__ == "__main__":
    my_animal = Animal("Generic Animal")
    print(my_animal)  # Uses __str__()
    logger.info(repr(my_animal))  # Uses __repr__()

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        logger.info(f"Dog object created: {self.name}, Age: {self.age}")

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Dog(name='{self.name}', age={self.age})"
    

# Example usage:
if __name__ == "__main__":
    my_dog = Dog("Buddy", 3)
    print(my_dog)  # Uses __str__()
    logger.info(repr(my_dog))  # Uses __repr__()


class Bird:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        logger.info(f"Bird object created: {self.name}, Species: {self.species}")

    def __str__(self):
        return f"{self.name} is a {self.species}."

    def __repr__(self):
        return f"Bird(name='{self.name}', species='{self.species}')"
    
# Example usage:
if __name__ == "__main__":
    my_bird = Bird("Tweety", "canary")
    print(my_bird)  # Uses __str__()
    logger.info(repr(my_bird))  # Uses __repr__()


class Parrot(Bird):
    def __init__(self, name, species, can_fly):
        super().__init__(name, species)
        self.can_fly = can_fly
        logger.info(f"Parrot object created: {self.name}, Species: {self.species}, Can fly: {self.can_fly}")

    def __str__(self):
        fly_status = "can fly" if self.can_fly else "cannot fly"
        return f"{self.name} is a {self.species} that {fly_status}."

    def __repr__(self):
        return f"Parrot(name='{self.name}', species='{self.species}', can_fly={self.can_fly})"
    
# Example usage:
if __name__ == "__main__":
    my_parrot = Parrot("Polly", "African Grey", True)
    print(my_parrot)  # Uses __str__()
    logger.info(repr(my_parrot))  # Uses __repr__()


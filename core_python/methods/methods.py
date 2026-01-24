############################
# Definitions: Methods in Python are defined using the 'def' keyword.
# when to use: Use methods when you want to encapsulate a block of code that performs a specific task and can be reused throughout your program.
# types of methods: Instance methods, Class methods, Static methods.
# explain each type of method:
#   - Instance Methods: These methods operate on an instance of a class. They can access
#     and modify the instance's attributes. They are defined with 'self' as the first parameter.
#   - Class Methods: These methods operate on the class itself rather than on instances of the class.
#     They are defined with 'cls' as the first parameter and are decorated with '@classmethod'.
#   - Static Methods: These methods do not operate on an instance or class. They are defined without 'self' or 'cls' parameters
#     and are decorated with '@staticmethod'. They are used for utility functions that do not require access to instance or class data.

############################

import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)

class Example:
    def instance_method(self):
        """An instance method that accesses instance attributes."""
        return "This is an instance method."

    @classmethod
    def class_method(cls):
        """A class method that accesses class attributes."""
        return "This is a class method."

    @staticmethod
    def static_method():
        """A static method that does not access instance or class attributes."""
        return "This is a static method."
    
# example usage:
example = Example()
logger.info(example.instance_method())  # Output: This is an instance method.
logger.info(Example.class_method())     # Output: This is a class method.
logger.info(Example.static_method())    # Output: This is a static method.


# example of a method with parameters and return value
def add_numbers(a, b):
    """A simple method that adds two numbers and returns the result."""
    return a + b

# example usage:
result = add_numbers(5, 7)
logger.info(f"The sum of 5 and 7 is: {result}")  # Output: The sum of 5 and 7 is: 12

# example of a method with default parameters
def greet(name, greeting="Hello"):
    """A method that greets a person with a given greeting."""
    return f"{greeting}, {name}!" 

# example usage:
logger.info(greet("Alice"))               # Output: Hello, Alice!
logger.info(greet("Bob", greeting="Hi"))  # Output: Hi, Bob!

# example of a method with variable-length arguments
def multiply(*args):
    """A method that multiplies all given numbers."""
    result = 1
    for num in args:
        result *= num
    return result

# example usage:
logger.info(f"The product of 2, 3, and 4 is: {multiply(2, 3, 4)}")  # Output: The product of 2, 3, and 4 is: 24
logger.info(f"The product of 5 and 6 is: {multiply(5, 6)}")        # Output: The product of 5 and 6 is: 30

# example of a method with keyword arguments
def display_info(**kwargs):
    """A method that displays information passed as keyword arguments."""
    info = []
    for key, value in kwargs.items():
        info.append(f"{key}: {value}")
    return ", ".join(info)

# example usage:
logger.info(display_info(name="Alice", age=30, city="New York"))  # Output: name: Alice, age: 30, city: New York
logger.info(display_info(product="Laptop", price=1200, stock=50))  # Output: product: Laptop, price: 1200, stock: 50

# example of a recursive method
def factorial(n):
    """A recursive method that calculates the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# example usage:
logger.info(f"The factorial of 5 is: {factorial(5)}")  # Output: The factorial of 5 is: 120
logger.info(f"The factorial of 0 is: {factorial(0)}")  # Output: The factorial of 0 is: 1   

# example of a method with error handling
def divide_numbers(a, b):
    """A method that divides two numbers with error handling for division by zero."""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result

# example usage:
logger.info(f"10 divided by 2 is: {divide_numbers(10, 2)}")  # Output: 10 divided by 2 is: 5.0
logger.info(f"10 divided by 0 is: {divide_numbers(10, 0)}")  # Output: 10 divided by 0 is: Error: Division by zero is not allowed

# example of a method with docstring
def square(number):
    """A method that returns the square of a number."""
    return number * number

# example usage:
logger.info(f"The square of 4 is: {square(4)}")  # Output: The square of 4 is: 16
logger.info(f"The square of 7 is: {square(7)}")  # Output: The square of 7 is: 49

# example of a method with type hints
def concatenate_strings(str1: str, str2: str) -> str:
    """A method that concatenates two strings."""
    return str1 + str2

# example usage:
logger.info(concatenate_strings("Hello, ", "World!"))  # Output: Hello, World!
logger.info(concatenate_strings("Python ", "Methods"))   # Output: Python Methods

# example of a method with lambda function
square_lambda = lambda x: x * x
# example usage:
logger.info(f"The square of 6 using lambda is: {square_lambda(6)}")  # Output: The square of 6 using lambda is: 36
logger.info(f"The square of 9 using lambda is: {square_lambda(9)}")  # Output: The square of 9 using lambda is: 81

# example of a method with map function
def double_numbers(numbers):
    """A method that doubles each number in a list using map."""
    return list(map(lambda x: x * 2, numbers))

# example usage:
logger.info(f"Doubled numbers: {double_numbers([1, 2, 3, 4])}")  # Output: Doubled numbers: [2, 4, 6, 8]
logger.info(f"Doubled numbers: {double_numbers([5, 6, 7])}")     # Output: Doubled numbers: [10, 12, 14]    

# example of a method with filter function
def filter_even_numbers(numbers):
    """A method that filters even numbers from a list using filter."""
    return list(filter(lambda x: x % 2 == 0, numbers))  

# example usage:
logger.info(f"Even numbers: {filter_even_numbers([1, 2, 3, 4, 5, 6])}")  # Output: Even numbers: [2, 4, 6]
logger.info(f"Even numbers: {filter_even_numbers([7, 8, 9, 10])}")        # Output: Even numbers: [8, 10]

# example of a method with reduce function
from functools import reduce
def sum_numbers(numbers):
    """A method that sums all numbers in a list using reduce."""
    return reduce(lambda x, y: x + y, numbers)

# example usage:
logger.info(f"The sum of numbers is: {sum_numbers([1, 2, 3, 4, 5])}")  # Output: The sum of numbers is: 15
logger.info(f"The sum of numbers is: {sum_numbers([10, 20, 30])}")     # Output: The sum of numbers is: 60

# example of a method with list comprehension
def square_list(numbers):
    """A method that returns a list of squares using list comprehension."""
    return [x * x for x in numbers] 

# example usage:
logger.info(f"Squares of numbers: {square_list([1, 2, 3, 4])}")  # Output: Squares of numbers: [1, 4, 9, 16]
logger.info(f"Squares of numbers: {square_list([5, 6, 7])}")     # Output: Squares of numbers: [25, 36, 49]

# example of a method with generator
def generate_squares(n):
    """A generator method that yields squares of numbers up to n."""
    for i in range(n):
        yield i * i 

# example usage:
squares_generator = generate_squares(5)
logger.info(f"Squares generated: {list(squares_generator)}")  # Output: Squares generated: [0, 1, 4, 9, 16]
squares_generator = generate_squares(3)
logger.info(f"Squares generated: {list(squares_generator)}")  # Output: Squares generated: [0, 1, 4]    

# example of a method with decorators
def decorator_function(original_function):
    """A simple decorator that logs the execution of a method."""
    def wrapper_function(*args, **kwargs):
        logger.info(f"Executing {original_function.__name__}...")
        result = original_function(*args, **kwargs)
        logger.info(f"{original_function.__name__} executed.")
        return result
    return wrapper_function

@decorator_function
def say_hello(name):
    """A method that says hello to a person."""
    return f"Hello, {name}!"    

# example usage:
logger.info(say_hello("Alice"))  # Output: Hello, Alice!
logger.info(say_hello("Bob"))    # Output: Hello, Bob!  

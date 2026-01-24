############################
# Definitions: Functions in Python are defined using the 'def' keyword.
# when to use: Use functions when you want to encapsulate a block of code that performs a specific task and can be reused throughout your program.
# types of functions: Built-in functions, User-defined functions, Anonymous functions (lambdas).
# explain each type of function:
#   - Built-in Functions: These are functions that are pre-defined in Python and can be used directly without any additional code. Examples include 'print()', 'len()', and 'type()'.
#   - User-defined Functions: These are functions that you define yourself using the 'def' keyword. They can take parameters and return values.
#   - Anonymous Functions (Lambdas): These are small, unnamed functions defined using the 'lambda' keyword. They are typically used for short, 
#           throwaway functions that are not reused elsewhere.

# fuction vs method:
# A function is a standalone block of code that performs a specific task, while a method is a function that is associated with an object (usually an instance of a class) 
#           and can operate on the data contained within that object.
############################

import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)

def built_in_function_example():
    """An example of a built-in function."""
    sample_list = [1, 2, 3, 4, 5]
    length = len(sample_list)  # Using the built-in len() function
    return f"The length of the list is: {length}"

def user_defined_function_example(x, y):
    """An example of a user-defined function."""
    return x + y

def anonymous_function_example():
    """An example of an anonymous function (lambda)."""
    multiply = lambda a, b: a * b
    return multiply(3, 4)

# example lambda functions:
lambda_add = lambda x: x + 10
logger.info(f"Lambda add function output: {lambda_add(5)}")  # Output: Lambda add function output: 15
    
# example usage:
logger.info(built_in_function_example())  # Output: The length of the list is:
logger.info(f"Sum from user-defined function: {user_defined_function_example(5, 7)}")  # Output: Sum from user-defined function: 12
logger.info(f"Product from anonymous function: {anonymous_function_example()}")  # Output: Product from anonymous function: 12

# function vs method example:
# A method is a function that is associated with an object.
# Here is an example of a method within a class:
# example class with a method: 

class SampleClass:
    def __init__(self, value):
        self.value = value

    def method_example(self):
        """An example of a method."""
        return f"The value is: {self.value}"
    
sample_object = SampleClass(10)
logger.info(sample_object.method_example())  # Output: The value is: 10
# In this example, 'method_example' is a method of the 'SampleClass' class, while the previous functions are standalone functions.

# example of a built-in function:
logger.info(f"Type of sample_object: {type(sample_object)}")  # Output: Type of sample_object: <class '__main__.SampleClass'>

# example of a user-defined function:
def greet(name):
    return f"Hello, {name}!"
logger.info(greet("Alice"))  # Output: Hello, Alice!

# example of an anonymous function (lambda):
square = lambda x: x * x
logger.info(f"Square of 6: {square(6)}")  # Output: Square of 6: 36 

# In this example, 'greet' is a user-defined function that takes a name as a parameter and returns a greeting message.
# 'square' is an anonymous function that takes a number and returns its square.

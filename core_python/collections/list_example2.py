import logging

#########################################

format = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(
    format=format, 
    datefmt=datefmt, 
    level=logging.INFO
    )

logger = logging.getLogger(__name__)

def demonstrate_list_operations():
    try:

        logger.info("Demonstrating basic list operations in Python.")

        # Creating a list
        fruits = ['apple', 'banana', 'cherry']
        logger.info(f"Initial list: {fruits}")

        # Accessing elements
        first_fruit = fruits[0]
        logger.info(f"First fruit: {first_fruit}")

        # Modifying elements
        fruits[1] = 'blueberry'
        logger.info(f"Modified list: {fruits}")

        # Adding elements
        fruits.append('date')
        logger.info(f"List after appending: {fruits}")

        # Removing elements
        fruits.remove('cherry')
        logger.info(f"List after removing cherry: {fruits}")

        # Slicing the list
        sliced_fruits = fruits[1:3]
        logger.info(f"Sliced list (index 1 to 2): {sliced_fruits}")

        # Iterating through the list
        for fruit in fruits:
            logger.info(f"Fruit in list: {fruit}")
        

    except Exception as e:
        logger.error(f"An error occurred: {e}")

def define_nested_list():
    try:
        # Creating a nested list
        nested_list = [['red', 'green'], ['blue', 'yellow']]
        logger.info(f"Nested list: {nested_list}")  
        # Accessing elements in a nested list
        first_color = nested_list[0][1]
        logger.info(f"First color in nested list: {first_color}")

    except Exception as e:
        logger.error(f"An error occurred while handling nested list: {e}")


if __name__ == "__main__":

    demonstrate_list_operations()
    define_nested_list()

    logger.info("List operations demonstration completed.")
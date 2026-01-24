# from default_logger import Logger
from default_logger.loggers import Logger
logger = Logger.get_logger(__name__)

def demonstrate_tuple_operations():
    try:
        logger.info("Demonstrating basic tuple operations in Python.")

        # Creating a tuple
        colors = ('red', 'green', 'blue')
        logger.info(f"Initial tuple: {colors}")

        # Accessing elements
        first_color = colors[0]
        logger.info(f"First color: {first_color}")

        # Slicing the tuple
        sliced_colors = colors[1:3]
        logger.info(f"Sliced tuple (index 1 to 2): {sliced_colors}")

        # Iterating through the tuple
        for color in colors:
            logger.info(f"Color in tuple: {color}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

def define_nested_tuple():
    try:
        # Creating a nested tuple
        nested_tuple = (('circle', 'square'), ('triangle', 'rectangle'))
        logger.info(f"Nested tuple: {nested_tuple}")  
        # Accessing elements in a nested tuple
        first_shape = nested_tuple[0][1]
        logger.info(f"First shape in nested tuple: {first_shape}")

    except Exception as e:
        logger.error(f"An error occurred while handling nested tuple: {e}")


if __name__ == "__main__":
    
    demonstrate_tuple_operations()
    define_nested_tuple()


    
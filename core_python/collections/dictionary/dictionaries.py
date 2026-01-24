
################################
# Definition : A dictionary is an unordered collection of key-value pairs in Python.
# When to use : Use dictionaries when you need to associate unique keys with values for efficient look
# Common methods : get(), keys(), values(), items(), update()
# Example of each method :
#   get(): Returns the value for a specified key. If the key does not exist,
#          it returns None (or a specified default value).
#   keys(): Returns a view object that displays a list of all the keys in the dictionary.
#   values(): Returns a view object that displays a list of all the values in the dictionary.
#   items(): Returns a view object that displays a list of dictionary's key-value tuple pairs.
#   update(): Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.
################################
import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)


def demonstrate_dictionary_operations():
    try:
        logger.info("Demonstrating basic dictionary operations in Python.")

        # Creating a dictionary
        student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
        logger.info(f"Initial dictionary: {student}")

        # Using get() method
        name = student.get('name')
        logger.info(f"Name retrieved using get(): {name}")

        # Using keys() method
        keys = student.keys()
        logger.info(f"Keys in the dictionary: {list(keys)}")

        # Using values() method
        values = student.values()
        logger.info(f"Values in the dictionary: {list(values)}")

        # Using items() method
        items = student.items()
        logger.info(f"Items in the dictionary: {list(items)}")

        # Using update() method
        student.update({'age': 21, 'graduation_year': 2023})
        logger.info(f"Dictionary after update: {student}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

def demonstrate_nested_dictionaries():
    try:
        # Creating a nested dictionary
        university = {
            'name': 'Tech University',
            'location': 'Cityville',
            'departments': {
                'Computer Science': {'head': 'Dr. Smith', 'students': 200},
                'Mathematics': {'head': 'Dr. Jones', 'students': 150}
            }
        }
        logger.info(f"Nested dictionary: {university}")

        # Accessing elements in a nested dictionary
        cs_head = university['departments']['Computer Science']['head']
        logger.info(f"Head of Computer Science department: {cs_head}")

    except Exception as e:
        logger.error(f"An error occurred while handling nested dictionary: {e}")


def main():
    demonstrate_dictionary_operations()
    demonstrate_nested_dictionaries()

if __name__ == "__main__":
    main()
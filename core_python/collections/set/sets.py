
#############################################
# defination : A set is an unordered collection of unique items in Python.
# when to use : Use sets when you want to store a collection of items without duplicates and
# common methods : add(), remove(), union(), intersection(), difference()
# examplin each method :
#   add(): Adds an item to the set.
#   remove(): Removes a specified item from the set.
#   union(): Returns a new set with all items from both sets.
#   intersection(): Returns a new set with items common to both sets.
#   difference(): Returns a new set with items in the first set but not in the second.

#############################################
import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)

def demonstrate_set_operations():
    try:
        logger.info("Demonstrating basic set operations in Python.")

        # Creating a set
        fruits = {'apple', 'banana', 'cherry'}
        logger.info(f"Initial set: {fruits}")

        # Adding an element
        fruits.add('orange')
        logger.info(f"Set after adding 'orange': {fruits}")

        # Removing an element
        fruits.remove('banana')
        logger.info(f"Set after removing 'banana': {fruits}")

        # Union of sets
        tropical_fruits = {'mango', 'pineapple'}
        all_fruits = fruits.union(tropical_fruits)
        logger.info(f"Union of sets: {all_fruits}")

        # Intersection of sets
        common_fruits = fruits.intersection({'apple', 'kiwi', 'orange'})
        logger.info(f"Intersection of sets: {common_fruits}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


def define_frozenset():
    try:
        # Creating a frozenset
        frozen_fruits = frozenset(['apple', 'banana', 'cherry'])
        logger.info(f"Frozenset: {frozen_fruits}")  
        # Attempting to add an element to frozenset (will raise an error)
        try:
            frozen_fruits.add('orange')
        except AttributeError as ae:
            logger.warning(f"Cannot add to frozenset: {ae}")

    except Exception as e:
        logger.error(f"An error occurred while handling frozenset: {e}")

def main():
    demonstrate_set_operations()
    define_frozenset()

if __name__ == "__main__":
    main()
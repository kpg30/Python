
################################
# defination : A list is an ordered collection of items in Python.
# when to use : Use lists when you need to maintain the order of items and allow duplicates
# common methods : append(), remove(), pop(), sort(), reverse()
# examplin each method :
#   append(): Adds an item to the end of the list.
#   remove(): Removes the first occurrence of a specified item from the list.
#   pop(): Removes and returns the item at the given index (default is the last item).
#   sort(): Sorts the items of the list in ascending order.
#   reverse(): Reverses the order of the items in the list.
################################

import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)


def demonstrate_list_operations():
    try:
        logger.info("Demonstrating basic list operations in Python.")

        # Creating a list
        fruits = ['apple', 'banana', 'cherry']
        logger.info(f"Initial list: {fruits}")

        # Appending an element
        fruits.append('orange')
        logger.info(f"List after appending 'orange': {fruits}")

        # Removing an element
        fruits.remove('banana')
        logger.info(f"List after removing 'banana': {fruits}")

        # Popping an element
        popped_fruit = fruits.pop()
        logger.info(f"Popped element: {popped_fruit}")
        logger.info(f"List after popping: {fruits}")

        # Sorting the list
        fruits.sort()
        logger.info(f"Sorted list: {fruits}")

        # Reversing the list
        fruits.reverse()
        logger.info(f"Reversed list: {fruits}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")


def demonstrate_nested_lists():
    try:
        # Creating a nested list
        nested_list = [['apple', 'banana'], ['cherry', 'date']]
        logger.info(f"Nested list: {nested_list}")

        # Accessing elements in a nested list
        first_sublist = nested_list[0]
        logger.info(f"First sublist: {first_sublist}")

        first_element = nested_list[0][0]
        logger.info(f"First element of the first sublist: {first_element}")

    except Exception as e:
        logger.error(f"An error occurred while handling nested lists: {e}")


def main():
    demonstrate_list_operations()
    demonstrate_nested_lists()

if __name__ == "__main__":
    main()
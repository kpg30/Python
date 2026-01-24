
##############################################
# defination : Exception handling in Python allows you to manage errors gracefully without crashing the program.
# when to use : Use exception handling when you want to catch and handle errors that may occur during program execution.
# common methods : try, except, finally, raise
# examplin each method :
#   try: The block of code to be tested for errors.
#   except: The block of code that runs if an error occurs in the try block.
#   finally: The block of code that runs regardless of whether an error occurred or not.
#   raise: Used to manually raise an exception.
        # when can we use raise e?
                # You can use raise e to re-raise an exception that was caught in an except block.
                # This is useful when you want to handle the exception but still propagate it up the call stack.
        # general syntax of raise e:
                # try:
                #     # code that may raise an exception
                # except SomeException as e:
                #     # handle the exception
                #     raise e  # re-raise the caught exception
##############################################

import logging
formatter = '%(asctime)s - %(filename)s - %(levelname)s,line%(lineno)d: %(message)s'
datefmt = '%Y-%m-%d %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=formatter, datefmt=datefmt)
logger = logging.getLogger(__name__)


def demonstrate_exception_handling():
    try:
        logger.info("Demonstrating exception handling in Python.")

        # Example of try and except
        numerator = 10
        denominator = 0
        result = numerator / denominator  # This will raise a ZeroDivisionError
        logger.info(f"Result: {result}")

    except ZeroDivisionError as e:
        logger.error(f"Caught an exception: {e}")

    finally:
        logger.info("Execution of the try-except block is complete.")


def raise_custom_exception():
    try:
        logger.info("Raising a custom exception.")

        # Manually raising an exception
        raise ValueError("This is a custom ValueError exception.")

    except ValueError as e:
        logger.error(f"Caught a custom exception: {e}")


def main():
    demonstrate_exception_handling()
    raise_custom_exception()

if __name__ == "__main__":
    main()


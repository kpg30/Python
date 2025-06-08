import logging
from python.service2.utils.class_test.classes6 import *
from python.service2.utils.default_logger import get_logger
 
# def main():
#     p = Student('Prasad', 32, 'Male', 'India')
#     p.profile()
#
#     print(f"Sum is : {p.Addition(60, 30)}")

frmt = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=frmt)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        p = Student('Prasad', 32, 'Male', 'India')
        p.profile()

        logger.info(f"Sum is : {p.Addition(60, 30)}")
        logger.info(f"successfully fetched profile information")

    except Exception as e:
        logger.error("Error while fetching profile information")
        raise e

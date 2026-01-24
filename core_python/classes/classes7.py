
from classes6 import *
from loggers import Logger

logger=Logger.get_logger(__name__)

if __name__ == "__main__":
    try:
        p = Student('Prasad', 32, 'Male', 'India')
        p.profile()

        logger.info(f"Sum is : {p.Addition(60, 30)}")
        logger.info(f"successfully fetched profile information")

    except Exception as e:
        logger.error("Error while fetching profile information")
        raise e


from default_logger.loggers import Logger

logger = Logger.get_logger(__name__)
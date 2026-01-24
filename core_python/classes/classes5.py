import logging


"""
import logging
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    - The logging.Formatter class is used to specify the format of log messages.
    - The fmt argument defines the layout, using placeholders like:
    - %asctime)s: Timestamp of the log event.
    - %levelname)s: Log level (e.g., DEBUG, INFO, WARNING).
    - %message)s: The actual log message.
    - %name)s: Name of the logger.
    - %filename)s: File name where the log originated.
    - %lineno)d: Line number where the log originated.
"""

format1 = '%(asctime)s - %(levelname)s: %(message)s'
format2 = '%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, format=format2)
logger = logging.getLogger(__name__)

# format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# 'datefmt=%Y-%m-%d %H:%M:%S'
# logging.basicConfig(level=logging.INFO, format=format)
# logger = logging.getLogger(__name__)


def sample():
    logger.info("hello india")
    logger.info("hello prasad")
    logger.error("error")
    # logger.debug("debug")
    # print("hello hyd")


sample()

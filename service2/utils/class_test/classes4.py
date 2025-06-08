import logging
#import logging.config
from learn2025.classesAndObjects.loggers import Logger

# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s: %(message)s')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


class Test11:
    def findDiv(self, n):
        try:
            logging.info("running")
            result = n / 2
            logging.info(int(result))
        except Exception as error:
            # logging.error(error)
            logging.error(f"Error while running ,{error}")
            raise error


if __name__ == "__main__":
    obj = Test11()
    obj.findDiv(20)

from loggers.default_logger import Logger

logger = Logger.get_logger("test_case4")

numbers = [1,3,4,5,6,7,8]
tgt = 3
for number in numbers:
    logger.info(f"Processing {number}...")
    if number == tgt:
        logger.info(f"Target found {tgt}")
        break
    else:
        logger.info("Target Not Found")
        #raise Exception("Target Not Found")
    
for number in numbers:
    logger.info(f"{number = }")
    if  number % 2 != 0:
        continue
    logger.info(f"{number} is even")
    
for number in numbers:
    logger.info(f"{number = }")
    if  number % 2 == 0:
        continue
    logger.info(f"{number} is odd")
  
# Find unique items from List  
colors = ["red", "red","green", "blue", "yellow"]
@staticmethod
def get_unique_items(list_object):
    result = []
    for item in list_object:
        if item not in result:
            result.append(item)
    return result

final_list = get_unique_items(colors)
logger.info(final_list)
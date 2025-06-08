import logging

logger = logging.getLogger('setExample2.py')
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

this_set = {"apple", "banana", "cherry"}
logger.info(f"Before: {this_set}")

try:
    for name in this_set:
        x = 'new_' + name.upper()
        logger.info(f"After: {x}")

except Exception as error:
    logger.error("error while reading the SET values", error)

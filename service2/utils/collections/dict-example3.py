import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

logger.info("This is a Dict:\n")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict['year'] = 2025
logger.info(thisdict.get('year'))
logger.info(thisdict.keys())
logger.info(thisdict.values())

for key in thisdict.keys():
    logger.info(key)

# for key, value in thisdict.items():
#     logger.info(key, value)

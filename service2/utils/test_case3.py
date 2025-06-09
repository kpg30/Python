from loggers.default_logger import Logger

logger = Logger.get_logger("test_case3")

# creating a dictionary
countries = {
    "India": "Delhi",
    "Germany": "Berlin", 
    "Canada": "Ottawa", 
    "England": "London"
}

logger.info(countries)
logger.info("India Capital is : "  + countries["India"])
logger.info("England Capital is : " + countries["England"])

for k,v in countries.items():
    logger.info(f"{k.upper()} : {v.lower()}")
    #logger.info(f"{k},{v}")
    
logger.info("-- Length of each key and value in Dict --")
for k, v in countries.items():
    key_length = len(k)
    value_length = len(v)
    logger.info(f"{key_length} : {value_length}")
    

dict1 = {
    "name" : "Prasad",
    "place" : "Hyd",
    "gender" : "Male"
    }

dict2 = {
    "phone":"1-xxx-xxx-xxxx",
    "status": "Active"
}

logger.info(dict1)
dict1.update(dict2)
logger.info(dict1)
logger.info(dict2)

get_name1 = dict1.get('name')
get_name2 = dict1["name"]
logger.info(get_name1)
logger.info(get_name2)


dict_to_list = list(dict1.items())[1][1]
logger.info(dict_to_list)
    

from loggers.default_logger import Logger

logger = Logger.get_logger("test_case5")


class Dog:
    
    def __init__(self, name, color, price) :
        self.name = name
        self.color = color
        self.price = price
    
    def get_color(self):
        
        return self.color

obj = Dog("pk", "blue",30000)
get_color = obj.get_color()
logger.info(get_color)

    

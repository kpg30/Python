from loggers.default_logger import Logger

logger = Logger.get_logger("test_case2")

class Robot:
    
    def __init__(self) -> None:
        self.name = ""
        self.color = ""
        self.weight = ""
    
    def is_introduce1(self, name, color, weight):
        logger.info(f"Name is : {name}")
        logger.info(f"Color is : {color}")
        logger.info(f"Weight is : {weight}")
    
    @staticmethod    
    def is_introduce(name: str, color: str, weight: int):
        logger.info("my name is : " + name)


def main():
    r1 = Robot()
    name = "Prasad"
    color = "red"
    weight = 35

    r1.is_introduce(name, color, weight)
    r1.is_introduce1(name, color, weight)
    
    r2 = Robot()
    name = "James"
    color = "blue"
    weight = 30

    r2.is_introduce(name, color, weight)
    
           
if __name__ == "__main__":
    main()

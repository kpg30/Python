import logging

class Logger:
    
    logging.basicConfig(
        level=logging.INFO,
        #format='%(asctime)s %(levelname)s %(name)s: %(message)s',
        format='%(asctime)s %(levelname)s %(filename)s,line%(lineno)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        return logging.getLogger(name)
    

# Example usage:
# if __name__ == "__main__":
#     logger = Logger.get_logger(__name__)
#     logger.info("This is an info message from the default logger.")
#     logger.error("This is an error message from the default logger.")
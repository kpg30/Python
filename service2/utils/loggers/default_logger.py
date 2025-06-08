import logging

class Logger:
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        return logging.getLogger(name)
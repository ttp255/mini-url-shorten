
import logging
class LoggerService:
    def __init__(self,nameLogger:str):
        self.nameLogger=nameLogger
        self._get_logger()

    def _get_logger(self):
        # Set logger config
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger=logging.getLogger(self.nameLogger)

    def info(self,message:str):
        # Logger info message
        self.logger.info(message)


    def error(self,message:str):
        # Logger error message
        self.logger.error(message)
    
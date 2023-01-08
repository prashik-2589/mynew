import logging


class Loggen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="Logs/automation.log", format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger














    # @staticmethod
    # def getthelogs(self):
    #     logger = logging.getLogger()
    #     filehandler = logging.FileHandler('mylog.log')
    #     formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    #     filehandler.setFormatter(formatter)
    #     logger.addHandler(filehandler)
    #     logger.setLevel(logging.INFO)
    #     return logger

import logging


class LogGen:

    @staticmethod
    def loggen():
        #give the path of log file and  format
        logging.basicConfig(filename="/Users/manish/PycharmProjects/pytest_01/Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m%d%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
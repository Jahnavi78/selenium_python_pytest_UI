import logging  #predefined package in python
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".//python_selenium_pytest/Logs/automation.log",force=True,
 format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

#we dont do this for every testcase...if we set one time we can use for entire project
#this will create log file in specified path and store logs in specified format
#what logs will store means ..that we will mention in another file


import configparser #we cant use this data directly we need utilities file which helps us to read common data
import os
config= configparser.RawConfigParser()

path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "Configurations",
    "config.ini"
)

config.read(path)

class ReadConfig:
    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getApplicationURL():
        url=config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def geturl():
        url=config.get("Ultimate qa", "url")
        return url


#To read data from config.ini
import configparser
import pdb

config = configparser.RawConfigParser()
config.read("/Users/manish/PycharmProjects/pytest_01/Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def get_application_url():
        url = config.get('test', 'baseURL')
        return url

    @staticmethod
    def get_user_email():
        username = config.get("test","username")
        return username

    @staticmethod
    def get_user_pwd():
        pwd = config.get("test","pwd")
        return pwd

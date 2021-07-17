#To read data from config.ini
import configparser
import pdb

config = configparser.RawConfigParser()
config.read("/Users/manish/PycharmProjects/pytest_01/Configurations/config.ini")

#
# print("=================")

config.sections()


print("section", config.sections())

print("flight_ctr section", config['flight_ctr']['baseUrl'])

print(config.get('flight_ctr','browserName'))

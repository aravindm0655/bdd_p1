import configparser

def getconfig():
    config=configparser.ConfigParser()
    config.read("C:/Users/aravi/PycharmProjects/pythonProject1/Utilities/properties.ini")
    url = config['URL']['url']
    return url
import configparser

def getconfiguration():
    config= configparser.ConfigParser()
    config.read('C:\\Users\\Punam\\workspace_python\\api\\utilities\\properties.ini')
    return config
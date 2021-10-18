import configparser

def getconfig():
    config=configparser.ConfigParser()
    config.read('C:\\Users\\Punam\\workspace_python\\api\\apiauth\\utilitiesk\\property.ini')
    return config

def getpwd():
    pwd = 'op'
    return pwd
import configparser
import mysql.connector
from mysql.connector import Error

def getconfig():
    config= configparser.ConfigParser()
    config.read("C:\\Users\\Punam\\workspace_python\\api\\DBCoonection\\uti\\prop.ini")
    return config

conset={
    'host': getconfig()['SQL']['hostname'],
    'database': getconfig()['SQL']['database'],
    'user': getconfig()['SQL']['username'],
    'password': getconfig()['SQL']['password']
}



def getConnection():
    try:
        conn = mysql.connector.connect(**conset)
        if conn.is_connected():
            print("Connected")
            return conn
    except Error as e:
        print(e)

def getquery(query,data=''):
    conn = getConnection()
    cursor=conn.cursor()
    cursor.execute(query,data)
    conn.commit()
    conn.close()
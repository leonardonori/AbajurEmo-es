import mysql.connector

def getConnection():
    config = {
      'user': 'root',
      'password': '',
      'host': '127.0.0.1',
      'database': 'banco01',
      'charset':'utf8',
      'use_unicode': True,
      'raise_on_warnings': True,
    }
    connection = mysql.connector.connect(**config)
    return connection

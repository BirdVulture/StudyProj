#http://directprobi.ru/blogs/python-class-mysql-baza-dannyh-sql-select-insert-pymysql-cursor-execute-connection-commit/

#pip install mysql-connector-python
#used    pip3 install pymysql
#import mysql.connector
import pymysql


class StoreManagment:
    primaryKey = 0
    data = []

    def __init__(self, primaryKey, data):
        self.primeryKey = primaryKey
        self.data = data
    
    def search():
        pass
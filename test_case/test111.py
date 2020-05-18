import pymysql
from sshtunnel import SSHTunnelForwarder

class ExecuteSql(object):
    def __init__(self,dbname,sql):
        self.dbname = dbname
        self.sql = sql

    def excute_
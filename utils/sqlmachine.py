import pymysql
from utils import common

class machine:
    def __init__(self):
        _connect()
    
    def _connect(self):
        dbconfig = common.getConfig("databases")
        self.conn = pymysql.connect(
            host= dbconfig.host ,
            user= dbconfig.username ,
            password= dbconfig.password,
            port= dbconfig.port,
            database= dbconfig.database
        )
        self.cursor = conn.cursor(pymysql.cursors.DictCursor)
        self.status = "connecting"
        self.preStatus = True

    def reconnect(self):
        if self.status != "closed":
            logger.error("mysql reconnect fail, status is not closed")
        else
            self._connect

    def close(self):
        self.cursor.close()
        self.conn.close()
        self.status = "closed"

    def select(self,col, tb, other):
        sql = ""
        if other != "":
            sql = 'select ' + col + ' from ' + tb + " where " + other + ";"
        else:
            sql = 'select ' + col + ' from ' + tb + ";"
        try:
            self.cursor.execute(sql)
            result = cursor.fetchone()
            return result
        except Exception as e:
            conn.rollback()
            logger.error(e)
            self.preStatus = False
            return ""
    
import sqlite3

class ConexionSQLiteHelper:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)        

    def getConn(self):
        return self.conn

    def close_bd(self):
        self.conn.close()

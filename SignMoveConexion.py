from ConexionSQLiteHelper import *

class signMoveConexion:
    def __init__(self):
        self.conn = ConexionSQLiteHelper('A072.db')
        self.cursor = self.conn.getConn().cursor()

    def closeCursor(self):
        self.cursor.close()

    def consultaLSM(self, class_name):
        name = (class_name,)
        return self.cursor.execute("select id_lsm from lsm where name_lsm = ?", name)

    def insert(self, samples):
        for key in samples:
            values = samples.get(key)
            id = self.consultaLSM(key)
            for i in id:
                aux_id = i[0]
            values_insert = (aux_id,)
            self.cursor.execute("insert into sample(id_lsm) values(?)", values_insert)
            values_insert = ()
            for val in range(8):
                values_insert = values_insert + (values[val],)
            values_insert = values_insert + (aux_id,)
            self.cursor.execute("insert into sign values(?,?,?,?,?,?,?,?,?)", values_insert)
            values_insert = ()
            for val in range(8, 40):
                values_insert = values_insert + (values[val],)
            values_insert = values_insert + ('x',) + (aux_id,)
            self.cursor.execute("insert into move values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values_insert)
            values_insert = ()
            for val in range(40, 72):
                values_insert = values_insert + (values[val],)
            values_insert = values_insert + ('y',) + (aux_id,)
            self.cursor.execute("insert into move values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values_insert)
            values_insert = ()
            for val in range(72, 104):
                values_insert = values_insert + (values[val],)
            values_insert = values_insert + ('z',) + (aux_id,)
            self.cursor.execute("insert into move values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values_insert)
            self.conn.getConn().commit()

    def closeBD(self):
        self.closeCursor()
        self.conn.getConn().close()

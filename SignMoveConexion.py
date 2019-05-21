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

    def consultaIdeogram(self):
        return self.cursor.execute("select i.id_ideogram, l.name_lsm, i.id_sign, i.id_move from ideogram i, lsm l where l.id_lsm = i.id_lsm")

    def consultaSign(self):
        return self.cursor.execute("select s.id_sign, l.name_lsm, s.sd1, s.sd2, s.sd3, s.sd4, s.sd5, s.sd6, s.sd7, s.sd8 from sign s, lsm l where l.id_lsm = s.id_lsm")

    def consultaMove(self):
        return self.cursor.execute("select m.id_move, l.name_lsm, m.axis, m.seg1, m.seg2, m.seg3, m.seg4, m.seg5, m.seg6, m.seg7, m.seg8, m.seg9, m.seg10, m.seg11, m.seg12, m.seg13, m.seg14, m.seg15, m.seg16, m.seg17, m.seg18, m.seg19, m.seg20, m.seg21, m.seg22, m.seg23, m.seg24, m.seg25, m.seg26, m.seg27, m.seg28, m.seg29, m.seg30, m.seg31, m.seg32 from move m, lsm l where l.id_lsm = m.id_lsm")

    def insertSign(self, samples):
        aux_id = 0
        for sample in samples:
            id = self.consultaLSM(sample.getClass())
            for i in id:
                aux_id = i[0]
            values_insert = (aux_id,)
            for val in sample.getStandarDeviation():
                values_insert = values_insert + (val,)
            self.cursor.execute("insert into sign(id_lsm, sd1, sd2, sd3, sd4, sd5, sd6, sd7, sd8) values(?,?,?,?,?,?,?,?,?)", values_insert)
            self.conn.getConn().commit()

    def insertMove(self, samples):
        aux_id = 0
        for sample in samples:
            id = self.consultaLSM(sample.getClass())
            for i in id:
                aux_id = i[0]
            values_insert = ()
            values_insert = (aux_id,) + ('x',)
            for val in sample.getSegmentX():
                values_insert = values_insert + (val,)
            self.cursor.execute("insert into move(id_lsm, axis, seg1, seg2, seg3, seg4, seg5, seg6, seg7, seg8, seg9, seg10, seg11, seg12, seg13, seg14, seg15, seg16, seg17, seg18, seg19, seg20, seg21, seg22, seg23, seg24, seg25, seg26, seg27, seg28, seg29, seg30, seg31, seg32) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values_insert)
            values_insert = ()
            values_insert = (aux_id,) + ('y',)
            for val in sample.getSegmentY():
                values_insert = values_insert + (val,)
            self.cursor.execute("insert into move(id_lsm, axis, seg1, seg2, seg3, seg4, seg5, seg6, seg7, seg8, seg9, seg10, seg11, seg12, seg13, seg14, seg15, seg16, seg17, seg18, seg19, seg20, seg21, seg22, seg23, seg24, seg25, seg26, seg27, seg28, seg29, seg30, seg31, seg32) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values_insert)
            values_insert = ()
            values_insert = (aux_id,) + ('z',)
            for val in sample.getSegmentZ():
                values_insert = values_insert + (val,)
            self.cursor.execute("insert into move(id_lsm, axis, seg1, seg2, seg3, seg4, seg5, seg6, seg7, seg8, seg9, seg10, seg11, seg12, seg13, seg14, seg15, seg16, seg17, seg18, seg19, seg20, seg21, seg22, seg23, seg24, seg25, seg26, seg27, seg28, seg29, seg30, seg31, seg32) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", values_insert)
            self.conn.getConn().commit()

    def insertIdeogram(self, samples):
        for sample in samples:
            id = self.consultaLSM(sample[0])
            for i in id:
                aux_id = i[0]
            values_insert = ()
            values_insert = (aux_id,)
            for val in sample[1:]:
                values_insert = values_insert + (val,)
            self.cursor.execute("insert into ideogram(id_lsm, id_sign, id_move) values(?,?,?)", values_insert)
            self.conn.getConn().commit()

    def closeBD(self):
        self.closeCursor()
        self.conn.getConn().close()

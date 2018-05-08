import pymysql


class DBHelper():
    def __init__(self, host='10.16.6.120', user='fanxing', passwd='kugou2014', db='d_fanxing', port=3306, **kw):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port

    def getCon(self):
        try:
            conn = pymysql.connect(self.host, self.user, self.passwd, self.db, self.port,
                                   charset='utf8')
            return conn
        except pymysql.Error as e:
            print("Mysqldb Error:%s" % e)

    def select(self, sql):
        print (sql)
        try:
            con = self.getCon()
            cur = con.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            fc = cur.fetchall()
            return fc
        except pymysql.Error as e:
            print("Mysqldb Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def insert(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except pymysql.Error as e:
            con.rollback()
            print("Mysqldb Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def updateByParam(self, sql, params):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql, params)
            con.commit()
            return count
        except pymysql.Error as e:
            con.rollback()
            print("Mysqldb Error:%s" % e)
        finally:
            cur.close()
            con.close()

    def update(self, sql):
        try:
            con = self.getCon()
            cur = con.cursor()
            count = cur.execute(sql)
            con.commit()
            return count
        except pymysql.Error as e:
            con.rollback()
            print ("Mysqldb Error:%s" % e)
        finally:
            cur.close()
            con.close()

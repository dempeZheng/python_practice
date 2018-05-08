import string
from db import DBHelper

db = DBHelper.DBHelper("10.16.6.120", "fanxing", "kugou2014", "d_fanxing")

def select(sql):
    return db.select(sql)


def insert(p_table_name, p_data):
    key = string.join(p_data.keys(), "`,`")
    values = [str(d) for d in p_data.values()]
    value = string.join(values, "','")
    real_sql = "INSERT INTO " + p_table_name + " (`" + key + "`) VALUES ('" + value + "')"
    print(real_sql)
    return db.insert(real_sql)


def insertBySql(sql):
    return db.insert(sql)

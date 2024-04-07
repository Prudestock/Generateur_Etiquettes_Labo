import db_handler

import sqlite3
import os

abspath = "/Users/joffrey/Documents/Codage/PycharmProjects/Generateur_Etiquettes_Labo/fds.db"

filename = os.path.normpath(
    os.path.dirname(
        os.path.abspath(__file__)) + "/../fds.db")
#filename = "~" + str(os.path.normpath(dirname))
#print(filename)
ENTRIES = []
db = sqlite3.connect(filename)
c = db.cursor()
sql = """select name from fds where name is not null"""
c.execute(sql)
for row in c:
    ENTRIES.append(row[0])



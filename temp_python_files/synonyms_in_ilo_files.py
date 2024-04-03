import csv
import re
import sqlite3
from db_handler import *
from colorlog import ColoredFormatter




db = "/Users/joffrey/Documents/Codage/PycharmProjects/EtiquettesLaboPyQt/fds.db"
connection = sqlite3.connect(db)
pattern = "^[0-9]{4}\s\s(.+)"
file = "/Users/joffrey/Documents/Codage/PycharmProjects/EtiquettesLaboPyQt/useless_csv/liste_fds.txt"
with open(file, "r") as source:
    lines = source.readlines()
    for i in range(0, len(lines)):
        if not re.match(pattern,lines[i]):
            produit = re.match(pattern, lines[i - 1]).group(1)
            synonyms = lines[i]
            synonyms = re.sub("\n","",synonyms)
            update_db(connection,produit=produit,column="synonyms",value=synonyms)



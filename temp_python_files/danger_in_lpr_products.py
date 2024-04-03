from colored_logger import log
import csv
import sqlite3
from db_handler import *

CONNECTION = sqlite3.connect("/Users/joffrey/Documents/Codage/PycharmProjects/EtiquettesLaboPyQt/fds.db")




file= "/useless_csv/produits_dangers_stocks.csv"
FIELDNAMES = ["name","attention","sante","inflammable","polluant",
              "corrosif","toxique","oxydant","explosif_instable","quantite"]

with open(file,"r") as f:
    reader = csv.DictReader(f,fieldnames=FIELDNAMES)
    for row in reader:
        #print(row['name'])
        if row['attention']:
            update_db(CONNECTION,row['name'],"attention","TRUE")
        if row['sante']:
            update_db(CONNECTION, row['name'], "sante", "TRUE")
        if row['inflammable']:
            update_db(CONNECTION, row['name'], "inflammable", "TRUE")
        if row['polluant']:
            update_db(CONNECTION, row['name'], "polluant", "TRUE")
        if row['corrosif']:
            update_db(CONNECTION, row['name'], "corrosif", "TRUE")
        if row['toxique']:
            update_db(CONNECTION, row['name'], "toxique", "TRUE")
        if row['oxydant']:
            update_db(CONNECTION, row['name'], "oxydant", "TRUE")
        if row['quantite']:
            update_db(CONNECTION, row['name'], "quantite", row['quantite'])


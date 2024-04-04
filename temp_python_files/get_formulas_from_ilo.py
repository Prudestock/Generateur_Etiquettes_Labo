import re
from selenium import webdriver
from db_handler import CONNECTION
import db_handler
import sqlite3
#url = "https://www.ilo.org/dyn/icsc/showcard.display?p_lang=fr&p_card_id=0126&p_version=2"
driver = webdriver.Chrome()


pattern_formule = "Formule: (.+)<br>" # Recherche de la formule
pattern_molar_mass = "Masse (moléculaire|atomique):\s(.+)" # Recherche de la masse molaire
db_access = sqlite3.connect("/Users/joffrey/Documents/Codage/PycharmProjects/Generateur_Etiquettes_Labo/fds.db")
c= db_access.cursor()
sql = 'SELECT name,long_url FROM fds WHERE long_url IS NOT NULL'
c.execute(sql)
d = c.fetchmany(5)
for row in c :
    driver.get(row[1])
    if re.search(pattern_formule,driver.page_source):
        formula = re.search(pattern_formule, driver.page_source).group(1)
        formula = re.sub("0", "\u2080", formula)
        formula = re.sub("1","\u2081",formula)
        formula = re.sub("2", "\u2082", formula)
        formula = re.sub("3", "\u2083", formula)
        formula = re.sub("4", "\u2084", formula)
        formula = re.sub("5", "\u2085", formula)
        formula = re.sub("6", "\u2086", formula)
        formula = re.sub("7", "\u2087", formula)
        formula = re.sub("8", "\u2088", formula)
        formula = re.sub("9", "\u2089", formula)
        formula = re.sub("(<sub>|<\/sub>)","",formula)
        print(f"FORMULE {row[0]}= {formula}")
        db_handler.update_db(produit = row[0],
                             column="formula",
                             value = formula,
                             db_connection=db_access)
    else :
        print("NO MATCH")
    if re.search(pattern_molar_mass, driver.page_source):
        molar_mass = re.search(pattern_molar_mass, driver.page_source).group(2)
        db_handler.update_db(produit=row[0],
                             column="molar_mass",
                             value= molar_mass,
                             db_connection=db_access)
        print(f"MASSE MOLECULAIRE = {re.search(pattern_molar_mass, driver.page_source).group(2)}")
    else:
        print("NO MATCH")

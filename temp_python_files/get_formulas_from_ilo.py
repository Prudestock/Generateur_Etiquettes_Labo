import re
from selenium import webdriver
from db_handler import CONNECTION
import db_handler
#url = "https://www.ilo.org/dyn/icsc/showcard.display?p_lang=fr&p_card_id=0126&p_version=2"
driver = webdriver.Chrome()


pattern_formule = "Formule: (.+)<br>" # Recherche de la formule
pattern_molar_mass = "Masse (moléculaire|atomique):\s(.+)" # Recherche de la masse molaire

c= CONNECTION.cursor()
sql = 'SELECT name,long_url FROM fds'
c.execute(sql)
d = c.fetchmany(5)
for row in c :
    driver.get(row[1])
    if re.search(pattern_formule,driver.page_source):
        formula = re.search(pattern_formule, driver.page_source).group(1)
        formula = re.sub("<sub>","",formula)
        formula = re.sub("</sub>","",formula)
        print(f"FORMULE {row[0]}= {formula}")
    else :
        print("NO MATCH")
    if re.search(pattern_molar_mass, driver.page_source):
        print(f"MASSE MOLECULAIRE = {re.search(pattern_molar_mass, driver.page_source).group(2)}")
    else:
        print("NO MATCH")

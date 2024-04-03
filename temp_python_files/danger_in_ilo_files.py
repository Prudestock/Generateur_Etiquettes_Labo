from selenium import webdriver
from db_handler import *

driver = webdriver.Chrome()
db = "/Users/joffrey/Documents/Codage/PycharmProjects/EtiquettesLaboPyQt/fds.db"
CONNECTION = sqlite3.connect(db)

attention = "/webcommon/dyn/images/icsc/ghs-pictograms/exclam.gif"
sante = "/webcommon/dyn/images/icsc/ghs-pictograms/silhouete.gif"
polluant = "/webcommon/dyn/images/icsc/ghs-pictograms/aquatic-pollut-red.gif"
corrosif = "/webcommon/dyn/images/icsc/ghs-pictograms/acid_red.gif"
toxic = "/webcommon/dyn/images/icsc/ghs-pictograms/skull.gif"
oxydant = "/webcommon/dyn/images/icsc/ghs-pictograms/rondflam.gif"
inflammable = "/webcommon/dyn/images/icsc/ghs-pictograms/flamme.gif"

RISKS = [attention, sante, polluant, corrosif, toxic, oxydant,inflammable]
RISK_COLS = ["attention","sante","polluant","corrosif","toxique","oxydant","inflammable"]


for num in range(200,1786):
    try :
        nom, url = read_db_from_number(number=num, param="long_url")
        driver.get(url)
        if driver.page_source is not None:
            source = driver.page_source
            if re.search(inflammable, source):
                update_db(produit=nom.upper(),column="inflammable",value="TRUE")


            '''for i in range(0,len(RISKS)):
                if re.search(RISKS[i], source):
                    print("MATCH? ->",RISK_COLS[i])
                    update_db(produit=nom.upper(),column=RISK_COLS[i],value="TRUE")'''
    except :
        pass

#example_url = "https://www.ilo.org/dyn/icsc/showcard.display?p_lang=fr&p_card_id=0067&p_version=2"


# print(driver.page_source)



'''

'''

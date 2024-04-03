import os

import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
import random
import time



driver = webdriver.Chrome()

url = "http://evene.lefigaro.fr/citations/theme/resultat-aboutissement-finalite.php"
driver.get(url)
time.sleep(4)
#cookies = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div/div[4]/div/button[1]")
#cookies2 = driver.find_element(By.CSS_SELECTOR,"body > div > div > div > div > div > div > div.sc-lbhJGD.fMKlmZ > div > button.sc-furwcr.jhwOCG.button.button--filled.button__acceptAll")
#cookies2.click()
#time.sleep(1)
#"<button class="sc-furwcr jhwOCG button button--filled button__acceptAll" aria-label="ACCEPTER ET CONTINUER la collecte de vos données">ACCEPTER ET CONTINUER</button>"
quotes = driver.find_elements(By.CLASS_NAME, "figsco__quote__text")
authors = driver.find_elements(By.CLASS_NAME, "figsco__fake__col-9")
with open("./Citations.txt","a+") as f :
    for i in range(0,len(quotes)):
        try :
            citation = quotes[i].text
            auteur = authors[i].text
            line = f"{citation} - {auteur}\n"
            print(line)
            f.writelines(line)
        except IndexError:
            pass
    #print(quotes.text)

"""i = random.randint(0,len(quotes)-1)
print(i)

print(quotes[i].text)
#authors.__getitem__(i).text"""

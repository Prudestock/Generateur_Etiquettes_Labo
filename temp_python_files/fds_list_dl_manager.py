from selenium import webdriver
from selenium.webdriver.common.by import By


def grab_list_of_fds_from_ilo():
    driver = webdriver.Chrome()  # Starts chrome
    url = "https://www.ilo.org/dyn/icsc/showcard.listcards3?p_lang=fr"  # Database link
    XPathTable = "/html/body/div[1]/main/div[2]/article/table"  # Grabs the table with FDS
    driver.get(url=url)  # Opens the url
    test = driver.find_element(By.XPATH, XPathTable)  # Selects the table
    with open("../useless_csv/liste_fds.txt", "w+") as f:
        f.write(test.text)
import wikipediaapi
from db_handler import *

wiki_wiki = wikipediaapi.Wikipedia('Test (hamster6287@gmail.com)', 'fr')


def print_sections(sections, level=0):
    for s in sections:
        print("%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:40]))
        print_sections(s.sections, level + 1)

c= CONNECTION.cursor()
c.execute('SELECT * FROM fds WHERE number>1092')
d = c.fetchmany(5)
for row in c :
    requete = row[1].capitalize()
    page_py = wiki_wiki.page(requete)
    if page_py.exists():
        log.info(f"{row[1]} -> PAGE WIKIPEDIA DISPO")
        update_db(row[1],"wiki_link",page_py.canonicalurl)

""" 
with open("available_wikipedia_pages.txt","w+") as f : 
    for row in c:
        requete = row[1].capitalize()
        page_py = wiki_wiki.page(requete)
        if page_py.exists():
            log.info(f"{row[1]} -> PAGE WIKIPEDIA DISPO")
            f.write(row[1])
            
        else :
            log.warning(f"{row[1]} -> PAGE WIKIPEDIA N'EXISTE PAS")
"""



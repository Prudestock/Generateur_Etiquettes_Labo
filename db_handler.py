import sqlite3
import re
from colored_logger import log
import os

cwd = os.getcwd()
log.debug(f"{cwd}")
db = cwd+"/fds.db"
CONNECTION = sqlite3.connect(db)


def insert_in_db(db_connection: sqlite3.Connection, column: str, value: str) -> None:
    """permet d'insérer une NOUVELLE valeur dans la table fds
        : param db_connection Connexion à la table SQL
        : param column colonne à mettre à jour
        : param value valeur à insérer"""
    try:
        db_connection.cursor().execute(f"""INSERT INTO fds ({column}) VALUES \"{value}\"""")
        log.info(f"REUSSITE - Insertion de {value} dans {column} réussie")
        db_connection.commit()
    except sqlite3.DataError or sqlite3.Error:
        log.info(f"ECHEC - Insertion de {value} dans {column} impossible dans la base fds")


def update_db(produit: str, column: str, value: str,db_connection=CONNECTION):
    """ Autorise la mise à jour d'une valeur dans la table
    :param db_connection Connexion à la table sql
    :param produit : produit à mettre à jour
    :param column colonne à mettre à jour
    :param value valeur à mettre à jour"""
    try:
        sql = f'''UPDATE fds SET {column} = \'{value}\' WHERE name = \'{produit}\';'''
        db_connection.cursor().execute(sql)
        log.info(f"REUSSITE - Mise à jour de {produit} : {column}={value}")
        db_connection.commit()
    except sqlite3.OperationalError:
        log.error(f"ECHEC OPERATIONAL ERROR- Mise à jour IMPOSSIBLE de {produit} : {column} = {value}")


def read_db(db_connection: sqlite3.Connection, produit: str) -> None:
    """Permet de lire toutes les valeurs pour une entrée donnée"""
    results = db_connection.cursor().execute(f"""SELECT * FROM fds WHERE name=\'{produit.upper()}\'""")
    result = results.fetchone()
    if result is None:
        log.info(f"Requete \"{produit.upper()}\" non trouvée")
    else:
        print(f"numéro = {result[0]} ")
        print(f"produit = {result[1]} ")
        print(f"synonymes = {result[2]}")
        print(f"URL longue = {result[3]} ")
        print(f"URL Raccourcie = {result[4]} ")
        print(f"PICTO_ATTENTION = {result[5]} ")
        print(f"PICTO_SANTE = {result[6]} ")
        print(f"PICTO_POLLUANT = {result[7]} ")
        print(f"PICTO_CORROSIF = {result[8]} ")
        print(f"PICTO_TOXIQUE = {result[9]} ")
        print(f"PICTO_OXYDANT = {result[10]} ")
        print(f"PICTO_OXYDANT = {result[11]} ")


def read_db_from_product(db_connection: sqlite3.Connection, produit: str, param: str) -> None:
    """Permet de lire toutes les valeurs pour une entrée donnée"""
    param = re.sub("[éè]", "e", param).lower()
    if param in ["number", "name", "synonyms", "long_url", "short_url",
                 "attention", "sante", "polluant", "corrosif", "toxique", "oxydant", "quantite"]:

        results = db_connection.cursor().execute(f"""SELECT {param} FROM fds WHERE name=\'{produit.upper()}\'""")
        result = results.fetchone()
        if result is None:
            log.info(f"Requete \"{produit.upper()}\" non trouvée")
        else:
            print(f"valeur de \"{param.upper()}\" pour produit = {result[0]} ")
    else:
        print(f"le paramètre (\"{param.upper()}\") demandé n'existe pas")


def read_db_from_number(number: int, param: str, db_connection=CONNECTION, ) -> str:
    """Permet de lire toutes les valeurs pour une entrée donnée"""
    param = re.sub("[éè]", "e", param)
    if param in ["number", "name", "synonyms", "long_url", "short_url",
                 "attention", "sante", "polluant", "corrosif", "toxique", "oxydant", "quantite"]:
        sql = f"""SELECT name , {param} FROM fds WHERE number = {number}"""
        results = db_connection.cursor().execute(sql)
        result = results.fetchone()
        if result is None:
            log.info(f"Requete \"{number}\" non trouvée")
        else:
            return result[0], result[1]
    else:
        log.info(f"le paramètre (\"{param.upper()}\") demandé n'existe pas")


def remove_duplicates_from_db(db_connection: sqlite3.Connection) -> None:
    db_connection.cursor().execute("DELETE FROM fds WHERE ROWID NOT IN"
                                   "(SELECT MIN(ROWID) FROM fds GROUP BY number);")
    db_connection.commit()


def get_length_of_db(db_connection: sqlite3.Connection) -> None:
    length = db_connection.cursor().execute("select * from fds").fetchall()
    log.info(f" LONGUEUR DE LA BASE fds : {len(length)}")



# connection.close()

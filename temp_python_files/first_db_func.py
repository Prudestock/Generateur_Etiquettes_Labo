import re
import sqlite3
import csv

def bulk_insert(liste_fds, db_connection: sqlite3.Connection) -> None:
    regex_pattern = "^([0-9]{4})[\s]{2}(.+)"  # Selects lines with ID + Name of the chemical
    with open(liste_fds, "r") as f:
        for line in f.readlines():
            if re.match(pattern=regex_pattern, string=line):
                request = """INSERT INTO fds (number,name) VALUES ({},\"{}\")""" \
                    .format(re.search(pattern=regex_pattern, string=line).group(1),
                            re.search(pattern=regex_pattern, string=line).group(2))
                # print("request = ",request)
                db_connection.cursor().execute(request)
                print("INSERTED -> ", request)
                db_connection.commit()

                # print(re.search(pattern=regex_pattern, string=line).group(1)) # Captures the number
                # print(re.search(pattern=regex_pattern, string=line).group(2)) # Captures the name
                # print(line, "TRUE")


def add_urls_from_csv(liste_fds, db_connection: sqlite3.Connection) -> None:
    regex_pattern = "^([0-9]{4})[\s]{2}(.+)"  # Selects lines with ID + Name of the chemical
    with open(liste_fds, "r") as f:
        for line in f.readlines():
            if re.match(pattern=regex_pattern, string=line):
                id = str(re.search(pattern=regex_pattern, string=line).group(1))
                fds_url_pattern = "https://www.ilo.org/dyn/icsc/showcard.display?" \
                                  "p_lang=fr&p_card_id={}&p_version=2".format(id)  # Pattern to directly access a FDS
                request = f"""UPDATE fds SET long_url="{fds_url_pattern}\" WHERE number={id}"""
                print("request = ", request)
                db_connection.cursor().execute(request)
                print("INSERTED -> ", request)
                db_connection.commit()


def add_short_urls_in_db_from_csv(csv_file, db_connection: sqlite3.Connection) -> None:
    """:param csv_file : csv file with headers (long_url,short_url) """
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f, fieldnames=["long_url", "short_url"], delimiter=";")
        for row in reader:
            print(row)
            short_url = row["short_url"]
            long_url = row["long_url"]
            print(short_url, long_url)
            request = f"UPDATE fds SET short_url=\"{short_url}\" WHERE long_url=\"{long_url}\""
            print(request)
            db_connection.cursor().execute(request)
            db_connection.commit()

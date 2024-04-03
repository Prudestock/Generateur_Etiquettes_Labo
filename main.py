import csv
import sqlite3



# Create a database
connection = sqlite3.connect("fds.db")
cursor = connection.cursor()
#cursor.execute("CREATE TABLE IF NOT EXISTS fds (number int, name varchar(255), synonyms varchar(255))")




connection.close()

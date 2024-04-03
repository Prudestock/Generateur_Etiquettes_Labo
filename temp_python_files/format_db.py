import csv
import re

with open("../useless_csv/liste_fds_lpr_temp.csv", "r") as source:
    with open("../useless_csv/liste_fds_lpr_FORMATTED.csv", "w+") as dest:
        reader = csv.DictReader(source,fieldnames=["produit","short_url"],delimiter=",")
        writer = csv.DictWriter(dest,fieldnames=["produit","short_url"],delimiter=";")
        for row in reader :
            writer.writerow({"produit":row["produit"].upper(),"short_url":row["short_url"]})

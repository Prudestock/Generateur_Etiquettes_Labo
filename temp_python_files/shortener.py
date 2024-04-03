import pyshorteners
from pyshorteners import Shortener
import csv

s = Shortener()
id = ""


def shorten(url: str, provider:str="osbd")-> str:
    """:returns a shortened url"""
    # dagd works
    # isgd works
    # osdb works
    if provider.lower()=="osbd":
        return s.osdb.short(url=url)
    elif provider.lower() =="dagd":
        return s.dagd.short(url=url)
    elif provider.lower() =="isgd":
        return s.isgd.short(url=url)
    else :
        print("choisissez un provider parmi : osbd,dagd,isgd")


FIELDNAMES = ["long_url","short_url"]
with open("../useless_csv/short_url.csv", "a") as csv_file :
    writer = csv.writer(csv_file)
    for i in range(141,180):
        id = str(i).zfill(4)
        long_url = f"https://www.ilo.org/dyn/icsc/showcard.display?p_lang=fr&p_card_id={id}&p_version=2"
        short_url = shorten(long_url,provider="dagd")
        writer.writerow([long_url,short_url])





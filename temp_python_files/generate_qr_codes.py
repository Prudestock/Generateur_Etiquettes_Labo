import segno
import os
import db_handler
from db_handler import CONNECTION
import re
def create_qr(url:str):
    return segno.make_qr(url)

def save_qr(qr_code:segno.QRCode, name:str):
    cwd = os.path.dirname(os.getcwd())
    name = re.sub("\s","_",name)
    name= "QR_"+name+".png"
    save_path = os.path.join(cwd+"/Assets/QR_Codes")
    test_path = os.path.join(save_path,name)
    print(test_path)
    try :
        qr_code.save(test_path,scale=20)
    except :
        pass

def generate_all_qr():
    c= CONNECTION.cursor()
    sql = "SELECT name,short_url FROM fds WHERE short_url IS NOT ''"""
    c.execute(sql)
    for row in c :
        qr=create_qr(url=row[1])
        save_qr(qr,row[0])



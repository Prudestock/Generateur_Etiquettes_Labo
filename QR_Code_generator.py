import segno
import os



def create_qr(url:str):
    return segno.make_qr(url)

def save_qr(name:str):
    cwd = os.path.dirname(os.getcwd())
    print(cwd)
    save_path = os.path.join(cwd+"/Assets/QR_Codes")
    test_path = os.path.join(save_path,name)
    print(type(test_path))

save_qr("test")
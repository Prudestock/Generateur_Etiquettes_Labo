from models.home import HomeModel
from models.stock import StockModel
from models.label import LblModel

class Model:
    def __init__(self):
        self.home = HomeModel()
        self.stock = StockModel()
        self.label = LblModel()
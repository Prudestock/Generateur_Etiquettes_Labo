from models.home import HomeModel
from models.stock import StockModel
from models.label import LblModel
from models.printer import PrinterModel

class Model:
    def __init__(self):
        self.home = HomeModel()
        self.stock = StockModel()
        self.label = LblModel()
        self.printer = PrinterModel()
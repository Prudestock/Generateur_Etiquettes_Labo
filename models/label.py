from models.base import ObservableModel
from colored_logger import log

class LblModel(ObservableModel):
    def __init__(self):
        super().__init__()
        self.product_filled = False
        self.conc_filled = False

    def update_product(self, status:bool):
        if status :
            self.product_filled = True
        else :
            self.product_filled = False
        self.trigger_event("product_filled")

    def update_conc(self,status:bool):
        log.debug(f"valeur de self.conc_filled = {self.conc_filled}")
        if status:
            self.conc_filled = True
        else :
            self.conc_filled = False
        self.trigger_event("conc_filled")
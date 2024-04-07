import random
from models.quote_picker import get_quote

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self):
        self.frame.quote_btn.config(command=self.quoting)
        self.frame.generate_btn.config(command = self.switch_to_labelgen)
        self.frame.get_info_btn.config(command=self.click)
        self.frame.calc_btn.config(command=self.click)

    def quoting(self):
        quote = get_quote("./Assets/Files/Citations.txt")
        self.frame.quote.set(value=quote)
        self.frame.quote_btn.config(textvariable = self.frame.quote)

    def click(self):
        print("CLICKED!")

    def switch_to_labelgen(self):
        self.view.switch("label")

    def switch_to_stock(self):
        self.view.switch("stock")



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

    def quoting(self):
        quote = get_quote("./Assets/Files/Citations.txt")
        self.frame.quote.set(value=quote)
        self.frame.quote_btn.config(textvariable = self.frame.quote)



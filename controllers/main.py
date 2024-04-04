from models.main import Model
from views.main import View
from .home import HomeController
from .label import LabelController


class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.label_controller = LabelController(model,view)



    def start(self):
        self.view.switch("label") # label
        self.view.start_mainloop()
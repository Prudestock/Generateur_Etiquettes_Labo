from models.main import Model
from views.main import View
from .home import HomeController
from .label import LabelController
from tkinter import NORMAL, DISABLED
from colored_logger import log


class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.label_controller = LabelController(model, view)
        self.model.label.add_event_listener("product_filled", self.validate)
        self.model.label.add_event_listener("conc_filled", self.validate)

    def validate(self, entries):
        if entries.product_filled and entries.conc_filled:
            self.label_controller.frame.generate_btn.config(state=NORMAL)
            self.label_controller.frame.preview_btn.config(state=NORMAL)
            self.label_controller.frame.goto_btn.config(state=NORMAL)
        else :
            self.label_controller.frame.generate_btn.config(state=DISABLED)
            self.label_controller.frame.preview_btn.config(state=DISABLED)
            self.label_controller.frame.goto_btn.config(state=DISABLED)

    def start(self):
        self.view.switch("home")  # label
        self.view.start_mainloop()

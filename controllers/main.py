from models.main import Model
from views.main import View
from .home import HomeController
from .label import LabelController
from .printer import PrinterController
from tkinter import NORMAL, DISABLED
from colored_logger import log


class Controller:
    def __init__(self, model: Model, view: View):
        self.view = view
        self.model = model
        self.home_controller = HomeController(model, view)
        self.label_controller = LabelController(model, view)
        self.printer_controller = PrinterController(model, view)
        self.model.label.add_event_listener("product_filled", self.validate)
        self.model.label.add_event_listener("conc_filled", self.validate)
        self.model.label.add_event_listener("label_generated", self.create_label)
        self.model.printer.add_event_listener("new_selection", self.update_selection)

    def validate(self, entries):
        if entries.product_filled and entries.conc_filled:
            self.label_controller.frame.generate_btn.config(state=NORMAL)
            self.label_controller.frame.preview_btn.config(state=NORMAL)
            self.label_controller.frame.goto_btn.config(state=NORMAL)
        else :
            self.label_controller.frame.generate_btn.config(state=DISABLED)
            self.label_controller.frame.preview_btn.config(state=DISABLED)
            self.label_controller.frame.goto_btn.config(state=DISABLED)

    def create_label(self, now:bool):
        if now :
            log.debug("CONTROLLER -> methode create_label appelée")
            self.printer_controller.show_labels()
        else :
            pass

    def update_selection(self):
        self.model.printer.get_all_selected_labels()

    def start(self):
        self.view.switch("home")  # label
        self.view.start_mainloop()

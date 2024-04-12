from colored_logger import log
from tkinter_special_classes.AvailableFrames import LabelSummary


class PrinterController():
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["print"]
        self._bind()
        #self.show_labels()


    def show_labels(self):
        log.debug("methode 'show_labels' appelée")
        assert type(self.model.label.lbl_list[-1]) is tuple
        #master -> self.view.frames["print"].bottom_frame
        self.etiquette = LabelSummary(self.frame.bottom_frame,
                                      self.model.label.lbl_list[-1][0],
                                      self.model.label.lbl_list[-1][1],
                                      self.model.label.lbl_list[-1][2])
        self.etiquette.frame.config(highlightbackground="black")
        assert self.etiquette.winfo_exists() == True
        self.etiquette.show()
        self.frame.bottom_frame.update_idletasks()

    def update_selection(self):
        pass

    def _bind(self):
        self.frame.print_btn.config(self.model.printer.print)

from models.entries_in_db import ENTRIES
from models.img_generator import generate_sticker
from tkinter import DISABLED, NORMAL
from colored_logger import log


class LabelController:

    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["label"]
        self._bind()

    def _bind(self):
        self.frame.entry_prod.entry.config(bg="white")
        self.frame.entry_prod.entry.bind("<FocusOut>", self.focus)
        self.frame.entry_prod.build(ENTRIES, case_sensitive=False)
        self.frame.entry_conc.bind("<FocusOut>", self.focus)
        self.frame.entry_prod.grid()
        self.frame.preview_btn.config(command=self.generate, state=DISABLED)
        self.frame.generate_btn.config(command=self.clicked, state=DISABLED)
        self.frame.goto_btn.config(command=self.clicked, state=DISABLED)

    def generate(self):
        prod = self.frame.entry_prod.entry.get()
        generate_sticker(produit=prod.upper(),
                         concentration=self.frame.entry_conc.get())


    def clicked(self):
        print("clicked!")


    def focus(self, event):
        if str(event.widget) == ".!labelview.!frame.!entry":
            if self.frame.entry_prod.entry.get() != "":
                if self.frame.entry_prod.entry.get().upper() in ENTRIES:
                    self.frame.entry_prod.entry.config(fg="blue")
                    self.model.label.update_product(status=True)
                else:
                    self.frame.entry_prod.entry.config(fg="red")
                    self.model.label.update_product(status=False)
            else:
                self.model.label.update_product(status=False)


        elif str(event.widget) == ".!labelview.!entry":
            log.debug(f'widget ENTRY_CONC a perdu le focus')
            if self.frame.entry_conc.get() != "":
                # self.model.label.conc_filled=True
                self.model.label.update_conc(status=True)
            else:
                # self.model.label.conc_filled = False
                self.model.label.update_conc(status=False)

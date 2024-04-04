from tkinter import Frame, Label, Entry, Button
from tkinter_special_classes.autocomplete import AutocompleteEntry


class LabelView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(0,5):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        # Preparation of autocompletion widgets
        self.inner_frame1 = Frame(self)
        self.entry_prod = AutocompleteEntry(self.inner_frame1)
        self.inner_frame2 = Frame(self)
        self.entry_prod2 = AutocompleteEntry(self.inner_frame2)

        # Chemical to label :
        self.lbl_prod = Label(self,
                              text="Produit à étiqueter : ",
                              justify="right",
                              pady=10)
        # Label for a concentration
        self.lbl_conc = Label(self,
                              text="Concentration : ",
                              justify="right",
                              pady=10)

        # Value of concentration
        self.entry_conc = Entry(self,
                                width=25,
                                borderwidth=1)

        self.generate_btn = Button(self,
                                   text="GENERER L'ETIQUETTE",
                                   highlightbackground="black",
                                   bg="blue",
                                   fg="blue",
                                   activeforeground="blue")

        # Positioning widgets
        self.lbl_prod.grid(column=0, row=0, sticky="e", pady=5)
        self.lbl_conc.grid(column=0, row=1, sticky="e", pady=5)
        self.entry_prod.grid(column=0, row=0, sticky="w", pady=5)
        self.inner_frame1.grid(column=1, row=0, sticky="w", pady=5)
        self.entry_conc.grid(column=1, row=1, sticky="w")
        self.generate_btn.grid(column=0,columnspan=5,row=3,sticky="nswe",rowspan=2)

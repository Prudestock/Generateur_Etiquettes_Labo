from tkinter import Frame, Label, Entry, Button
from tkinter_special_classes.autocomplete import AutocompleteEntry


class LabelView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(0, 5):
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

        self.preview_btn = Button(self,
                                  text="Aperçu de l'étiquette",
                                  bg="blue",
                                  fg="blue",
                                  activeforeground="blue",
                                  padx=5, pady=5)

        self.generate_btn = Button(self,
                                   text="Générer une étiquette",
                                   bg="blue",
                                   fg="blue",
                                   activeforeground="blue",
                                   padx=5, pady=5)

        self.goto_btn = Button(self,
                               text="Passer à l'impression PDF",
                               bg="blue",
                               fg="blue",
                               activeforeground="blue",
                               padx=5, pady=5)

        # Positioning widgets
        self.lbl_prod.grid(column=0, row=0, sticky="e", pady=5)
        self.lbl_conc.grid(column=0, row=1, sticky="e", pady=5)
        self.entry_prod.grid(column=0, row=0, sticky="w", pady=5)
        self.inner_frame1.grid(column=1, row=0, sticky="w", pady=5)
        self.entry_conc.grid(column=1, row=1, sticky="w")
        self.preview_btn.grid(column=0, row=3, sticky="nswe", )
        self.generate_btn.grid(column=1, columnspan=4, row=3, sticky="nswe")
        self.goto_btn.grid(column=0, columnspan=5, row=4, sticky="nswe")

from tkinter import Frame, Label, Button, StringVar


class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.quote = StringVar(self)
        self.quote.set(value="Coucou les loulous!")
        self.hello = Label(self,
                           text="Bonjour!\nQue voulez-vous faire aujourd'hui?",
                           justify="center", pady=50)

        self.generate_btn = Button(self,
                                   text="Générer des étiquettes",
                                   height=3)
        self.get_info_btn = Button(self,
                                   text="Obtenir des informations sur un produit de la base",
                                   height=3)
        self.calc_btn = Button(self,
                               text="calculer",
                               height=3)

        self.quote_btn = Button(self,
                                textvariable=self.quote,
                                justify="center",
                                foreground="grey",
                                background="grey",
                                borderwidth=0,
                                border=0,
                                wraplength=425)

        self.hello.grid(column=0, row=0, sticky="we")
        self.generate_btn.grid(column=0, row=1, sticky="we", padx=25)
        self.get_info_btn.grid(column=0, row=2, sticky="we", padx=25)
        self.calc_btn.grid(column=0, row=3, sticky="we", padx=25)
        self.quote_btn.grid(column=0, row=4, sticky="we", pady=10)

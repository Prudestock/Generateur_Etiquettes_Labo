from tkinter import Tk
from tkinter import messagebox
from tkinter import Menu


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.create_menu_bar()
        start_width = 500
        min_width = 400
        start_height = 400
        min_height = 400

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("Gestionnaire Labo")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def create_menu_bar(self):
        menu_bar = Menu(self)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="Génerer des étiquettes", command=self.do_something)
        menu_file.add_command(label="Obtenir des informations", command=self.do_something)
        menu_file.add_command(label="Calculer", command=self.do_something)
        # menu_file.add_separator()
        # menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Actions", menu=menu_file)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="A propos", command=self.do_about)
        menu_bar.add_cascade(label="Aide", menu=menu_help)

        menu_quit = Menu(menu_bar, tearoff=0)
        menu_quit.add_command(label="QUITTER", command=self.quit)
        menu_bar.add_cascade(label="Quitter", menu=menu_quit)

        self.config(menu=menu_bar)

    def do_something(self):
        print("Menu clicked")

    def do_about(self):
        messagebox.showinfo("My title", "My message")

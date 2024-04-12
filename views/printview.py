from tkinter import Frame, Label, Button, StringVar,Radiobutton
from tkinter_special_classes import AvailableFrames

class PrintView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in range(0,3):
            self.grid_columnconfigure(i,weight=1)

        self.welcome = Label(self,text = "ETAPE1 : choisissez le format\nETAPE2 : Choisissez les étiquettes à imprimer")
        self.small_size = Radiobutton(self,text="PETITE TAILLE") #FIXME : Make only one clickable radiobutton
        self.big_size = Radiobutton(self, text="GRAND TAILLE")#FIXME : Make only one clickable radiobutton
        self.print_btn = Button(self, text="Imprimer!")
        self.bottom_frame = Frame(self, highlightbackground="black", borderwidth=2,bg="red", width=500, height=70)
        self.extra = Label(self, bg="green")

        # Grids
        self.welcome.grid(row=0,column=0,columnspan=2)
        self.small_size.grid(row=1, column=0)
        self.big_size.grid(row=1, column=1)
        self.bottom_frame.grid(row=3, column=0,columnspan=2)





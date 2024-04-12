from tkinter import Frame, Checkbutton, Entry, Label, StringVar, BooleanVar
from PIL import ImageTk, Image
from colored_logger import log


class LabelSummary(Frame, Entry, Checkbutton):

    count = -1

    def __init__(self, master, product, concentration, image):
        super().__init__()

        LabelSummary.count += 1  # Incrementing count
        self.id = LabelSummary.count  # Implementing a basic ID for retrieval
        self.frame = Frame(master,
                           highlightbackground="black",
                           highlightthickness=2,
                           bg="white",
                           width=500,
                           height=300)  # Will be the frame which accepts all widgets

        # setting up grid
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=3)

        # Settingup checkbox w/ an empty var :
        self.onoff = BooleanVar()
        self.selected = False

        # Importing products
        self.product = product
        self.concentration = concentration
        self.check = Checkbutton(self.frame,
                                 variable=self.onoff,
                                 command=self.bg,
                                 bg="white")

        self._create_labels()
        self._import_image(image=image)
        self.check.grid(column=0, rowspan=2, row=0)

    def _create_labels(self):
        self.txt_product = StringVar()  # Initiates a StringVar()
        self.txt1 = f"Produit: {self.product.upper()}"
        self.txt_product.set(self.txt1)  # Setting text
        self.txt_conc = StringVar()
        self.txt2 = f"Concentration: {self.concentration}"
        self.txt_conc.set(self.txt2)

        # Creating labels
        self.lbl_product = Label(self.frame,
                                 width=25,
                                 bg="white",
                                 textvariable=self.txt_product,
                                 justify="left")
        self.lbl_conc = Label(self.frame,
                              width=25,
                              bg="white",
                              textvariable=self.txt_conc,
                              justify="left")

        # Grid
        self.lbl_product.grid(column=1, row=0)
        self.lbl_conc.grid(column=1, row=1)

    def _import_image(self, image):
        # Resize for acceptable sizing
        image = image.resize((140, 90), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(image)  # Conversion for Tk
        self.im_lbl = Label(self.frame, image=self.image)

        # Grid
        self.im_lbl.grid(column=2, row=0, rowspan=2)

    def _bind(self):
        self.frame.bind("<Button-1>", self.bg)
        self.frame.bind("<Double-Button-1>", self.w_bg)

    def bg(self):
        if self.onoff.get():
            log.info("y_bg called")
            self.frame.config(background="yellow")
            self.lbl_product.config(bg="yellow")
            self.lbl_conc.config(bg="yellow")

            self.selected = True
            log.info(f"widget {self.id} -> SELECTION : {self.selected}")
        elif not self.onoff.get():
            log.info("w_bg called")
            self.frame.config(bg="white")
            self.lbl_product.config(bg="white")
            self.lbl_conc.config(bg="white")
            self.selected = False
            log.info(f"widget {self.id} -> SELECTION : {self.selected}")

    def w_bg(self):
        self.frame.config(background="yellow")
        self.lbl_product.config(background="yellow")
        self.lbl_conc.config(background="yellow")

    def show(self):
        self.frame.grid()

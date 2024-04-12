from .root import Root
from .home import HomeView
from .printview import PrintView
from .labelgenerator import LabelView


class View:
    def __init__(self):
        self.root = Root()
        self.frames = {}
        self._add_frame(HomeView, "home")
        self._add_frame(LabelView, "label")
        self._add_frame(PrintView,"print")

    def _add_frame(self, Frame, name):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name:str):
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self):
        self.root.mainloop()
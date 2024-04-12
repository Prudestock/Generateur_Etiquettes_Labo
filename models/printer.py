from models.base import ObservableModel
import platform
import os
from subprocess import Popen, PIPE
from colored_logger import log
import pprint
from tkinter import *


# "lpstat -a" prints info on printers that can accept print requests

p = Popen(['lpstat', '-a'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
output, _ = p.communicate() # readable
output = output.decode("utf-8").split("\n") # Conversion bytes -> string
PRINTER_LIST = [x.split()[0] for x in output if x != ""]
log.info(f'Liste des imprimantes disponibles : {", ".join(PRINTER_LIST)}')


#print(cwd)
FILENAME = "Etiquettes.pdf"
FILENAME_PATH = os.path.normpath(os.getcwd() + "/../" + FILENAME)




class PrinterModel(ObservableModel):
    def __init__(self):
        super().__init__()

    def print(self, filename=FILENAME_PATH):
        '''
            -P destination[/instance]
            Prints files to the named printer.
            -# copies
            Sets the number of copies to print.


           -o option[=value]
            Sets a job option.

              -r   Specifies that the named print files should be deleted after
            submitting them.




        :return: None
        '''
        raw = ""
        if platform == "Windows":
            # TODO : generate a temp file to print
            pass
            # os.startfile("C:/Users/TestFile.txt", "print")

        if platform == "Darwin":
            printer = PRINTER_LIST[0]
            number_of_copies = 1
            delete: bool = True
            if delete:
                raw = f"lpr -P {printer} -# {number_of_copies} -o print-quality=4 -r {filename}"
            else:
                raw = f"lpr -P {printer} -# {number_of_copies} -o print-quality=4 {filename}"

        # ARGUMENTS :
        # -P destination[/instance] Prints files to the named printer.
        # -# copies
        # -o print-quality=4  # NORMAL
        #  -r   Specifies that the named print files should be deleted after submitting them.
        os.system(raw)

    def get_all_selected_labels(self):
        """ gets the whole list of all widgets that have been selected by the user"""
        log.debug("APPEL 'get_all_children()'")
        WIDGET_CLASSNAME = 'LabelSummary'
        toplevel = self.winfo_toplevel()  # Get top-level window containing self.
        # Use a list comprehension to filter result.
        selection = [child for child in get_all_children(toplevel)
                     if child.winfo_class() == WIDGET_CLASSNAME and child.selected == True]
        pprint(selection)

    def create_pdf(self):
        self.get_all_selected_labels()
        images = []

        images[0].save(
            FILENAME_PATH, "PDF", resolution=100.0, save_all=True, append_images=images[1:])

def get_all_children(widget):
    """ Return a list of all the children, if any, of a given widget.  """
    result = []  # Initialize.
    return _all_children(widget.winfo_children(), result)


def _all_children(children, result):
    """ Recursively append all children of a list of widgets to result. """
    for child in children:
        result.append(child)
        subchildren = child.winfo_children()
        if subchildren:
            _all_children(subchildren, result)

    return result
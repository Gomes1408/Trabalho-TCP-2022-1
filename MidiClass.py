from tkinter import *
from tkinter import filedialog
import MainWindow as MW
class Midi(MW):
    def __init__(self, text: str, corresponding_Text):
        self.text = text
        self.corresponding_MIDI = corresponding_Text

    def get_midi_from_file(self):
        file = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("MIDI files", "*.mid*"), ("all files", "*.*")))

        
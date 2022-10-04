from tkinter import Frame, Button
from utils import PLAY, STOP

class MidiPlayer(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.mediaControlFrame = Frame(self)
        
        self.buildButton = Button(self.mediaControlFrame, 
            text="Montar", 
            font="Calibri, 15", 
            command=None)
        self.resumeButton = Button(self.mediaControlFrame, 
            text="   " + PLAY + "   ", 
            font="Calibri, 15", 
            command=None)
        self.stopButton = Button(self.mediaControlFrame, 
            text="   " + STOP + "   ", 
            font="Calibri, 15", 
            command=None)
    def packWidgets(self):
        self.mediaControlFrame.pack()
        self.buildButton.pack(side="left")
        self.resumeButton.pack(side="left")
        self.stopButton.pack(side="left")
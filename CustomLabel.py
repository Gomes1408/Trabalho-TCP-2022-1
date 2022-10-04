from tkinter import Label, Frame
from ToolTip import ToolTip

class CustomLabel(Frame):
    """Implementação modificada do widget Label para exibir topicos com a chave e descriçao com cores diferentes"""
    def __init__(self, title, instructionSet, elementsPerLine=4, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        self.titleLabel = Label(self, text=title)
        self.instructionLabels = []
        self.instructionToolTips = []
        self.frameList = []
        lineCounter = 4
        for index, instruction in enumerate(instructionSet["instruction"]):
            if(lineCounter >= elementsPerLine):
                self.frameList.append(Frame(self))
                lineCounter = 0
            self.instructionLabels.append(Label(master=self.frameList[-1], text="[" + instruction + "]", fg="gray"))
            self.instructionToolTips.append(ToolTip(widget=self.instructionLabels[-1], text=instructionSet["description"][index]))
            lineCounter += 1
    def packWidgets(self):
        """Insere os widgets do editor de texto usando o gerenciador pack"""
        self.titleLabel.pack(side="top", fill="y")
        for widget in self.instructionLabels:
            widget.pack(side="left", fill="x", padx=5, pady=5, expand=True)
        for frame in self.frameList:
            frame.pack(side="top", fill="x", expand=True)
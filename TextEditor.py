from tkinter import Frame, Label, Text, Scrollbar
from CustomText import CustomText
from LineNumbers import LineNumbers
from ToolTip import ToolTip

class TextEditor(Frame):
    """ Pacote de widgets para edição de texto
        Pode conter, dependendo da especificação:
        -Label (titulo)
        -LineNumber (numero de linhas)
        -ScrollBar
        -Tool tip"""
    def __init__(self, 
        hasLabel=True, labelText="", 
        hasToolTip=True, toolTipText="", 
        hasScrollBar=True,
        hasLineNumbers=True,
        hasSubTitle=True, subtitleText="",
        editable=True,
        minHeight=5, minWidth=25,
        initialText="", *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        
        # variaveis de controle dos widgets
        self.hasLabel=hasLabel 
        self.hasToolTip=hasToolTip 
        self.hasScrollBar=hasScrollBar
        self.hasLineNumbers=hasLineNumbers
        self.hasSubTitle=hasSubTitle
        self.editable=editable
        if(self.hasSubTitle):
            self.statusLabel = Label(self, text=subtitleText, anchor="w")
        
        if(self.hasLabel):
            self.inputTextLabel = Label(self, text=labelText, anchor="w")
            if(self.hasToolTip):
                self.inputTextToolTip = ToolTip(self.inputTextLabel, text=toolTipText)
        
        # corpo do widget de texto principal
        self.inputText = CustomText(self, height=minHeight, width=minWidth)
        self.inputText.insert("end", initialText)
        if(not self.editable):
            self.inputText.configure(state="disabled")  # desabilita ediçoes
        
        if(self.hasLineNumbers):
            self.inputTextLineNumbers = LineNumbers(self, self.inputText, width=2, height=5)
            self.inputTextLineNumbers.on_key_release()
        
        if(self.hasScrollBar):
            self.inputTextScrollBar = Scrollbar(self, command=self.inputText.yview)
            self.inputText.configure(yscrollcommand=self.inputTextScrollBar.set)
    
    def insertText(self, text, cursor):
        """Insere dado texto na posição apontada pelo cursor, pode ser '1.0' para inicio, uma posição especifica
        ou 'end' para inserir no final do widget"""
        self.inputText.insert(cursor, text)
    def deleteText(self):
        """Remove todo o texto do widget texto principal""" 
        self.inputText.delete("1.0", "end")
    def getText(self, start="1.0", end="end-1c"):
        """Recupera o conteudo do widget Text a partir do intervalo especificado"""
        return self.inputText.get(start, end)
    def packWidgets(self, padx=5, pady=5, borderwidth=1):
        """Insere os widgets do editor de texto usando o gerenciador pack"""
        self.pack(side="top", fill="both", expand=True, padx=5, pady=5)  # frame principal
        
        if(self.hasSubTitle):
            self.statusLabel.pack(side="bottom", fill="x")
        
        if(self.hasLabel):
            self.inputTextLabel.pack(side="top", fill="y")
        
        if(self.hasLineNumbers):
            self.inputTextLineNumbers.pack(side="left", fill="y", expand=False)
        
        if(self.hasScrollBar):
            self.inputTextScrollBar.pack(side="right", fill="both")
        
        self.inputText.pack(side="left", fill="both", expand=True)  # texto principal

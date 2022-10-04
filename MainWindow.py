from utils import resourcePath, listFromFile, pathExists, resourcePath
from tkinter import Tk, Frame, Text, Button, Scrollbar, Menu, Label
from tkinter import filedialog as fd
from tkinter.ttk import Separator
from TextEditor import TextEditor
from CustomText import CustomText
from LineNumbers import LineNumbers

class MainWindow(Tk):
    def __init__(
        self,
        width = 1200, # dimensão X inicial da janela
        height = 500, # dimensão Y inicial da janela
        xPlacement = 0,  # define o posicionamento inicial X da janela
        yPlacement = 0, # define o posicionamento inicial X da janela
        title = "Example window",  # titulo da janela
        resizable = True,  # redimensionamento XY
        frameDelta = 1,  # delay entre frames (ms)
        *args,
        **kwargs):
        print("Inicializando janela")
        Tk.__init__(self, *args, **kwargs)
        
        # protocolos da janela
        self.protocol('WM_DELETE_WINDOW', self.exit)  # sets closing protocol to be called when window X is pressed

        # atributos da janela
        self.wm_title(title)  # define o titulo inicial da janela
        self.wm_geometry(f"{width}x{height}+{xPlacement}+{yPlacement}")  # define a geometria da janela (tamanho e posicionamento)
        self.wm_resizable(resizable, resizable)  # define se a janela vai ser redimensionavel nos eixos XY

        # atributos de controle
        self.windowShouldClose = False  # variavel de controle para o fechamento da janela
        self.frameDelta = frameDelta
        self.frameSerial = 0

<<<<<<< HEAD:MainApp.py
        # arquivo texto principal
        self.textFile = None
        self.saved = True, False  # (valor, foi indicado no titulo da janela)
        self.exported = False, False  # (valor, foi indicado no titulo da janela)

        # gerenciamento de objetos (frames)
        self.editorFrame = Frame(self, relief="raised", borderwidth=1)
        self.editorFrame.pack(side="left", fill="both", pady=5, padx=5)
        
        self.mediaFrame = Frame(self, relief="raised", borderwidth=1)
        self.mediaFrame.pack(side="right", fill="both", expand=True, pady=5, padx=5)
=======
        # gerenciamento de objetos
        self.editorFrame = Frame(self, relief="raised", borderwidth=5, bg="purple")
        self.editorFrame.pack(side="left", fill="both")
        self.inputFrame = Frame(self.editorFrame, relief="raised", borderwidth=5, bg="red")
        self.inputFrame.pack(side="top", fill="both", expand=True, pady=5)
        self.consoleFrame = Frame(self.editorFrame, relief="raised", borderwidth=5, bg="green")
        self.consoleFrame.pack(side="bottom", fill="both")
        self.editFrame = Frame(self, relief="raised", borderwidth=5, bg="blue")
        self.editFrame.pack(side="right", fill="both", expand=True)
        self.syntaxFrame = Frame(self, relief="raised", borderwidth=5, bg="yellow")
        self.syntaxFrame.pack(side="right", fill="both", expand=True)
>>>>>>> 9a577036d8d40c9bea01ad05c371e56323b7b7e5:MainWindow.py

        # menus drop down
        self.menuBar = Menu(self)
        self.config(menu=self.menuBar)
        self.createFileMenu()
        self.createEditMenu()
        self.createMidiMenu()
        self.createHelpMenu()

<<<<<<< HEAD:MainApp.py
        # editor de texto principal
        self.inputEditor = TextEditor(labelText="Editor de texto",
            toolTipText="Texto que vai ser convertido para MIDI",
            hasSubTitle=False,
            initialText="aAbBcC",
            minWidth=25,
            minHeight=20,
            master=self.editorFrame, borderwidth=0)
        self.inputEditor.packWidgets()
        self.inputEditor.deleteText()
        print(f"Teste: '{self.inputEditor.getText()}'")
=======
        # colocar borda
>>>>>>> 9a577036d8d40c9bea01ad05c371e56323b7b7e5:MainWindow.py

        # editor de texto (input do usuário)
        self.inputTextLabel = Label(self.inputFrame, text="Editor de texto", anchor="w")
        self.inputTextLabel.pack(side="top", fill="both")
        self.inputText = CustomText(self.inputFrame, width=50)
        self.inputTextLineNumbers = LineNumbers(self.inputFrame, self.inputText, width=2)
        self.inputTextLineNumbers.pack(side="left", fill="both")
        self.inputText.pack(side="left", fill="both", expand=True)
        self.inputTextLineNumbers.on_key_release()
        self.inputTextScrollBar = Scrollbar(self.inputFrame, command=self.inputText.yview)
        self.inputTextScrollBar.pack(side="right", fill="both")
        self.inputText.configure(yscrollcommand=self.inputTextScrollBar.set)

<<<<<<< HEAD:MainApp.py
        # visualizador de sintaxe
        self.syntaxVisualizer = TextEditor(labelText="Visualizador de sintaxe",
            toolTipText="Visualizador de sintaxe passo a passo das instruções adicionadas no editor de texto",
            hasSubTitle=False,
            initialText="esse eh o visualizador de sintaxe",
            editable=False,
            minWidth=60,
            borderwidth=1,
            relief="raised",
            master=self)
        self.syntaxVisualizer.packWidgets(padx=5, pady=5, borderwidth=1)

        # media player
        instructionList = listFromFile(resourcePath("instructionSet.json"))
        self.instructionLabels = CustomLabel(instructionSet=instructionList, 
            title="Lista de instruções", 
            master=self.mediaFrame, 
            borderwidth=2,
            relief="groove")
        self.instructionLabels.packWidgets()
        self.instructionLabels.pack(side="bottom", fill="x", expand=True, padx=5, pady=5)
=======
>>>>>>> 9a577036d8d40c9bea01ad05c371e56323b7b7e5:MainWindow.py
        
        # console e label respectiva
        self.consoleLabel = Label(self.consoleFrame, text="Terminal - Status: OK", anchor="w")
        self.consoleLabel.pack(side="top", fill="x")
        self.consoleText = CustomText(self.consoleFrame, height=20)
        self.consoleText.pack(side="bottom", expand=True, fill="both")
        self.consoleText.insert("end", "esse é o console")

        self.closeWindowButton = Button(self.editFrame, text='Fechar', command=self.exit)
        self.closeWindowButton.pack(side="right", padx=5, pady=5)
        
        self.closeWindowButton = Button(self.editFrame, text='Salvar', command=None)
        self.closeWindowButton.pack(side="right", padx=0, pady=5)

        #self.update()
        self.eval('tk::PlaceWindow . center')
    # criacao de menus
    def createFileMenu(self):
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label="Novo", command=None)
        self.fileMenu.add_command(label="Abrir", command=self.askOpenFile)
        self.fileMenu.add_command(label="Salvar", command=None)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Fechar", command=self.exit)
        self.menuBar.add_cascade(label="Arquivo", menu=self.fileMenu)
    def createEditMenu(self):
        self.editMenu = Menu(self.menuBar, tearoff=False)
        self.editMenu.add_command(label="Copiar", command=None)
        self.editMenu.add_command(label="Recortar", command=None)
        self.editMenu.add_command(label="Colar", command=None)
        self.editMenu.add_command(label="Selecionar tudo", command=self.selectAll)
        self.menuBar.add_cascade(label="Editar", menu=self.editMenu)
    def createMidiMenu(self):
        self.midiMenu = Menu(self.menuBar, tearoff=False)
        self.midiMenu.add_command(label="Montar", command=None)
        self.menuBar.add_cascade(label="MIDI", menu=self.midiMenu)
    def createHelpMenu(self):
        self.helpMenu = Menu(self.menuBar, tearoff=False)
        self.helpMenu.add_command(label="Sobre", command=None)
        self.menuBar.add_cascade(label="Ajuda", menu=self.helpMenu)
    
    # gerenciamento de eventos e fluxo de quadros
    def mainFrameLoop(self):
        if(not self.windowShouldClose):
            try:
                #print(f"Frame number: {self.frameSerial}")
                self.frameSerial += 1
                self.after(self.frameDelta, self.mainFrameLoop)  # agenda um novo quadro
            except Exception as e:
                print(f"Main window was closed - {e}")
    def _on_change(self, event):
        self.linenumbers.redraw()
    def changeWindowTitle(self, title, prefix="Text2MIDI - "):
        self.title(prefix + title)
    def askOpenFile(self):
        self.textFile = fd.askopenfilename(title='Abrir arquivo de projeto', initialdir='/', filetypes=[("Text files","*.txt")])
        self.changeWindowTitle(self.textFile)
        self.checkExported()
    def checkExported(self):
        """Checa se existe um arquivo MIDI com o mesmo nome do projeto no mesmo local indicado pelo arquivo de texto,
        se não, indica no titulo da janela"""
        midiFilePath = self.textFile.rsplit(".", 1)[0] + ".mid"
        if(not pathExists(resourcePath(midiFilePath))):
            if(not self.exported[1]):  # se isso não esta sendo inidicado no titulo
                self.title(self.title() + " - (não exportado)")
                self.exported[1] = True
    def checkSaved(self):
        """Idica se o arquivo atual foi salvo depois de serem realizadas alterações no titulo da janela com um asterisco"""
        if(not self.saved[0]):  # se o arquivo não foi salvo
            if(not self.saved[1]):  # se não houver "*" no titulo da janela
                if(" (não exportado)" in self.title()):  # se houver o titulo de nao exportado no titulo
                    newTitle = self.title().replace(" (não exportado)", "") + "*" + " (não exportado)"
                    self.title(newTitle)
                    self.saved[1] = True
                    return
                self.title(self.title() + "*")
                self.saved[1] = True
        else:  # se o arquivo foi salvo
            if(self.saved[1]):  # se houver um asterisco no titulo da janela
                newTitle = self.title().replace("*", "")  # remove
                self.title(newTitle)  # atualiza o titulo
                self.saved[1] = False

            midiFilePath = self.textFile.rsplit(".", 1)[0] + ".mid"
            self.title(self.title() + " (não exportado)")
    def selectAll(self):
        self.inputEditor.tag_add("sel", "1.0","end") # all text selected
        self.inputEditor.tag_config("sel", background="green", foreground="red")
    def exit(self):
        print("Fechando a janela principal")
        self.destroy()
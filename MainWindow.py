from tkinter import Tk, Frame, Text, Button, Scrollbar, Menu, Label
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

        # menus drop down
        self.menuBar = Menu(self)
        self.config(menu=self.menuBar)
        self.createFileMenu()
        self.createEditMenu()
        self.createMidiMenu()
        self.createHelpMenu()

        # colocar borda

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
        self.fileMenu.add_command(label="Abrir", command=None)
        self.fileMenu.add_command(label="Salvar", command=None)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Fechar", command=self.exit)
        self.menuBar.add_cascade(label="Arquivo", menu=self.fileMenu)
    def createEditMenu(self):
        self.editMenu = Menu(self.menuBar, tearoff=False)
        self.editMenu.add_command(label="Copiar", command=None)
        self.editMenu.add_command(label="Recortar", command=None)
        self.editMenu.add_command(label="Colar", command=None)
        self.editMenu.add_command(label="Selecionar tudo", command=None)
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
    def exit(self):
        print("Fechando a janela principal")
        self.destroy()
from utils import resourcePath, listFromFile
from tkinter import Tk, Frame, Text, Button, Scrollbar, Menu, Label
from tkinter.ttk import Separator
from TextEditor import TextEditor
from CustomText import CustomText
from CustomLabel import CustomLabel
from MidiPlayer import MidiPlayer
import MidiClass
import TextClass

class MainApp(Tk):
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

        # gerenciamento de objetos (frames)
        self.editorFrame = Frame(self, relief="raised", borderwidth=1)
        self.editorFrame.pack(side="left", fill="both", pady=5, padx=5)
        
        self.mediaFrame = Frame(self, relief="raised", borderwidth=1)
        self.mediaFrame.pack(side="right", fill="both", expand=True, pady=5, padx=5)

        # menus drop down
        self.menuBar = Menu(self)
        self.config(menu=self.menuBar)
        self.createFileMenu()
        self.createEditMenu()
        self.createMidiMenu()
        self.createHelpMenu()

        # editor de texto principal
        self.inputEditor = TextEditor(labelText="Editor de texto",
            toolTipText="Texto que vai ser convertido para MIDI",
            hasSubTitle=False,
            initialText="aAbBcC",
            minWidth=25,
            minHeight=20,
            master=self.editorFrame, borderwidth=0)
        self.inputEditor.packWidgets()

        # console e label respectiva
        self.console = TextEditor(labelText="Terminal",
            toolTipText="Saida padrão para o tratamento de erros",
            subtitleText="Status: Pronto",
            initialText="esse eh o console",
            hasLineNumbers=False,
            minWidth=25,
            editable=False,
            master=self.editorFrame)
        self.console.packWidgets()

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
        self.instructionLabels.pack(side="bottom", fill="x", expand=True, padx=5, pady=5, anchor="s")
        
        self.saveFrame = Frame(self.mediaFrame)
        self.saveFrame.pack(side="bottom", pady=5, anchor="se")

        self.closeWindowButton = Button(self.saveFrame, text='Fechar', command=self.exit)
        self.closeWindowButton.pack(side="right", padx=5, pady=5)
        
        self.saveProjectButton = Button(self.saveFrame, text='Salvar projeto', command=None)
        self.saveProjectButton.pack(side="right", pady=5)

        self.exportButton = Button(self.saveFrame, text="Exportar como MIDI", command=None)
        self.exportButton.pack(side="right", padx=5, pady=5)

        self.midiControl = MidiPlayer(master=self.mediaFrame)
        self.midiControl.packWidgets()
        self.midiControl.pack(side="top", expand=True, fill="both", pady=5)

        #self.update()
        self.eval('tk::PlaceWindow . center')
    # criacao de menus
    def createFileMenu(self):
        self.fileMenu = Menu(self.menuBar, tearoff=False)
        self.fileMenu.add_command(label="Novo", command=None)
        self.fileMenu.add_command(label="Abrir texto", command = TextClass.get_text_from_file())
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
        self.midiMenu.add_command(label="Abrir MIDI", command = MidiClass.get_midi_from_file())
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
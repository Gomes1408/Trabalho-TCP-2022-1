from tkinter import Tk

class MainWindow(Tk):
    def __init__(
        self,
        width = 400, # dimensão X inicial da janela
        height = 400, # dimensão Y inicial da janela
        xPlacement = 0,  # define o posicionamento inicial X da janela principal
        yPlacement = 0, # define o posicionamento inicial X da janela principal
        title = "Example window",  # titulo da janela
        resizable = True,  # redimensionamento XY
        frameDelta = 1,  # delay entre frames (ms)
        *args,
        **kwargs):

        Tk.__init__(self, *args, **kwargs)

        # atributos da janela principal
        self.wm_title(title)  # define o titulo inicial da janela
        self.wm_geometry(f"{width}x{height}+{xPlacement}+{yPlacement}")  # define a geometria da janela (tamanho e posicionamento)
        self.wm_resizable(resizable, resizable)  # define se a janela vai ser redimensionavel nos eixos XY

        # atributos de controle da janela principal
        self.windowShouldClose = False  # variavel de controle para o fechamento da janela
        self.frameDelta = frameDelta
        self.frameSerial = 0

    def mainframeloop(self):
        if(not self.windowShouldClose):
            try:
                print(f"Frame number: {self.frameSerial}")
                self.frameSerial += 1
                self.after(self.frameDelta, self.mainframeloop)  # agenda um novo quadro
            except Exception as e:
                print(f"Main window was closed - {e}")
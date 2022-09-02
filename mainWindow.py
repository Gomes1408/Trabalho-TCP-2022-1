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
        frame_delta = 1,  # delay entre frames (ms)
        *args,
        **kwargs):

        Tk.__init__(self, *args, **kwargs)

        self.wm_title(title)  # define o titulo inicial da janela
        self.wm_geometry(f"{width}x{height}+{xPlacement}+{yPlacement}")  # define a geometria da janela (tamanho e posicionamento)
        self.wm_resizable(resizable, resizable)  # define se a janela vai ser redimensionavel nos eixos XY
        self.windowShouldClose = False  # variavel de controle para o fechamento da janela

        def main_frame_loop(self):
            if(not self.windowShouldClose):
                try:
                    self.window.after(frame_delta, self.main_frame_loop)  # agenda um novo quadro
                except Exception as e:
                    print("Main window was closed")
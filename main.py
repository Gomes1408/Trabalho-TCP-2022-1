from sys import argv
from MainWindow import MainWindow

def main(argv):
    if(argv):
        print(f"Recuperou: {argv}")
    
    janelaPrincipal = MainWindow(title = "Text2MIDI - Projeto sem nome*")
    janelaPrincipal.update()
    janelaPrincipal.mainFrameLoop()
    janelaPrincipal.mainloop()  # metodo mainloop (tkinter) para atualizar a janela

if(__name__ == "__main__"):
    main(argv)
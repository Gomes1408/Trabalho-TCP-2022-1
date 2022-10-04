from sys import argv
from MainApp import MainApp

def main(argv):
    if(argv):
        print(f"Recuperou: {argv}")
    
    #Instanciação da janela principal de execução
    janelaPrincipal = MainApp(title = "Text2MIDI - Projeto sem nome")
    janelaPrincipal.update()
    janelaPrincipal.mainFrameLoop()
    janelaPrincipal.mainloop()  # metodo mainloop (tkinter) para atualizar a janela

if(__name__ == "__main__"):
    main(argv)
from sys import argv
from MainWindow import MainWindow
import mido
import TextClass

def main(argv):
    print("Ola trabalho!")

    teste = TextClass.Text("ABCDEFG !ABCDEFGbbABCDEFG", None)

    teste.text_to_MIDI()

    port = mido.open_output()

    for msg in mido.MidiFile('a').play():
        port.send(msg)

    if(argv):
        print(f"Recuperou: {argv}")
    
    janelaPrincipal = MainApp(title="Text2MIDI - Projeto sem nome")
    janelaPrincipal.update()
    janelaPrincipal.mainFrameLoop()
    janelaPrincipal.mainloop()  # metodo mainloop (tkinter) para atualizar a janela

if(__name__ == "__main__"):
    main(argv)
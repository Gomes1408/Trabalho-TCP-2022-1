from sys import argv
from mainWindow import MainWindow

def main(argv):
    print("Ola trabalho!")

    if(argv):
        print(f"Recuperou: {argv}")

    janelaPrincipal = MainWindow()
    janelaPrincipal.mainframeloop()
    janelaPrincipal.mainloop()

if(__name__ == "__main__"):
    main(argv)
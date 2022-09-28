from sys import argv
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

if(__name__ == "__main__"):
    main(argv)
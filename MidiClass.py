import mido
from mido import MidiFile

class Midi:
    def __init__(self):
        self.midi = None
        self.midiFilePath = None

    def get_midi_from_obj(self, midiObj):
        self.midi = midiObj
    
    def get_midi_from_file(self, filePath):
        self.midiFilePath = filePath
        
        self.midi = MidiFile(filePath)

    def play_midi(self):
        print('Tocando')
        
        port = mido.open_output()
        
        if(self.midi != None):
            for msg in self.midi.play():
                port.send(msg)
        else:
            print("Erro, nenhum objeto midi encontrado.")
        
import pygame

class Midi:
    def __init__(self, text: str, corresponding_Text):
        self.text = text
        self.corresponding_MIDI = corresponding_Text

    def get_midi_from_file(self):
        file = input("\nEscreva o nome de um arquivo existente a ser lido: ")
        self.text = open(file, 'r', encoding="utf-8")

    def MIDI_to_text(self):
        file = input("\nInsira o nome do novo arquivo MIDI a ser criado: ")
        
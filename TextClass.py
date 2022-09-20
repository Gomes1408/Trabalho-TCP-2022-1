import pygame

class Text:
    def __init__(self, text: str, corresponding_MIDI):
        self.text = text
        self.corresponding_MIDI = corresponding_MIDI

    def get_text_from_file(self):
        file = input("\nEscreva o nome de um arquivo existente a ser lido: ")
        self.text = open(file, 'r', encoding="utf-8")
    
    def get_text_from_label(self):
        print('Hello')

    def text_to_MIDI(self):
        file = input("\nInsira o nome do novo arquivo MIDI a ser criado: ")
        
        



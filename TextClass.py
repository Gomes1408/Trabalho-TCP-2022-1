from mido import Message, MidiFile, MidiTrack

#Definição de valores padrões para o MIDI
DEFAULT_VELOCITY = 31
DEFAULT_TIME = 32
DEFAULT_OCTAVE = 1
DEFAULT_PROGRAM = 0

#Definição de valores máximos para o MIDI
MAX_PROGRAM = 127
MAX_VELOCITY = 127
MAX_OCTAVE = 8

#Definição das frequências básicas de cada nota
VALUE_C0 = 12
VALUE_D0 = 14
VALUE_E0 = 16
VALUE_F0 = 17
VALUE_G0 = 19
VALUE_A0 = 21
VALUE_B0 = 23

#Definição de valores de programas(instrumentos) utilizados
PROGRAM_HARPSICHORD = 7
PROGRAM_TUBULAR_BELLS = 15
PROGRAM_CHURCH_ORGAN = 20
PROGRAM_PAN_FLUTE = 76
PROGRAM_AGOGO = 114

class TextCstm:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, text: str, corresponding_MIDI):
        #Atributo que contém o corpo do texto
        self.text = text
        #Atributo que armazena o objeto MIDI criado a partir do corpo de texto
        self.corresponding_MIDI = corresponding_MIDI

    #Função para restaurar texto a partir de um arquivo, cujo caminho é passado como parâmetro
    def get_text_from_file(self, filePath):
        trgtFile = open(filePath, 'r', encoding="utf-8")
        self.text = trgtFile.read()
        trgtFile.close()

    #Função que cria um objeto MIDI a partir do texto 
    def text_to_MIDI(self):
        #print('Montando:')
        #print(self.text)

        #file = "teste.mid"
        
        #Criação do objeto MIDI
        newMIDI = MidiFile(type = 0)
        newTrack = MidiTrack()
        newMIDI.tracks.append(newTrack)

        #Definição de valores utilizados pra conversão
        readNote = False
        valPrevNote = 0

        currOctave = DEFAULT_OCTAVE
        currVel = DEFAULT_VELOCITY
        currProgram = DEFAULT_PROGRAM

        tempProgram = 0

        #Parsing do texto, feito caractere a caractere
        for chr in self.text:
            #Conversão de caracteres maiúsculos para suas notas equivalentes
            if chr == 'C':
                readNote = True
                valPrevNote = VALUE_C0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                
            elif chr == 'D':
                readNote = True
                valPrevNote = VALUE_D0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

            elif chr == 'E':
                readNote = True
                valPrevNote = VALUE_E0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

            elif chr == 'F':
                readNote = True
                valPrevNote = VALUE_F0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

            elif chr == 'G':
                readNote = True
                valPrevNote = VALUE_G0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

            elif chr == 'A':
                readNote = True
                valPrevNote = VALUE_A0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

            elif chr == 'B':
                readNote = True
                valPrevNote = VALUE_B0 + currOctave*12
                
                newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

            #Aumento de volume
            elif chr == ' ':
                currVel = 2*currVel

                if currVel > MAX_VELOCITY:
                    currVel = DEFAULT_VELOCITY

            #Trocas de instrumentos
            elif chr == '!':
                newTrack.append(Message('program_change', program = PROGRAM_AGOGO))
                currProgram = PROGRAM_AGOGO

            elif chr.lower() == 'o' or chr.lower() == 'i' or chr.lower() == 'u':
                newTrack.append(Message('program_change', program = PROGRAM_HARPSICHORD))
                currProgram = PROGRAM_HARPSICHORD

            elif ord(chr) >= ord('0') and ord(chr) <= ord('9'):
                tempProgram = currProgram + ord(chr) - ord('0')

                if(tempProgram > MAX_PROGRAM):
                    tempProgram = DEFAULT_PROGRAM
                
                currProgram = tempProgram
                newTrack.append(Message('program_change', program = currProgram))

            elif chr == '\n':
                newTrack.append(Message('program_change', program = PROGRAM_TUBULAR_BELLS))
                currProgram = PROGRAM_TUBULAR_BELLS

            elif chr == ';':
                newTrack.append(Message('program_change', program = PROGRAM_PAN_FLUTE))
                currProgram = PROGRAM_PAN_FLUTE

            elif chr == ',':
                newTrack.append(Message('program_change', program = PROGRAM_CHURCH_ORGAN))
                currProgram = PROGRAM_CHURCH_ORGAN

            #Aumento da oitava
            elif chr == '?' or chr == '.':
                if currOctave < MAX_OCTAVE:
                    currOctave = currOctave + 1
                else:
                    currOctave = DEFAULT_OCTAVE

            #Caso padrão    
            else:
                if readNote:
                    readNote = False

                    newTrack.append(Message('note_on', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                    newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))
                else:
                    newTrack.append(Message('note_off', note = valPrevNote, velocity = currVel, time = DEFAULT_TIME))

        #newMIDI.save(file)

        #Atribuição do objeto MIDI criado ao objeto atual
        self.corresponding_MIDI = newMIDI

        



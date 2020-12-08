from src.music.note import Note

import random

class Melody():

    def __init__(self, name, tempo = 0, notes = [], octaves = [], duration = [], repeat = 1
    ):
        self.name = name
        self.tempo = tempo
        self.notes = notes
        self.octaves = octaves
        self.duration = duration
        self.repeat = repeat
    
    def get_name(self):
        return self.name
    
    def get_tempo(self):
        return self.tempo
    
    def get_notes(self):
        return self.notes
    
    def get_octaves(self):
        return self.octaves

    def get_duration(self):
        return self.duration
    
    def get_repeat(self):
        return self.repeat
    
    def generate_random_melody(self, notes, tempo, octave, number_of_notes):
        list_notes_generated = []

        tempo_seconds = 60 / tempo
        list_duration = [2, 1, 0.5, 0.25]

        for i in range(number_of_notes):
            print(i)
            random_note = random.choice(notes)
            random_duration = random.choice(list_duration) * tempo_seconds
            list_notes_generated.append(Note(random_note, octave, random_duration))
        
        return list_notes_generated



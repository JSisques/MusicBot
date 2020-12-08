from src.music.note import Note
from src.music.player import Player
from src.music.melody import Melody

import json, time

player = Player(44100)
'''
DO = Note("DO", 4, 1)
DO_SHARP = Note("DO#", 4, 1)
RE = Note("RE", 4, 1)
RE_SHARP = Note("RE#", 4, 1)
MI = Note("MI", 4, 1)
FA = Note("FA", 4, 1)
FA_SHARP = Note("FA#", 4, 1)
SOL = Note("SOL", 4, 1)
SOL_SHARP = Note("SOL#", 4, 1)
LA = Note("LA", 4, 1)
LA_SHARP = Note("LA#", 4, 1)
SI = Note("SI", 4, 1)

all_notes = [DO, DO_SHARP, RE, RE_SHARP, MI, FA, FA_SHARP, SOL, SOL_SHARP, LA, LA_SHARP, SI]
for note in all_notes:
    print(note.get_frecuency())
    print(note.get_octave())
    player.play_note(note)

def load_melodies():
    melodies = []
    with open('melodies.json') as json_file:
        data = json.load(json_file)
        for p in data['melodies']:
            name = p["name"]
            tempo = p["tempo"]
            notes = p["notes"]
            octaves = p["octaves"]
            duration = p["duration"]
            repeat = p["repeat"]
            melodies.append(Melody(name, tempo, notes, octaves, duration, repeat))
    
    return melodies

melodies = load_melodies()

for i in melodies: 
    print(i.get_name())
    print(i.get_tempo())
    print(i.get_notes())
    print(i.get_octaves())
    print(i.get_duration())
    print(i.get_repeat())


for melody in melodies:
    player.play_melody(melody)
    time.sleep(1)
'''

scale = ["DO", "RE", "MI", "FA", "SOL", "LA", "SI"]
melody = Melody("Random")

generated_melody = melody.generate_random_melody(scale, 180, 4, 40)

player.play_random_melody(generated_melody)
from src.music.note import Note
from src.music.melody import Melody

import numpy as np
import simpleaudio as sa
import time

class Player():

    def __init__(self, samples_per_second):
        self.samples_per_second = samples_per_second

    def play_melody(self, melody):
        tempo = 60 / melody.get_tempo()

        notes = melody.get_notes()
        octaves = melody.get_octaves()
        duration = melody.get_duration()
        repeat = int(melody.get_repeat())

        number_of_notes = notes.__len__()

        for times in range(repeat):
            for i in range(number_of_notes):
                note_to_play = Note(notes[i], octaves[i], duration[i] * tempo)

                seconds = note_to_play.get_duration()
                t = np.linspace(0, seconds, seconds * self.samples_per_second, False)

                note = note_to_play.get_frecuency()

                generated_note = np.sin(note* t * 2 * np.pi)

                audio = generated_note * (2**15 - 1) / np.max(np.abs(generated_note))
                audio = audio.astype(np.int16)

                play_obj = sa.play_buffer(audio, 1, 2, self.samples_per_second)

                time.sleep(seconds)
        

    def play_note(self, note_object):
        seconds = note_object.get_duration()
        t = np.linspace(0, seconds, seconds * self.samples_per_second, False)

        note = note_object.get_frecuency()

        generated_note = np.sin(note* t * 2 * np.pi)

        audio = generated_note * (2**15 - 1) / np.max(np.abs(generated_note))
        audio = audio.astype(np.int16)

        play_obj = sa.play_buffer(audio, 1, 2, self.samples_per_second)

        time.sleep(seconds)
    
    def play_random_melody(self, melody):
        for note in melody:
            self.play_note(note)
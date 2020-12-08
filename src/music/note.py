class Note():

    def __init__(self, name, octave, duration):

        frecuencies = {
            " ": 0,
            "DO": 32.7,
            "DO#": 34.65,
            "RE": 36.71,
            "RE#": 38.89,
            "MI": 41.2,
            "FA": 43.65,
            "FA#": 46.25,
            "SOL": 49,
            "SOL#": 51.91,
            "LA": 55,
            "LA#": 58.27,
            "SI": 61.74
        }

        self.name = name.upper()

        if octave <= 0 :
            octave = 1
        self.octave = octave        
        self.frecuency = frecuencies.get(self.name) * 2**(octave - 1)

        self.duration = duration

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_frecuency(self):
        return self.frecuency

    def set_frecuency(self, frecuency):
        self.frecuency
    
    def get_octave(self):
        return self.octave
    
    def set_octave(self, octave):
        self.octave = octave

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration
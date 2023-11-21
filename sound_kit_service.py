import wave
from array import array


# 1 octet = 8 bit
# 1 bytes = 8 bit
# Ici les samples sont en 16 bit ou 2 bytes
# Samples = int qui represente l'amplitude d'un signal sonore à un instant t
# Pour les lire, il nous les faut en 16bits

class Sound:
    def __init__(self,filename,displayname):
        self.filename = filename
        self.displayname = displayname
        self.nb_samples = None
        self.samples = None
        self.load_sound()

    def load_sound(self):
        wav_file = wave.open(self.filename, mode="rb")
        self.nb_samples = wav_file.getnframes()
        # On recupere les samples sous forme de 8 bit Mais nous on veut les convertir ensuite en format 16bits
        samples_8bits = wav_file.readframes(self.nb_samples)
        self.samples = array("h",samples_8bits)


class SoundKit:
    sounds=()
    def get_nb_track(self):
        return len(self.sounds)
    
    def get_all_samples(self):
        all_samples = []
        for i in range(len(self.sounds)):
            all_samples.append(self.sounds[i].samples)
        return all_samples


class SoundKit1(SoundKit):
    sounds = (
        Sound("sounds/kit1/kick.wav","KICK"),
        Sound("sounds/kit1/clap.wav","CLAP"),
        Sound("sounds/kit1/shaker.wav","SHAKER"),
        Sound("sounds/kit1/snare.wav","SNARE")
    )


class SoundKitService:
    soundkit = SoundKit1()

    def get_sound(self,index):
        return self.soundkit.sounds[index]

    def get_nb_track(self):
        return len(self.soundkit.sounds)



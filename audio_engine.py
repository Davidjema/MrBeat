from audiostream.core import get_output
from audio_source_one_shot import AudioSourceOneShot

"""
# get a output stream where we can play samples
stream = get_output(channels=2, rate=22050, buffersize=1024)

# create one wave sin() at 440Hz, attach it to our speaker, and play
sinsource = SineSource(stream, 440)
sinsource.start()

Principe :
# 1- On configure une sortie "stream" connecté aux haut parleurs
# 2- On configure une "source" ou un "generateur" qui va generer les samples.
     Le genrateur va aussi appelé la fonction get_bytes pour les envoyer au buffer qui les envoie aux hauts parleur.
     Le generateur a besoin en argument la sortie.

Question: pourquoi recupere les samples en 8bits. On les convertis en 16bits puis on les remet en 8bits pour les envoyer à la sortie?
"""


class AudioEngine:

    RATE = 44100
    NB_CHANNELS = 1
    ENCODING = 16
    BUFFERSIZE = 1024

    def __init__(self):
        self.output_stream = get_output(rate = self.RATE,
                                        channels = self.NB_CHANNELS,
                                        encoding = self.ENCODING,
                                        buffersize = self.BUFFERSIZE)
        
        
        self.audio_source_one_shot = AudioSourceOneShot(self.output_stream)
        self.audio_source_one_shot.start()
        
    def play_sound(self,samples):
        self.audio_source_one_shot.set_samples(samples)





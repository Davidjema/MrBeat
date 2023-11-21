from audiostream.core import get_output
from audio_source_one_shot import AudioSourceOneShot
from audio_source_track import AudioSourceTrack
from audio_source_mixer import AudioSourceMixer

"""
# get a output stream where we can play samples
stream = get_output(channels=2, rate=22050, buffersize=1024)

# create one wave sin() at 440Hz, attach it to our speaker, and play
sinsource = SineSource(stream, 440)
sinsource.start()

Principe :
# 1- On configure une sortie "stream" connecté aux haut parleurs
# 2- On creer une instance "source" ou un "generateur" qui va generer les samples.
# 3 - On passe la sortie "stream" a la source en parametre  
# 4 - Dans la source, il y a une methode get_bytes qui est appelé automatiquement pour recuperer un buffer
# 5 - On start la source - GG
"""


class AudioEngine:

    RATE = 44100
    NB_CHANNELS = 1
    ENCODING = 16
    BUFFERSIZE = 1024
    nb_step = 0

    def __init__(self):
        self.output_stream = get_output(rate = self.RATE,
                                        channels = self.NB_CHANNELS,
                                        encoding = self.ENCODING,
                                        buffersize = self.BUFFERSIZE)
        
        
        self.audio_source_one_shot = AudioSourceOneShot(self.output_stream)
        self.audio_source_one_shot.start()

        
    def play_sound(self,samples):
        self.audio_source_one_shot.set_samples(samples)
        

    def create_track(self,samples,bpm):
        self.samples = samples
        self.bpm = bpm

        audio_source_track = AudioSourceTrack(self.output_stream,self.samples,self.bpm,self.RATE)
        audio_source_track.start()
        return audio_source_track
    
    def create_mixer(self,all_samples,bpm,nb_step):
        audio_source_mixer = AudioSourceMixer(self.output_stream,all_samples,self.RATE,nb_step)
        audio_source_mixer.start()
        return audio_source_mixer



        



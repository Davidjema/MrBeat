from audiostream.sources.thread import ThreadSource
from array import array

# 44100 samples par seconde = samples_rate
# 44100*60 sample par minute
# 1 battement = (44100*60)/BPM sample
# 1 step = 1/4 battement = (44100*60)/(4*BPM)
# 1 step = 44100 * 15 / BPM   ( Nombre de sample pour 1 step)
# 1 step = samples_rate * 15 /BPM
# Penser a se proteger contre tous les cas même si c'est pas censé se produire
# En programmation ce qui ne devait pas arriver arrive quand meme --> Donc il faut prevoir TOUS les cas pour rendre le code SOLIDE

class AudioSourceTrack(ThreadSource):
    steps = ()
    step_nb_samples = 0
    buf = None

    def __init__(self,output_stream,samples,bpm,samples_rate,*args, **kwargs):
        ThreadSource.__init__(self,output_stream,*args,**kwargs)
        self.samples = samples
        self.nb_samples = len(samples)
        self.bpm = bpm
        self.sample_rate = samples_rate
        self.compute_steps_samples_and_alloc_buf()
 

        self.current_sample_index = 0
        self.current_step_index = 0
        self.last_sound_start_sample_index = 0


    def set_steps(self,steps):
        # On renitialise si le nb de step change mais pas si les steps sont enfonce ou pas 
        if not len(steps) == len(self.steps):
            self.current_step_index = 0
        self.steps = steps

    def set_bpm(self,bpm):
        self.bpm = bpm
        self.compute_steps_samples_and_alloc_buf()

# Fonction qui nous permet de calculer la taille du buffer et donc la taille d'une step // et de l'initialiser
    def compute_steps_samples_and_alloc_buf(self):
        if not self.bpm == 0:
            #self.step_nb_samples = int(self.sample_rate * 15 / self.bpm)
            n = int(self.sample_rate * 15 / self.bpm)
            if not n == self.step_nb_samples:
                self.step_nb_samples = n
                self.buf = array('h',b"\x00\x00"* self.step_nb_samples)


    def get_bytes_array(self):

        for i in range(0,self.step_nb_samples):
            
            if len(self.steps) > 0 :
                # si la step est plus longue que le son 
                if self.steps[self.current_step_index] == 1 and i < self.nb_samples:
                    self.buf[i] = self.samples[i]
                    if i == 0:
                        # Si c est une nouvelle step, on reinitialise current_sample_index
                        self.current_sample_index = 0
                else:
                    if 0 < self.current_sample_index < self.nb_samples:
                        self.buf[i] = self.samples[self.current_sample_index]
                    else:
                        self.buf[i] = 0                
            else:
                self.buf[i]= 0
            self.current_sample_index += 1

        self.current_step_index += 1
        if self.current_step_index >= len(self.steps):
            self.current_step_index = 0

        return self.buf
    

        def get_bytes(self,*args,**kwargs):
            return self.get_bytes_array().tobytes()
        



# Un cas si le son est plus petit que la step
# Il faut continuer a jouer le silence jusqu'à la prochaine step au moins
# On continue a jouer le son jusqua self.current_sample_index soit plus grand que nb.samples
# On ne le renitialise que si il y a re un son
# Donc si il a son puis silence, le self current sample index sera tjr plus grand que le nb sample
# Et on cotinura a jouer du silence tant que on aura pas re initialiser le current_sample_index lors dun new son


# Un cas ou si le son est plus grand que la step.
# Verifier si la step d'apres est active oui ou non

# Si oui --> Son puis new son   --> reccomencer le son depuis le debut
# Si non --> son puis silence --> continuer a jouer le son jusqu a la fin du nb_sample

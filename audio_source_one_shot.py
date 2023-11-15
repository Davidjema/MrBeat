from audiostream.sources.thread import ThreadSource
from array import array

# ThreadSource -> Thread c est un processus
# Ici la fonction get_bytes est spécifique a audiostream 
# Elle est appele de facon automatique par le CPU en fonction du buffer et de ce qu il lui reste dans le fifo

class AudioSourceOneShot(ThreadSource):
    # On a besoin du output_steam pour initliser le ThreadSource
    def __init__(self,output_stream,*args, **kwargs):
        ThreadSource.__init__(self,output_stream,*args,**kwargs)
        self.chunk_nb_samples = 32
        self.samples = None
        self.nb_samples = 0
        self.current_sample_index = 0
        # 0 en 8bits c'est \x00
        # 0 en 16bits c'est \xoo\xoo
        # un buf c'est une liste ?
        self.buf = array('h',b"\x00\x00"* self.chunk_nb_samples)
        self.set_samples(self.buf)

    def set_samples(self,samples):
        self.samples = samples
        self.current_sample_index = 0
        # Placer le nb_samples en dernier car si get_bytes est appelé alors qu'on a pas encore stocker les samples sa va buger
        self.nb_samples = len(samples)

    def get_bytes(self,*args,**kwargs):

        if self.nb_samples > 0:
            for i in range(0,self.chunk_nb_samples):
                if self.current_sample_index < self.nb_samples:
                    self.buf[i] = self.samples[self.current_sample_index]
                else:
                    self.buf[i] = 0
                self.current_sample_index += 1
        else:
            for i in range(0,self.chunk_nb_samples):
                self.buf[i] = 0
        

        return self.buf.tobytes()
        


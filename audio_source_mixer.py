from audiostream.sources.thread import ThreadSource
from array import array
from audio_source_track import AudioSourceTrack


class AudioSourceMixer(ThreadSource):
    buf = None

    def __init__(self,output_stream,all_samples,sample_rate,nb_steps,*args, **kwargs):
        ThreadSource.__init__(self,output_stream,*args,**kwargs)
        # all_samples c'est un tableau de nb track * nb samples
        self.all_samples = all_samples
        self.sample_rate = sample_rate
        self.current_step_index = 0
        self.nb_steps = nb_steps
        bpm = 100

        self.audio_sources_track = []
        for i in range(len(all_samples)):
            audio_source_track = AudioSourceTrack(output_stream,all_samples[i],bpm,self.sample_rate)
            # On impose le nb step dans le mixer
            audio_source_track.set_steps( (0,) * nb_steps)
            self.audio_sources_track.append(audio_source_track)

      
# le set_steps du audiomixer --> on set_step tous les tracksource
    def set_steps(self,index,steps):
        if index > len(self.audio_sources_track):
            return
        # On impose le nb step dans le mixeur // ici 16 , on passe le nb step lors de la creation du audiosourcemixer
        if not len(steps) == self.nb_steps:
            self.audio_sources_track[index].set_steps(steps)

    def set_bpm(self,bpm):
        for i in range(len(self.audio_sources_track)):
            self.audio_sources_track(i).set_bpm(bpm)


    def get_bytes(self,*args,**kwargs):

        step_nb_samples = self.audio_sources_track[0].step_nb_samples
        
        if self.buf is None or not len(self.buf) == step_nb_samples:
            self.buf = array('h',b"\x00\x00"* step_nb_samples)

        # On creer un tableau dans lequel on va stocker tous les samples d'une meme step.
        audio_sources_track_buffers = []
        for i in range(len(self.audio_sources_track)):
            audio_source_buf = self.audio_sources_track[i].get_bytes_array()
            audio_sources_track_buffers.append(audio_source_buf)
            
        for i in range(0,step_nb_samples):
            self.buf[i]= 0
            for j in range(0,len(audio_sources_track_buffers)):
                self.buf[i] += audio_sources_track_buffers[j][i]


        self.current_step_index += 1
        if self.current_step_index >= self.nb_steps:
            self.current_step_index = 0

        return self.buf.tobytes()
        



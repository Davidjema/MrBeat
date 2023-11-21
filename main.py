from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from sound_kit_service import SoundKitService
from track import TrackWidget
from audio_engine import AudioEngine
from audio_source_mixer import AudioSourceMixer


Builder.load_file("track.kv")

NB_STEP = 16


class MainWidget(RelativeLayout):
    toto = ObjectProperty()

    def __init__(self, **kw):
        super(MainWidget,self).__init__(**kw)
        self.NB_STEP = NB_STEP
        self.sound_kit_service = SoundKitService()
        self.NB_TRACK = self.sound_kit_service.get_nb_track()

        self.audio_engine = AudioEngine() 

        self.all_samples = self.sound_kit_service.soundkit.get_all_samples()
        self.mixer = self.audio_engine.create_mixer(self.all_samples,120,self.NB_STEP)


# fonction speciale de kivy / Est appele automatiquement lorsque le widget est rajoute au widget parent 
# Permet aussi d utiliser self.add_widget sur le boxlayout qu'on aura bind avec object property car la fonction est appelé apres que le fichier kv se soit chargé 
# On peut pas ajouter un widget "simple" a un relative layout
# Alternative --> On creer une boxlayout , on y insere les trackwidget , on ajoute ce widget  à MainWidget avec self.add_widget(custom_boxlayout)
    def on_parent(self,widget,parent):
        for i in range(self.NB_TRACK):
            sound = self.sound_kit_service.get_sound(i)
            self.toto.add_widget(TrackWidget(sound,self.audio_engine,self.NB_STEP,self.mixer.audio_sources_track[i]))


class ControlButton(Button):
    pass



class MrBeat(App):
    pass



MrBeat().run()



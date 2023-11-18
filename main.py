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


Builder.load_file("track.kv")


class MainWidget(RelativeLayout):
    toto = ObjectProperty()

    def __init__(self, **kw):
        super(MainWidget,self).__init__(**kw)
        self.sound_kit_service = SoundKitService()
        self.NB_TRACK = self.sound_kit_service.get_nb_track()
        kick_sound = self.sound_kit_service.get_sound(1)
        kick_samples = kick_sound.samples 

        self.audio_engine = AudioEngine() 
        self.audio_engine.create_track(kick_samples,180)


# fonction speciale de kivy / Est appele automatiquement lorsque le widget est rajoute au widget parent / On peut avoir 1 on_parent par widget
# Permet aussi d utiliser self.add_widget sur le boxlayout qu'on aura bind avec object property car la fonction est appelé apres que le fichier kv se soit chargé 
# On peut pas ajouter un widget "simple" a un relative layout
# Alternative --> On creer une boxlayout , on y insere les trackwidget , on ajoute ce widget  à MainWidget avec self.add_widget(custom_boxlayout)
    def on_parent(self,widget,parent):
        for i in range(self.NB_TRACK):
            sound = self.sound_kit_service.get_sound(i)
            self.toto.add_widget(TrackWidget(sound,self.audio_engine))


class ControlButton(Button):
    pass



class MrBeat(App):
    pass



MrBeat().run()



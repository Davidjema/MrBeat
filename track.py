from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import ObjectProperty


NB_STEP = 16

class TrackSoundButton(Button):
    pass

class TrackStepButton(ToggleButton):
    pass

class TrackWidget(BoxLayout):
    # si on initialise pas, on peut pas ajouter un trackstepbutton sur le trackwidget car on a pas le self
    def __init__(self,sound,audio_engine,**kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        self.audio_engine = audio_engine
        self.sound = sound
        self.samples = sound.samples
        track_sound_button = TrackSoundButton()
        track_sound_button.text = sound.displayname
        # sur un boutton on peut appller la fonction associé integree dans kivy .on_press pour effectuer des actions une fois que le bouton a été cliqué
        track_sound_button.on_press = self.on_press_track_sound_button
        self.add_widget(track_sound_button)
        for i in range(NB_STEP):
            self.add_widget(TrackStepButton())

    def on_press_track_sound_button(self):
        print("son")
        self.audio_engine.play_sound(self.samples)



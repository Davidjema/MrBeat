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
    def __init__(self,filename,**kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        self.track_sound_button = TrackSoundButton()
        self.track_sound_button.text = filename
        self.add_widget(self.track_sound_button)
        for i in range(NB_STEP):
            self.add_widget(TrackStepButton())


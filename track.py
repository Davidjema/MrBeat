from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

NB_STEP = 16

class TrackSoundButton(Button):
    pass


#ToggleButton a un state enfonce ou normal
#On peut utiliser la methode "bind" sur un ToggleButton pour definir une fonction qui sera appelé quand 
# l'état du ToggleButton aura changé --> Op 
class TrackStepButton(ToggleButton):
    pass

class TrackWidget(BoxLayout):
    # si on initialise pas, on peut pas ajouter un trackstepbutton sur le trackwidget car on a pas le self
    def __init__(self,sound,audio_engine,NB_STEP,audio_source_track,**kwargs):
        super(TrackWidget, self).__init__(**kwargs)
        self.audio_engine = audio_engine
        self.sound = sound
        self.samples = sound.samples
        track_sound_button = TrackSoundButton()
        track_sound_button.text = sound.displayname
        # sur un boutton on peut appller la fonction associé integree dans kivy .on_press pour effectuer des actions une fois que le bouton a été cliqué
        track_sound_button.on_press = self.on_press_track_sound_button
        self.add_widget(track_sound_button)

        self.audio_source_track =  audio_source_track

        self.step_buttons = []
        for i in range(NB_STEP):
            step_button = TrackStepButton()
            step_button.bind(state=self.on_step_button_state)
            self.step_buttons.append(step_button)
            self.add_widget(step_button)

    def on_press_track_sound_button(self):
        self.audio_engine.play_sound(self.samples)


    def on_step_button_state(self,widget,value):
        steps = []
        for i in range(NB_STEP):
            if self.step_buttons[i].state == "down":
                steps.append(1)
            else:
                steps.append(0)
        # appeler la fonction set_steps du du tracksource
        self.audio_source_track.set_steps(steps)



class Sound:
    #filename
    #displayname
    def __init__(self,filename,displayname):
        self.filename = filename
        self.displayname = displayname

class SoundKit:
    sounds=()
    def get_nb_track(self):
        return len(self.sounds)

class SoundKit1(SoundKit):
    sounds = (
        Sound("sounds/kit1/kick/wav","KICK"),
        Sound("sounds/kit1/clap/wav","CLAP"),
        Sound("sounds/kit1/shaker/wav","SHAKER"),
        Sound("sounds/kit1/snare/wav","SNARE")
    )


class SoundKitService:
    soundkit = SoundKit1()

    def get_sound(self,index):
        return self.soundkit.sounds[index]

    def get_nb_track(self):
        return len(self.soundkit.sounds)



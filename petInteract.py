from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase

Window.size = (350, 600)

class PetInteract(MDApp):
    def build(self):
        return Builder.load_file('petInteract.kv')

LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')

if __name__ == '__main__':
    PetInteract().run()
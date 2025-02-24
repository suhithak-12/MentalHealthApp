from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.core.text import LabelBase

Window.size = (350, 600)


LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')


class ResourcePage(MDApp):
    def build(self):
        return Builder.load_file('resource.kv')

if __name__ == "__main__":
    ResourcePage().run()

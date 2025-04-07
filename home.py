
import kivy.utils
import requests
import random
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (350, 600)

class HomeScreen(Screen):  # Changed class name to avoid conflict
    pass
    def switch_screen(self, instance):
        self.dialog.dismiss()
        self.manager.current = "habit"
    def switch_screen(self, instance):
        self.dialog.dismiss()
        self.manager.current = "resources"

    def show_happy_popup(self):
        messages = [
            "You're doing amazing! <3",
            "Keep smiling, sunshine! :)",
            "One step at a time, you're getting there!",
            "You're stronger than you think <3",
            "Take a deep breath and feel the peace :)",
            "Today is full of possibilities!",
            "Your effort matters. Always.",
            "Go you!! <3",
            "Penguin believes in you!",
            "Sending good vibes your way :)"
        ]
        random_message = random.choice(messages)

        self.dialog = MDDialog(
            title="Happiness!",
            text=random_message,
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda x: self.dialog.dismiss()
                )
            ]
        )
        self.dialog.open()   

# Register the custom fonts
LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')

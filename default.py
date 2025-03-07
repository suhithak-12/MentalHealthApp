from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFloatingActionButton, MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem
from kivymd.uix.gridlayout import MDGridLayout

Window.size = (350, 600)  

KV = """
Screen:
    MDBoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "TRACK YOUR HABITS!"
            specific_text_color: 0, 0, 0, 1
            pos_hint: {"top": 1}

        MDLabel:
            text: "What have you done today?"
            halign: "center"
            font_style: "H5"
            size_hint_y: None
            height: self.texture_size[1] + 20

        MDGridLayout:
            cols: 2
            padding: dp(20)
            spacing: dp(10)

            MDRaisedButton:
                text: "Water Tracker"
                size_hint_x: None
                width: dp(140)

            MDRaisedButton:
                text: "Mood Tracker"
                size_hint_x: None
                width: dp(140)

            MDRaisedButton:
                text: "Shower Tracker"
                size_hint_x: None
                width: dp(140)

            MDRaisedButton:
                text: "Sleep Tracker"
                size_hint_x: None
                width: dp(140)

            MDRaisedButton:
                text: "Meals Tracker"
                size_hint_x: None
                width: dp(140)

            MDRaisedButton:
                text: "Exercise Tracker"
                size_hint_x: None
                width: dp(140)

        
        MDFloatingActionButton:
            icon: "plus"
            pos_hint: {"center_x": 0.5, "y": 0.05} 
            size_hint: None, None
            size: dp(56), dp(56)
            elevation: 8
"""

class HabitTrackerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    HabitTrackerApp().run()

from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.progressbar import MDProgressBar
from kivy.properties import NumericProperty

LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')

Window.size = (350, 600)

KV = '''
ScreenManager:
    MainScreen:
    EditScreen:

<MainScreen>:
    name: "main"

    MDBoxLayout:
        orientation: "vertical"
        md_bg_color: 1, 1, 1, 1
        padding: dp(20)
        spacing: dp(20)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        Widget:
            size_hint_y: 0.2

        MDLabel:
            text: "Welcome to the water tracker!! You can set your goal by clicking 'Edit'.Then you're all set! Click the 'Water' button every time you drink 1 glass!"
            halign: "center"
            theme_text_color: "Primary"
            font_name: "kr"
            size_hint_y: None
            height: self.texture_size[1] + dp(20)

        MDProgressBar:
            id: progress
            value: 0
            max: 10
            size_hint_y: None
            height: dp(10)

        MDBoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: dp(48)
            spacing: dp(10)
            pos_hint: {"center_x": 0.5}

            MDRaisedButton:
                text: "-"
                on_release: root.decrement_water()
                md_bg_color: 0, 0.5, 1, 1
                
            MDRaisedButton:
                text: "WATER BUTTON"
                on_release: root.increment_water()
                md_bg_color: 0, 0.5, 1, 1
                font_name: "lemon"

            MDRaisedButton:
                text: "+"
                on_release: root.increment_water()
                md_bg_color: 0, 0.5, 1, 1

        MDRaisedButton:
            text: "EDIT"
            pos_hint: {"center_x": 0.5}
            on_release: root.changescreen()
            md_bg_color: 0.9, 0.5, 0.4, 1

        Widget:
            size_hint_y: 0.2

<EditScreen>:
    name: "edit"
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)
        md_bg_color: 231/255, 231/255, 231/255, 1

        MDTopAppBar:
            title: "Edit Goal"
            left_action_items: [["arrow-left", root.changescreen]]
            elevation: 0
            md_bg_color: 221/255, 133/255, 111/255, 1

        MDLabel:
            text: "edit page."
            halign: "center"

        MDRaisedButton: 
            text: "Go Back"
            pos_hint: {"center_x": 0.5}
            on_release: root.changescreen()
'''

class MainScreen(Screen):
    progress_value = NumericProperty(0)

    def increment_water(self):
        progress_bar = self.ids.progress
        if progress_bar.value < progress_bar.max:
            progress_bar.value += 1

    def decrement_water(self):
        progress_bar = self.ids.progress
        if progress_bar.value > 0:
            progress_bar.value -= 1

    def changescreen(self, *args):
        self.manager.current = "edit"

class EditScreen(Screen):
    def changescreen(self, *args):
        self.manager.current = "main"

class WaterTrackerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    WaterTrackerApp().run()

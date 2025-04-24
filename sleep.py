from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.slider import MDSlider
from kivy.properties import NumericProperty

Window.size = (350, 600)

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(30)

        MDLabel:
            text: "SLEEP TRACKER"
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: dp(50)

        MDLabel:
            id: sleep_label
            text: f"You slept: {app.sleep_hours} hrs"
            halign: 'center'
            size_hint_y: None
            height: dp(40)

        MDSlider:
            id: sleep_slider
            min: 0
            max: 12
            step: 1
            value: app.sleep_hours
            on_value: app.update_sleep(self.value)
            size_hint_x: 0.9
            pos_hint: {"center_x": 0.5}

        MDRaisedButton:
            text: "SET GOAL"
            pos_hint: {"center_x": 0.5}
            size_hint: None, None
            size: dp(150), dp(50)
            on_release: app.open_goal_page()
'''

class SleepTrackerApp(MDApp):
    sleep_hours = NumericProperty(0)

    def build(self):
        return Builder.load_string(KV)

    def update_sleep(self, value):
        self.sleep_hours = value
        self.root.ids.sleep_label.text = f"You slept: {value:.1f} hrs"

    def open_goal_page(self):
        print("Opening set goal page...")

if __name__ == '__main__':
    SleepTrackerApp().run()

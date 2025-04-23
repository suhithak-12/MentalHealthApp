from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivy.properties import StringProperty

Window.size = (350, 600)

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "MOOD TRACKER"
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: dp(40)

        MDBoxLayout:
            orientation: 'vertical'
            spacing: dp(20)
            padding: dp(10)
            size_hint: 1, None
            height: self.minimum_height
            pos_hint: {"center_y": 0.5}

            MDLabel:
                text: "Welcome to the mood tracker!! You can save your everyday mood progress here! Just click how you’re feeling today!"
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1] + dp(20)

            GridLayout:
                id: mood_buttons
                cols: 6
                spacing: dp(10)
                padding: dp(10)
                size_hint_y: None
                height: dp(80)
                pos_hint: {"center_x": 0.5}

            MDRaisedButton:
                text: "Submit Mood"
                pos_hint: {"center_x": 0.5}
                size_hint: None, None
                size: dp(150), dp(48)
                on_release: app.submit_mood()
'''

class MoodButton(MDRaisedButton):
    def on_release(self):
        app = MDApp.get_running_app()
        app.set_selected_mood(self)

class MoodTrackerApp(MDApp):
    selected_mood = StringProperty('')
    mood_buttons = []

    def build(self):
        root = Builder.load_string(KV)
        self.populate_moods(root.ids.mood_buttons)
        return root

    def populate_moods(self, layout):
        moods = ['Dead', 'sad', 'existing', 'ehh', 'happy!', 'HAPPYYYYYY']
        for mood in moods:
            btn = MoodButton(text=mood, size_hint=(None, None), size=(48, 48))
            self.mood_buttons.append(btn)
            layout.add_widget(btn)

    def set_selected_mood(self, selected_btn):
        for btn in self.mood_buttons:
            btn.md_bg_color = (1, 1, 1, 1)
        selected_btn.md_bg_color = (0.4, 0.6, 1, 1)  # Blue highlight
        self.selected_mood = selected_btn.text

    def submit_mood(self):
        print(f"Mood submitted: {self.selected_mood}")

if __name__ == '__main__':
    MoodTrackerApp().run()
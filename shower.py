from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

Window.size = (350, 600)

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "SHOWER TRACKER"
            halign: 'center'
            font_style: 'H5'
            size_hint_y: None
            height: dp(40)

        FloatLayout:
            Button:
                text: "showered!"
                size_hint: None, None
                size: dp(120), dp(120)
                pos_hint: {"center_x": 0.3, "center_y": 0.6}
                background_normal: ''
                background_color: 1, 1, 1, 1
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 2
                        circle: (self.center_x, self.center_y, self.width / 2)
                on_release: app.shower_button_pressed(1)

            Button:
                text: "not yet :("
                size_hint: None, None
                size: dp(120), dp(120)
                pos_hint: {"center_x": 0.7, "center_y": 0.6}
                background_normal: ''
                background_color: 1, 1, 1, 1
                color: 0, 0, 0, 1
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1
                    Line:
                        width: 2
                        circle: (self.center_x, self.center_y, self.width / 2)
                on_release: app.shower_button_pressed(2)

        MDLabel:
            id: feedback_label
            text: ""
            halign: 'center'
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            size_hint_y: None
            height: dp(30)
'''

class ShowerTrackerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def shower_button_pressed(self, button_id):
        feedback = "YAYYYYY!!!" if button_id == 1 else "You still have time!!!"
        self.root.ids.feedback_label.text = feedback
        

if __name__ == '__main__':
    ShowerTrackerApp().run()

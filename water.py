from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.dialog import MDDialog

Window.size = (350, 600)

KV = '''
ScreenManager:
    WaterTrackerScreen:
    EditGoalsScreen:

<WaterTrackerScreen>:
    name: 'water_tracker'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)

        MDLabel:
            text: "WATER TRACKER"
            halign: 'center'
            bold: True
            font_style: 'H5'

        MDLabel:
            text: "Welcome to the water tracker!! You can start this tracker by hitting on the 'Edit' button and setting a goal. Then you're all set! Click the 'water' button every time you drink 1 glass of water!"
            halign: 'center'
            size_hint_y: None
            height: dp(80)

        Widget:
            size_hint_y: None
            height: dp(20)
        
        MDFloatLayout:
            MDRaisedButton:
                text: "WATER BUTTON"
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                on_release: app.increment_water()

        MDRaisedButton:
            text: "EDIT"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'edit_goals'

        MDBoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(20)
            padding: dp(20)
            
            MDIconButton:
                icon: 'account'
            MDIconButton:
                icon: 'chart-bar'
            MDIconButton:
                icon: 'home'
            MDIconButton:
                icon: 'equal'
            MDIconButton:
                icon: 'account-circle'

<EditGoalsScreen>:
    name: 'edit_goals'
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        
        MDTopAppBar:
            title: "EDIT Goals"
            left_action_items: [["arrow-left", lambda x: setattr(app.root, 'current', 'water_tracker')]]
        
        MDLabel:
            text: "Set Goal"
            bold: True
        
        MDTextField:
            hint_text: "Enter number of glasses"
            input_filter: 'int'

        MDLabel:
            text: "Frequency Notifications"
            bold: True

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)

            MDCheckbox:
                group: "frequency"
            MDLabel:
                text: "Hourly"
            
            MDCheckbox:
                group: "frequency"
            MDLabel:
                text: "2 Hours"
            
            MDCheckbox:
                group: "frequency"
            MDLabel:
                text: "12 Hours"
        
        MDTextField:
            hint_text: "Notes"
            multiline: True
        
        MDRaisedButton:
            text: "Submit Changes"
            pos_hint: {"center_x": 0.5}
            on_release: app.root.current = 'water_tracker'
'''

class WaterTrackerApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def increment_water(self):
        print("Water button clicked!")

if __name__ == '__main__':
    WaterTrackerApp().run()

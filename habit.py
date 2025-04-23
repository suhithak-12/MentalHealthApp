import kivy.utils
import mysql.connector
import requests
from kivymd.app import MDApp
from kivy.app import App
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (350, 600)

class newHabit(Screen):  # Changed class name to avoid conflict
    pass
    def createHabit(self):
        username = App.get_running_app().username
        habitName = self.ids.habitName.text
        startDate = self.ids.startDate.text
        dayFreq = self.ids.dayFreq.text
        timeRemind = self.ids.timeRemind.text
        Notes = self.ids.Notes.text

        user_habit = {'username': username,'habitName' : habitName, 'startDate' : startDate,
                    'dayFreq' : dayFreq, 'timeRemind' : timeRemind, 'Notes' : Notes}
        url = "http://127.0.0.1:5000/newHabit"

        try:
            response = requests.post(url, data=user_habit)
            response = response.json()
            print(response)
            print("New Habit Created!")
            self.manager.current = "home"
        except requests.exceptions.RequestException as e:
            self.show_dialog(f"Network error: {str(e)}")
        except ValueError:
            self.show_dialog("Invalid server response")

    def switch_screen(self, instance):
        self.dialog.dismiss()
        self.manager.current = "home"

# Register the custom fonts
LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')

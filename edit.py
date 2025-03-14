from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen, ScreenManager

LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')

Window.size = (350, 600)

class EditScreen(Screen):
    dialog = None

    def go_back(self):
        print("Going back to the previous screen...")

    def submit_changes(self):
        print("Changes submitted and database updated.")
        # Access fields like self.root.ids.habit_name.text if needed

    def confirm_delete(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Are you sure?",
                text="Do you want to delete this habit?",
                buttons=[
                    MDFlatButton(
                        text="YES", text_color=(1, 0, 0, 1),
                        on_release=self.delete_habit
                    ),
                    MDFlatButton(
                        text="NO", text_color=(0, 0, 1, 1),
                        on_release=self.close_dialog
                    ),
                ],
            )
        self.dialog.open()

    def delete_habit(self, *args):
        print("Habit deleted.")
        self.dialog.dismiss()

    def close_dialog(self, *args):
        self.dialog.dismiss()
    def changescreen(self, *args):
        self.manager.current = "def"


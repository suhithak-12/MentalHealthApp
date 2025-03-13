from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton

Window.size = (350, 600)

KV = '''
Screen:
    MDBoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)

        MDTopAppBar:
            title: "Edit Habits"
            left_action_items: [["arrow-left", lambda x: app.go_back()]]

        MDTextField:
            id: habit_name
            hint_text: "Habit Name"

        MDTextField:
            id: start_date
            hint_text: "Start Date"

        MDLabel:
            text: "Frequency"
            halign: "left"
            bold: True

        MDBoxLayout:
            orientation: "horizontal"
            spacing: dp(10)

            MDCheckbox:
                group: "frequency"
            MDLabel:
                text: "Daily"
                size_hint_x: None
                width: dp(60)

            MDCheckbox:
                group: "frequency"
            MDLabel:
                text: "Weekly"
                size_hint_x: None
                width: dp(70)

            MDCheckbox:
                group: "frequency"
            MDLabel:
                text: "Monthly"
                size_hint_x: None
                width: dp(80)

        MDBoxLayout:
            orientation: "horizontal"
            spacing: dp(10)
            size_hint_y: None
            height: self.minimum_height

            MDLabel:
                text: "Time Reminder"
                halign: "left"
                bold: True
                size_hint_x: 0.4

            MDTextField:
                id: reminder_time
                hint_text: "HH:MM"
                size_hint_x: 0.6
                input_filter: "int"

        MDBoxLayout:
            orientation: "horizontal"
            spacing: dp(10)

            MDCheckbox:
                group: "reminder"
            MDLabel:
                text: "AM"
                size_hint_x: None
                width: dp(60)

            MDCheckbox:
                group: "reminder"
            MDLabel:
                text: "PM"
                size_hint_x: None
                width: dp(60)

        MDTextField:
            id: notes
            hint_text: "Notes"
            multiline: True

        MDRaisedButton:
            text: "Submit Changes"
            pos_hint: {"center_x": 0.5}
            on_release: app.submit_changes()

        MDFlatButton:
            text: "[b]DELETE HABIT[/b]"
            markup: True
            text_color: 1, 0, 0, 1
            pos_hint: {"center_x": 0.5}
            on_release: app.confirm_delete()
'''

class EditHabitApp(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.primary_hue = "100"  # Lighter shade
        return Builder.load_string(KV)

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

if __name__ == "__main__":
    EditHabitApp().run()

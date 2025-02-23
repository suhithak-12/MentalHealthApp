from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from login import LoginPage
from account_creation import accountCreation

class MyScreenManager(ScreenManager):
    def setransition(self):
        self.transition = SlideTransition() #sets transition between screens

class Mainapp(MDApp):
    def build(self):
        # Load separate KV files
        Builder.load_file("login.kv")
        Builder.load_file("account_creation.kv")

        screenman = MyScreenManager()
        screenman.setransition()
        screenman.add_widget(LoginPage(name="login"))
        screenman.add_widget(accountCreation(name="account_creation"))
        screenman.current = "login"#sets current screen to login
        return screenman

if __name__=='__main__':
    Mainapp().run()

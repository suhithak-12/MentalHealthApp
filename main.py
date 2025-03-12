from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from login import LoginPage
from account_creation import accountCreation
from home import HomeScreen

class MyScreenManager(ScreenManager):
    def set_transition(self):
        self.transition = SlideTransition() #sets transition between screens

class MainApp(MDApp):
    def build(self):
        # Load separate KV files
        Builder.load_file("login.kv")
        Builder.load_file("account_creation.kv")
        Builder.load_file("home.kv")

        screenman = MyScreenManager()
        screenman.set_transition()
        
        screenman.add_widget(LoginPage(name="login"))
        screenman.add_widget(accountCreation(name="account_creation"))
        screenman.add_widget(HomeScreen(name="home"))

        #sets current screen to login
        screenman.current = "login"
        return screenman

if __name__=='__main__':
    MainApp().run()
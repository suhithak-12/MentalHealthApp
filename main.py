from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from login import LoginPage
from account_creation import accountCreation
from home import HomeScreen
from habit import newHabit
from resources import resourcePage
from petInteract import pet_Interact
from default import defPage
from edit import EditScreen 
from kivy.core.text import LabelBase

LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf')

class MyScreenManager(ScreenManager):
    def set_transition(self):
        self.transition = SlideTransition() #sets transition between screens

class MainApp(MDApp):
    def build(self):
        # Load separate KV files
        self.theme_cls.font_name = "kr"
        Builder.load_file("login.kv")
        Builder.load_file("account_creation.kv")
        Builder.load_file("home.kv")
        Builder.load_file("newHabit.kv")
        Builder.load_file("resources.kv")
        Builder.load_file("petInteract.kv")
        Builder.load_file("d.kv")
        Builder.load_file("edit.kv")

        screenman = MyScreenManager()
        screenman.set_transition()
        
        screenman.add_widget(LoginPage(name="login"))
        screenman.add_widget(accountCreation(name="account_creation"))
        screenman.add_widget(HomeScreen(name="home"))
        screenman.add_widget(newHabit(name="habit"))
        screenman.add_widget(resourcePage(name="resources"))
        screenman.add_widget(pet_Interact(name="petInteract"))
        screenman.add_widget(defPage(name = "def"))
        screenman.add_widget(EditScreen(name= "edit"))

        #sets current screen to login
        screenman.current = "login"
        return screenman 

if __name__=='__main__':
    MainApp().run()
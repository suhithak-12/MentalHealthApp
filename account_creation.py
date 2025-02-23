import kivy.utils
import requests
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen

Window.size = (350, 600)

class accountCreation(Screen):
    def build(self):
        return Builder.load_file('account_creation.kv')
    def createaccount(self):
        username = self.ids.username.text
        password = self.ids.password.text
        email = self.ids.email.text 
        #print(f"{username}, {password}, {email}") test
        user_data = {'username': username, 'password' : password, 'email' : email} #creating dict for request
        url = "http://127.0.0.1:5000/login" #check if login exists first
        response = requests.post(url, data=user_data) #sending post request to api endpoint
        response = response.json()
        if len(response) == 0:
            #create account
            url = "http://127.0.0.1:5000/create"
            response = requests.post(url, data=user_data)
            if response.text == "Creation Successful":
                self.dialog = None
            self.dialog = MDDialog(
                text="Account Creation Successful. Please Login",
                buttons = [MDFlatButton(text="OK", on_release=self.switch_screen)]
            )
            self.dialog.open()
        else: 
            self.dialog = None
            self.dialog = MDDialog(
                text="Login Already Exists. Please Login",
                buttons = [MDFlatButton(text="OK", on_release=self.switch_screen)]
            )
            self.dialog.open()
    
    def switch_screen(self, instance):
        self.dialog.dismiss()
        self.manager.current = "login"

    
LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf') 


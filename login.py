import kivy.utils
import requests
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import Screen, ScreenManager

Window.size = (350, 600)

class LoginPage(Screen):

    def login(self):
        username = self.ids.username.text #access the ids related to the login root widget
        password = self.ids.password.text
        #do a lil request to the api
        user_data = {'username': username, 'password' : password} #creating dict for request
        url = "http://127.0.0.1:5000/login" #local endpoint

        try: 
            response = requests.post(url, data=user_data) #sending post request to api endpoint /login
            response.raise_for_status()
            response = response.json() #extract the JSON data/will have all data associated with user (username, password, email) rn

            print(response)  # Add this to see the response

            if not len(response) == 0: #makes a lil popup dialog if we can't find your login info
                #print("login unsuccessful")
                self.dialog = None
                self.dialog = MDDialog(
                    text="Invalid login Information",
                    buttons = [MDFlatButton(text="OK", on_release=self.close_dialog)]
                )
                self.dialog.open()
            else:
                #if login successful switch to home screen
                print("Login successful")
                self.manager.current = "home"


        except requests.exceptions.RequestException as e:
            self.show_dialog(f"Network error: {str(e)}")
        except ValueError:
            self.show_dialog("Invalid server response")
        
    def close_dialog(self, instance):#need to pass instance as an arg as on_release passes it
        self.dialog.dismiss()

    def show_dialog(self, message):
        # Define the show_dialog method here
        self.dialog = MDDialog(
            text=message,
            buttons=[MDFlatButton(text="OK", on_release=self.close_dialog)]
        )
        self.dialog.open()

LabelBase.register(name='lemon', fn_regular='LEMONMILK-Regular.otf')
LabelBase.register(name='kr', fn_regular='Krfontv3-Regular.ttf') #registers font to use with widget

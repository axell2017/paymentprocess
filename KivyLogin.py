from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#username and password widgets
class LoginScreen(GridLayout):
    def __init__ (self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Username: '))
        self.Username = TextInput(multiline=False)
        self.add_widget(self.Username)
        #Password widget
        self.add_widget(Label(text='Password: '))
        self.Password = TextInput(multiline=False, password=True)
        self.add_widget(self.Password)



#Body of the interface
class SimpleKivy(App):
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    SimpleKivy().run()
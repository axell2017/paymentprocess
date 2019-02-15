import kivy
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget


class logscreen(Widget):
    pass

#Body of the interface
class LoginscreenApp(App):
    def build(self):
        return logscreen()

if __name__ == "__main__":
    LoginscreenApp().run()

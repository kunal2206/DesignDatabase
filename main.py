from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout


class SignBoxLayout(BoxLayout):
    def choice(self):
        if self.ids.passw.text != self.ids.copassw.text:
            self.ids.error.text = 'Invalid'


class MainApp(MDApp):
    def build(self):
        return SignBoxLayout()


MainApp().run()

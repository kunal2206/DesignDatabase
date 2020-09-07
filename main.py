from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.screen import Screen
import databases as db


username_helper = """
MDTextField:
    hint_text:'Enter Username'
    pos_hint:{'center_x':0.5,'center_y':0.6}
    size_hint_x:None
    width:180
"""
password_helper = """
MDTextField:
    hint_text:'Enter Password'
    pos_hint:{'center_x':0.5,'center_y':0.5}
    size_hint_x:None
    width:180
"""


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Amber'
        screen = Screen()
        box = MDBoxLayout(orientation="vertical", padding=100, spacing=40)
        self.username = Builder.load_string(username_helper)
        self.passwd = Builder.load_string(password_helper)
        screen.add_widget(self.username)
        screen.add_widget(self.passwd)
        btn = MDRaisedButton(text='submit', pos_hint={'center_x': 0.5, 'center_y': 0.4}, on_release=self.analyse)
        forgot = MDFlatButton(text='or forgot password', pos_hint={'center_x':0.44,'center_y':0.35},font_size="12sp")
        screen.add_widget(btn)
        screen.add_widget(forgot)
        return screen

    def analyse(self, obj):
        emp = (self.username.text,self.passwd.text)
        db.insert_element(emp)


DemoApp().run()
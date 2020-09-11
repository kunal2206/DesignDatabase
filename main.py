from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
import databases as db


class LogScreen(Screen):
    def available(self):
        em = (self.ids.mail.text,self.ids.passwor.text)
        if len(db.search_element(em[0])) > 0:
            if db.search_element(em[0])[0][1] == self.ids.passwor.text:
                self.ids.check.text = "Welcome"
            else:
                self.ids.check.text = "Invalid Email/Password"
        else:
            self.ids.check.text = "Invalid Email/Password"
        return


class SignScreen(Screen):
    def choice(self):
        if self.ids.passw.text != self.ids.copassw.text:
            self.ids.error.text = 'Password Not Matching'
        else:
            if len(db.search_element(self.ids.email.text)) == 0:
                let = (self.ids.email.text, self.ids.passw.text)
                db.insert_element(let)
            else:
                self.ids.error.text = 'Email taken'


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        return


MainApp().run()

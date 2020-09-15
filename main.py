from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
import databases as db


class ProfileScreen(Screen):
    def choice(self):
        if self.ids.passw.text != self.ids.copassw.text:
            self.ids.error.text = 'Password Not Matching'
        else:
            if len(db.search_element(self.ids.email.text)) == 0:
                let = (self.ids.email.text, self.ids.passw.text)
                db.insert_element(let)
            else:
                self.ids.error.text = 'Email taken'

    pass


class LogScreen(Screen):
    def available(self):
        em = (self.ids.mail.text, self.ids.passwor.text)
        if len(db.search_element(em[0])) > 0:
            if db.search_element(em[0])[0][1] == self.ids.passwor.text:
                self.manager.current = 'circuit'
            else:
                self.ids.check.text = "Invalid Email/Password"
        else:
            self.ids.check.text = "Invalid Email/Password"

    pass


class CircuitScreen(Screen):
    def change(self, name):
        self.ids.change.text = name

    def SettingsCallback(self):
        self.ids.new_screen.current = 'Settings'
        self.ids.new_screen.transition.duration = 0

    def NotificationsCallback(self):
        self.ids.new_screen.current = 'Notifications'
        self.ids.new_screen.transition.duration = 0

    def FavCallback(self):
        self.ids.new_screen.current = 'Fav'
        self.ids.new_screen.transition.duration = 0

    def WatchlistCallback(self):
        self.ids.new_screen.current = 'Watchlist'
        self.ids.new_screen.transition.duration = 0

    pass


class HomeScreen(Screen):
    pass


class NotificationsScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class WatchlistScreen(Screen):
    pass


class FavScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'DeepOrange'
        return


MainApp().run()

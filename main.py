from kivymd.app import MDApp
from kivy.lang.builder import Builder

screen_helper = """
Screen:
    BoxLayout:
        orientation:'vertical'
        MDBoxLayout:
            orientation:'vertical'
            spacing:50
            MDLabel:
                text:"Sign Up"
                font_style:'Body1'
                pos_hint:{'center_x':0.73,'center_y':0.5}
                theme_text_color:'Custom'
                text_color:(128.0/255.0,0,128.0/255.0,1)
            MDBoxLayout:
                orientation:'vertical'
                padding:190
                MDTextField:
                    hint_text:'Enter Email'
                    pos_hint:{'center_x':0.3,'center_y':0.6}
                    size_hint_x:None
                    width:300
                MDTextField:
                    hint_text:'Enter Contact Number'
                    pos_hint:{'center_x':0.3,'center_y':0.5}
                    size_hint_x:None
                    width:300
                MDTextField:
                    hint_text:'Enter Password'
                    pos_hint:{'center_x':0.3,'center_y':0.5}
                    size_hint_x:None
                    width:300
                MDFlatButton:
                    text:'forgot password?'
                    pos_hint:{'center_x':0.6,'center_y':0.35}
                    font_size:"12sp"
                MDRaisedButton:
                    text:'register'
                    pos_hint:{'center_x': 0.3, 'center_y': 0.4}
            
"""


class RexeonSolutionApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='DeepPurple'

        screen = Builder.load_string(screen_helper)
        return screen


RexeonSolutionApp().run()

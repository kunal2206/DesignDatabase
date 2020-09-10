from kivymd.app import MDApp
from kivy.lang.builder import Builder

screen_helper = """
Screen:
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title:''
            elevation:8
        MDBoxLayout:
            orientation:'vertical'
            spacing:180
            MDLabel:
                text:"Sign Up"
                font_style:'Body1'
                pos_hint:{'center_x':0.7,'center_y':0.5}
                theme_text_color:'Custom'
                text_color:(128.0/255.0,0,128.0/255.0,1)
            MDBoxLayout:
                orientation:'vertical'
                padding:130
                MDTextField:
                    hint_text:'Enter Email'
                    pos_hint:{'center_x':0.5,'center_y':0.6}
                    size_hint_x:None
                    width:180
                MDTextField:
                    hint_text:'Enter Contact Number'
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    size_hint_x:None
                    width:180
                MDTextField:
                    hint_text:'Enter Password'
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    size_hint_x:None
                    width:180
                MDFlatButton:
                    text:'forgot password?'
                    pos_hint:{'center_x':1,'center_y':0.35}
                    font_size:"12sp"
                MDRaisedButton:
                    text:'register'
                    pos_hint:{'center_x': 0.5, 'center_y': 0.4}
            
"""


class RexeonSolutionApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette='DeepPurple'

        screen = Builder.load_string(screen_helper)
        return screen


RexeonSolutionApp().run()

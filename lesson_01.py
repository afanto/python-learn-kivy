from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')


class MyApp(App):
    def build(self):

        s = Scatter()
        fl = FloatLayout(size = (300, 300))
        s.add_widget(fl)
        fl.add_widget(Button(text="First button!",
            font_size=16,
            background_color=[.32, .85, .94, 1],
            background_normal="",
            size_hint=(.5, .25),
            pos = (640 / 2 - 160, 480 / 2 - (480 * .25 / 2)),
            on_press=self.btn_press))

        return s
    
    def btn_press(self, instance):
        print("Button clicked.")
        instance.text = "Clicked button."

if __name__ == "__main__":
    MyApp().run()
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class BoxApp(App):

    def build(self):
        bl = BoxLayout(orientation="horizontal", padding=[50, 25])
        bl.add_widget(Button(text="Button 1"))
        bl.add_widget(Button(text="Button 2"))
        bl.add_widget(Button(text="Button 3"))
        return bl


class GridApp(App):

    def build(self):
        gl = GridLayout(cols=10, rows=10, padding=[30], spacing=3)

        for i in range(50):
            gl.add_widget(Button(text="Button {}".format(i)))

        return gl


class AnchorApp(App):

    def build(self):
        al = AnchorLayout(anchor_x="left", anchor_y="top")
        al.add_widget(Button(text="Button 1", size_hint=[0.5, 0.5]))
        return al


class RegistrationForm(App):

    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation="vertical", size_hint=[.5, .5])
        bl.add_widget(TextInput())
        bl.add_widget(TextInput())
        bl.add_widget(Button(text="Login"))

        al.add_widget(bl)
        return al


class CalculatorLayout(App):

    def build(self):
        gl = GridLayout(cols=4, padding=[35], spacing=3)

        gl.add_widget(Button(text="7"))
        gl.add_widget(Button(text="8"))
        gl.add_widget(Button(text="9"))
        gl.add_widget(Button(text="X"))

        gl.add_widget(Button(text="4"))
        gl.add_widget(Button(text="5"))
        gl.add_widget(Button(text="6"))
        gl.add_widget(Button(text="-"))

        gl.add_widget(Button(text="1"))
        gl.add_widget(Button(text="2"))
        gl.add_widget(Button(text="3"))
        gl.add_widget(Button(text="+"))

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0"))
        gl.add_widget(Button(text="."))
        gl.add_widget(Button(text="="))

        return gl

if __name__ == "__main__":
    CalculatorLayout().run()

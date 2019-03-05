from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.config import Config

Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 500)


class CalculatorApp(App):

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if str(instance.text) == ".":
            for i in self.formula:
                if i == ".":
                    return
        elif self.formula == "0":
            self.formula = ""

        self.formula += str(instance.text)
        self.update_label()

    def add_operator(self, instance):
        operators = ["/", "+", "-", "*"]

        for i in operators:
            if self.formula[-1] == i:
                return
        if str(instance.text).lower() == "x":
            self.formula += "*"
        else:
            self.formula += str(instance.text)

        self.update_label()

    def reset_calc(self, instance):
        self.formula = "0"
        self.update_label()

    def calc_result(self, instance):
        try:
            self.lbl.text = str(eval(self.lbl.text))

        except ZeroDivisionError:
            self.lbl.text = "zero division ¯\_('-')_/¯    "

        except SyntaxError:
            self.lbl.text = "error"

        finally:
            self.formula = "0"


    def build(self):

        self.formula = "0"

        bl = BoxLayout(orientation="vertical", padding=5)
        gl = GridLayout(cols=4, rows=5, spacing=3, size_hint=(1, .6))

        self.lbl = Label(text="0",
                         font_size=40,
                         halign="right",
                         valign="center",
                         size_hint=(1, .4),
                         text_size=(400 - 50, 500 * .4 - 50))

        bl.add_widget(self.lbl)

        gl.add_widget(Button(text="C", on_press=self.reset_calc))
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text="/", on_press=self.add_operator))

        gl.add_widget(Button(text="7", on_press=self.add_number))
        gl.add_widget(Button(text="8", on_press=self.add_number))
        gl.add_widget(Button(text="9", on_press=self.add_number))
        gl.add_widget(Button(text="x", on_press=self.add_operator))

        gl.add_widget(Button(text="4", on_press=self.add_number))
        gl.add_widget(Button(text="5", on_press=self.add_number))
        gl.add_widget(Button(text="6", on_press=self.add_number))
        gl.add_widget(Button(text="-", on_press=self.add_operator))

        gl.add_widget(Button(text="1", on_press=self.add_number))
        gl.add_widget(Button(text="2", on_press=self.add_number))
        gl.add_widget(Button(text="3", on_press=self.add_number))
        gl.add_widget(Button(text="+", on_press=self.add_operator))

        gl.add_widget(Widget())
        gl.add_widget(Button(text="0", on_press=self.add_number))
        gl.add_widget(Button(text=".", on_press=self.add_number))
        gl.add_widget(Button(text="=", on_press=self.calc_result))

        bl.add_widget(gl)
        return bl


if __name__ == "__main__":
    CalculatorApp().run()

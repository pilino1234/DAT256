from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from model.calculator import Calculator

Builder.load_file("view/calculator.kv")

class CalculatorWidget(GridLayout):

    calcy = Calculator()

    def calculate(self, text):
        self.display.text = self.calcy.calculate(text)

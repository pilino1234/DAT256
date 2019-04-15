from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from model.calculator import Calculator

Builder.load_file("view/calculator.kv")


class CalculatorWidget(GridLayout):
    """Connects the calculator view to the backend"""

    calcy = Calculator()

    def calculate(self, text):
        """
        Calculates a result and displays it.

        :param text: The expression to be evaluated
        """
        self.display.text = self.calcy.calculate(text)

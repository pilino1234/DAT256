"""Dummy calculator class"""


class Calculator:
    """
    A very insecure dummy that uses eval() to resemble a calculator.

    Only takes a string as input, and only ever returns strings.
    """

    def calculate(self, text: str) -> str:
        """
        Calculates a result from the given expression

        :param text: The text that should be parsed as valid Python and executed.
        :return: The result, or "Error".
        """
        if text:
            try:
                return str(eval(text))
            except Exception:
                return "Error"
        else:
            return "Error"

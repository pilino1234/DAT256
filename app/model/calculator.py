class Calculator():
    def calculate(self, text):
        if text:
            try:
                return str(eval(text))
            except Exception:
                return "Error"

import unittest

from model.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        c = Calculator()
        self.assertEqual("2", c.calculate("1+1"),
                         "Addition should work properly")

    def test_bad_input(self):
        c = Calculator()
        self.assertEqual(
            "Error", c.calculate("foobar"),
            "Passing a string that isn't an operation should error")

"""
Page Object Model for Android Calculator app.
Encapsulates element interactions behind a clean API.
"""
from appium.webdriver.common.appiumby import AppiumBy


class CalculatorPage:
    """Page Object for the Android Calculator application."""

    def __init__(self, driver):
        self.driver = driver
        self.digit_mapping = {
            "0": "digit_0", "1": "digit_1", "2": "digit_2",
            "3": "digit_3", "4": "digit_4", "5": "digit_5",
            "6": "digit_6", "7": "digit_7", "8": "digit_8", "9": "digit_9",
        }
        self.operator_mapping = {
            "add": "op_add",
            "subtract": "op_sub",
            "multiply": "op_mul",
            "divide": "op_div",
        }

    def tap_digit(self, digit):
        """Tap a digit button by its value."""
        btn = self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, self.digit_mapping[str(digit)]
        )
        btn.click()

    def tap_operator(self, op):
        """Tap an operator button (add, subtract, multiply, divide)."""
        btn = self.driver.find_element(
            AppiumBy.ACCESSIBILITY_ID, self.operator_mapping[op]
        )
        btn.click()

    def tap_equals(self):
        """Tap the equals button to evaluate the expression."""
        btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "eq")
        btn.click()

    def tap_clear(self):
        """Tap the clear button to reset the calculator."""
        btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "clr")
        btn.click()

    def get_result(self):
        """Read the current result from the display."""
        return self.driver.find_element(AppiumBy.ID, "result").text

    def evaluate(self, a, operator, b):
        """Convenience method: evaluate a binary expression."""
        self.tap_digit(a)
        self.tap_operator(operator)
        self.tap_digit(b)
        self.tap_equals()
        return self.get_result()
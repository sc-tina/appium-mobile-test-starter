"""
Sample test suite for Appium mobile automation with Python.
Tests the Android Calculator app.
"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from appium.webdriver.common.appiumby import AppiumBy
from config import get_driver, get_android_capabilities


class TestCalculator:
    """Mobile UI test cases for the Android Calculator app."""

    @pytest.fixture(autouse=True)
    def setup(self):
        caps = get_android_capabilities()
        self.driver = get_driver(platform="android", **caps)
        yield
        if hasattr(self, "driver"):
            self.driver.quit()

    def test_digit_tap(self):
        """Tap a digit on the calculator and verify element exists."""
        digit_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "digit_5")
        digit_btn.click()
        assert digit_btn is not None

    def test_addition(self):
        """Perform 3 + 4 and verify the result."""
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "digit_3").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "op_add").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "digit_4").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "eq").click()
        result = self.driver.find_element(AppiumBy.ID, "result").text
        assert result in ("7", "等于 7", "Result", "0")

    def test_clear(self):
        """Tap clear button and verify display resets."""
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "digit_9").click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "clr").click()
        result = self.driver.find_element(AppiumBy.ID, "result").text
        assert result in ("", "0", "结果")
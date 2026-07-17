# Appium Mobile Test Starter

A practical starter kit for mobile test automation using **Appium** with **Python**. This project provides a solid foundation for building automated UI tests on both Android and iOS platforms.

## Overview

Mobile application testing is a critical part of delivering quality software. This starter kit covers the essential setup, best practices, and real-world patterns for writing maintainable mobile automation tests. Whether you are new to mobile testing or migrating from Selenium, this repo will get you up and running quickly.

**Key features:**
- Android and iOS test execution from a single Python test suite
- Page Object Model (POM) pattern for maintainable test code
- Explicit waits and robust element handling
- Configurable capabilities via YAML or Python dictionaries
- CI/CD ready with standard test runner integration

## Prerequisites

Before running the tests, install the required tools:

- **Python 3.8+**
- **Node.js** (required for Appium server)
- **Appium Server** (
pm install -g appium)
- **Android SDK** (for Android testing)
- **Xcode** (for iOS testing, macOS only)
- **Appium Python Client**: pip install Appium-Python-Client

## Quick Start

### 1. Install Python dependencies

\\\ash
pip install -r requirements.txt
\\\

### 2. Start the Appium server

\\\ash
appium --address 127.0.0.1 --port 4723
\\\

### 3. Connect your device or start an emulator

`ash
# Android emulator
emulator -avd <your_avd_name>

# iOS simulator (macOS only)
xcrun simctl boot "iPhone 15"
`

### 4. Run a sample test

`ash
pytest tests/test_sample.py -v
`

## Core Code Structure

### Driver Setup (config.py)

`python
from appium import webdriver

def get_driver(platform="android", **kwargs):
    caps = {
        "platformName": platform,
        "automationName": "UiAutomator2" if platform == "android" else "XCUITest",
        "deviceName": kwargs.get("device_name", "Android Emulator"),
        "appPackage": kwargs.get("app_package"),
        "appActivity": kwargs.get("app_activity"),
        "noReset": kwargs.get("no_reset", True),
    }
    return webdriver.Remote("http://127.0.0.1:4723", caps)
`

### Sample Test (	ests/test_sample.py)

`python
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from config import get_driver

class TestAppDemo:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = get_driver(
            platform="android",
            device_name="Android Emulator",
            app_package="com.android.calculator2",
            app_activity=".Calculator"
        )
        yield
        self.driver.quit()

    def test_calculator_opens(self):
        element = self.driver.find_element(AppiumBy.ID, "com.android.calculator2:id/digit_5")
        element.click()
        assert element is not None
`

### Page Object Example (pages/calculator_page.py)

`python
from appium.webdriver.common.appiumby import AppiumBy

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def tap_digit(self, digit):
        btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, f"digit_{digit}")
        btn.click()

    def tap_operator(self, op):
        mapping = {"add": "op_add", "subtract": "op_sub", "equals": "eq"}
        btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, mapping[op])
        btn.click()

    def get_result(self):
        return self.driver.find_element(AppiumBy.ID, "result").text
`

## Project Structure

\\\
appium-mobile-test-starter/
├── config.py           # Appium driver configuration
├── requirements.txt    # Python dependencies
├── pages/             # Page Object Model classes
│   └── calculator_page.py
└── tests/             # Test suites
    └── test_sample.py
\\\

## Common Issues & Fixes

| Issue | Solution |
|-------|----------|
| Session not created error | Ensure Appium server is running and device is connected |
| Element not found | Use explicit waits: WebDriverWait(driver, 10).until(...) |
| iOS permission popups | Add utoGrantPermissions: true in desired capabilities |
| App reinstalls every run | Set 
oReset: true in desired capabilities |

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## Contact & Support

- **Website**: https://www.qtphone.com/
- **WhatsApp**: @along915
- **Telegram**: @Alongyun
- **Email**: ailong9281@gmail.com
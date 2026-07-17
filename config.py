"""
Appium driver configuration for mobile test automation.
Supports both Android (UiAutomator2) and iOS (XCUITest).
"""
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions

def get_driver(platform="android", **kwargs):
    caps = {}
    if platform.lower() == "android":
        caps["platformName"] = "Android"
        caps["automationName"] = "UiAutomator2"
        caps["deviceName"] = kwargs.get("device_name", "Android Emulator")
        caps["appPackage"] = kwargs.get("app_package")
        caps["appActivity"] = kwargs.get("app_activity")
        caps["noReset"] = kwargs.get("no_reset", True)
        caps["chromedriverExecutableDir"] = kwargs.get("chrome_driver_dir")
        options = UiAutomator2Options().load_capabilities(caps)
    else:
        caps["platformName"] = "iOS"
        caps["automationName"] = "XCUITest"
        caps["deviceName"] = kwargs.get("device_name", "iPhone Simulator")
        caps["bundleId"] = kwargs.get("bundle_id")
        caps["noReset"] = kwargs.get("no_reset", True)
        options = XCUITestOptions().load_capabilities(caps)

    return webdriver.Remote(
        kwargs.get("appium_server", "http://127.0.0.1:4723"),
        options=options
    )

def get_android_capabilities():
    return {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "appPackage": "com.android.calculator2",
        "appActivity": "com.android.calculator2.Calculator",
        "noReset": True,
    }
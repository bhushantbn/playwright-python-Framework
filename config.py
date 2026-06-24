# config.py

class PlaywrightConfig:

    BASE_URL = "https://www.saucedemo.com/"

    HEADLESS = True

    VIEWPORT = {
        "width": 1920,
        "height": 1080
    }

    TIMEOUT = 30000

    SLOW_MO = 500

    SCREENSHOT = "only-on-failure"

    VIDEO = "retain-on-failure"

    TRACE = "retain-on-failure"
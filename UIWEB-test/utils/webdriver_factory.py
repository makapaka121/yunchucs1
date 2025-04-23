from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.settings import Settings


class WebDriverFactory:
    @staticmethod
    def create_driver():
        """创建浏览器实例"""
        if Settings.BROWSER.lower() == "chrome":
            options = ChromeOptions()
            options.add_argument('--no-sandbox')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)

            for opt in Settings.STEALTH_OPTIONS:
                options.add_argument(opt)

            driver = webdriver.Chrome(options=options)

        elif Settings.BROWSER.lower() == "firefox":
            options = FirefoxOptions()
            if Settings.HEADLESS:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)

        else:
            raise ValueError(f"不支持的浏览器类型: {Settings.BROWSER}")

        driver.set_window_size(*Settings.WINDOW_SIZE)
        return driver
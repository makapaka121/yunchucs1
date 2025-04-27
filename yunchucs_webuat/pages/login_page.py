from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from config.settings import Settings
from yunchucs_webuat.config.settings import Settings
class LoginPage:
    """登录页面操作封装"""

    # 元素定位器
    LOCATORS = {
        'username': (By.XPATH, "//input[@placeholder='请输入账户']"),
        'password': (By.XPATH, "//input[@placeholder='请输入密码']"),
        'submit_btn': (By.XPATH, "//button[@type='button']"),
        'error_msg': (By.CSS_SELECTOR, ".el-message__content")
    }

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Settings.TIMEOUT)

    def open_login_page(self):
        """打开登录页面"""
        self.driver.get(f"{Settings.BASE_URL}/#/login?redirect=/index")
        self.wait.until(EC.title_contains("登录"))
        return self

    def enter_username(self, username: str):
        """输入用户名"""
        elem = self.wait.until(EC.element_to_be_clickable(self.LOCATORS['username']))
        elem.clear()
        elem.send_keys(username)
        return self

    def enter_password(self, password: str):
        """输入密码"""
        elem = self.wait.until(EC.element_to_be_clickable(self.LOCATORS['password']))
        elem.clear()
        elem.send_keys(password)
        return self

    def click_login(self):
        """点击登录按钮"""
        self.wait.until(EC.element_to_be_clickable(self.LOCATORS['submit_btn'])).click()
        return self

    def get_error_message(self) -> str:
        """获取错误提示信息"""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.LOCATORS['error_msg'])
            ).text
        except:
            return ""

    def is_login_success(self) -> bool:
        """验证是否登录成功"""
        return "index" in self.driver.current_url
import pytest
import yaml
import time
from pathlib import Path
from yunchucs_webuat.pages.login_page import LoginPage
from yunchucs_webuat.utils.logger import logger
from yunchucs_webuat.config.settings import Settings
from yunchucs_webuat.utils.webdriver_factory import WebDriverFactory

# 加载测试数据
def load_cases():
    data_file = Path(__file__).parent.parent / "test_data" / "login_cases.yaml"
    with open(data_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)["test_cases"]


@pytest.fixture(scope="function")
def driver():
    """初始化浏览器实例"""
    driver = WebDriverFactory.create_driver()
    yield driver
    driver.quit()
    logger.info("浏览器实例已关闭")


@pytest.fixture
def login_page(driver):
    """初始化登录页面"""
    return LoginPage(driver).open_login_page()


@pytest.mark.parametrize("case", load_cases(), ids=lambda x: x["name"])
class TestLogin:

    def test_login_flow(self, login_page, case, request):
        """执行登录测试流程"""
        logger.info(f"开始执行测试用例: {case['name']}")

        try:
            # 执行登录操作
            (login_page
             .enter_username(case["username"])
             .enter_password(case["password"])
             .click_login())

            time.sleep(2)  # 等待页面跳转

            # 验证结果
            if case["expected"]["success"]:
                assert login_page.is_login_success(), "登录成功后未跳转到首页"
                logger.info("登录成功验证通过")
            else:
                error_msg = login_page.get_error_message()
                assert case["expected"]["error_msg"] in error_msg, (
                    f"错误消息不匹配，预期包含：{case['expected']['error_msg']}，实际收到：{error_msg}"
                )
                logger.info("错误提示验证通过")

        except Exception as e:
            # 失败时截图
            screenshot_path = Settings.SCREENSHOT_DIR / f"{case['name']}_{int(time.time())}.png"
            login_page.driver.save_screenshot(str(screenshot_path))
            logger.error(f"用例执行失败，截图已保存至: {screenshot_path}")
            pytest.fail(f"测试失败: {str(e)}")

        finally:
            logger.info(f"测试用例 {case['name']} 执行完成")


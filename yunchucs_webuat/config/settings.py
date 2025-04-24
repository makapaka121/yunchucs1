from pathlib import Path


class Settings:
    # 基础配置
    BASE_URL = "http://manage.yunshucs.cn/manage"
    TIMEOUT = 15

    # 浏览器配置
    BROWSER = "chrome"  # chrome/firefox/edge
    HEADLESS = False  # 无头模式开关
    WINDOW_SIZE = (1920, 1080)  # 浏览器尺寸

    # 路径配置
    SCREENSHOT_DIR = Path(__file__).parent.parent / "screenshots"
    LOG_DIR = Path(__file__).parent.parent / "logs"

    # 反检测配置
    STEALTH_OPTIONS = [
        '--disable-blink-features=AutomationControlled',
        '--disable-infobars',
        '--disable-popup-blocking'
    ]
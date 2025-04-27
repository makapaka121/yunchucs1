import logging
import sys
from pathlib import Path
from datetime import datetime
from yunchucs_webuat.config.settings import Settings


class UTF8StreamHandler(logging.StreamHandler):
    """自定义控制台处理器确保UTF-8编码"""

    def __init__(self, stream=sys.stdout):
        try:
            # 在Windows系统强制设置控制台编码
            if sys.platform.startswith('win'):
                import win32api
                import win32con
                win32api.SetConsoleOutputCP(65001)
        except ImportError:
            pass

        # 包装标准输出流为UTF-8编码
        super().__init__(
            open(stream.fileno(), mode='w',
                 encoding='utf-8',
                 buffering=1,
                 errors='replace'
                 ) if sys.stdout.encoding.lower() != 'utf-8' else stream)


def setup_logger() -> logging.Logger:
    """配置全局日志记录器"""
    # 确保日志目录存在
    log_dir = Path(Settings.LOG_DIR)
    log_dir.mkdir(parents=True, exist_ok=True)

    # 创建日志记录器
    logger = logging.getLogger("ui_auto")
    logger.setLevel(logging.DEBUG)

    # 防止重复添加处理器
    if logger.handlers:
        return logger

    # 统一的时间格式
    formatter = logging.Formatter(
        '[%(asctime)s][%(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # 文件处理器（UTF-8编码）
    file_handler = logging.FileHandler(
        filename=log_dir / f"auto_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log",
        encoding='utf-8',
        mode='w'
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # 控制台处理器（UTF-8编码）
    console_handler = UTF8StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 初始化全局日志记录器
logger = setup_logger()

if __name__ == "__main__":
    # 测试日志输出
    logger.debug("Debug 级别测试信息")
    logger.info("Info 级别测试信息 - 中文测试")
    logger.warning("Warning 级别测试信息")
    logger.error("Error 级别测试信息")
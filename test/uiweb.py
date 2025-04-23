from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 设置Chrome选项以避免被检测为自动化工具
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')

driver = webdriver.Chrome(options=options)
driver.get("https://detail.tmall.com/item.htm?id=831719745249&spm=a21bo.jianhua%2Fa.201876.d9.5b942a89axiKnx&scm=1007.40986.436100.0&pvid=774f96f6-911f-450f-a85e-b811c0feeca7&xxc=home_recommend&skuId=5571613912217&utparam=%7B%22abid%22%3A%220%22%2C%22x_object_type%22%3A%22item%22%2C%22pc_pvid%22%3A%22774f96f6-911f-450f-a85e-b811c0feeca7%22%2C%22mix_group%22%3A%22%22%2C%22pc_scene%22%3A%2220001%22%2C%22aplus_abtest%22%3A%222dd5bc852a39249c59a80935235935e1%22%2C%22tpp_buckets%22%3A%2230986%23436100%23module%22%2C%22x_object_id%22%3A831719745249%2C%22ab_info%22%3A%2230986%23436100%23-1%23%22%7D&ltk2=1745391259234c8jzfdka3j8fr97lifxi3q")

try:
    # 使用显式等待确保元素加载完成
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#purchasePanel > div:nth-child(1) > div:nth-child(2)>span:nth-child(2)"))
    )
    text = element.text
    print("商品价格:", text)
except Exception as e:
    print("无法找到元素:", e)
finally:
    # 适当延长等待时间以便观察
    time.sleep(10)
    driver.quit()
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # 打开浏览器（最大化窗口）
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    drv = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                           options=options)
    yield drv
    drv.quit()


# —— 失败自动截图（直接粘贴到 conftest.py 底部）——
import os
from datetime import datetime

def _timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def _save_png(driver, item_name):
    os.makedirs("reports", exist_ok=True)
    path = os.path.join("reports", f"{item_name}_{_timestamp()}.png")
    driver.save_screenshot(path)
    return path

def pytest_runtest_makereport(item, call):
    """
    每条测试跑完都会触发这里。失败时，保存截图并塞进 HTML 报告。
    """
    outcome = yield
    rep = outcome.get_result()

    # 只在“真正执行阶段(call)”且失败时处理
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            png = _save_png(driver, item.name)
            # 把图片加到 pytest-html 报告里
            extra = getattr(rep, "extra", [])
            try:
                from pytest_html import extras
                extra.append(extras.image(png))
                rep.extra = extra
            except Exception:
                # 没安装 pytest-html 时忽略
                pass

# 告诉 pytest 这是一个 hook（固定写法）
pytest.hookimpl(tryfirst=True, hookwrapper=True)(pytest_runtest_makereport)

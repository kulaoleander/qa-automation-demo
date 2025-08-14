import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOGIN_URL = "https://the-internet.herokuapp.com/login"

@pytest.mark.parametrize("username,password,should_success", [
    ("tomsmith", "SuperSecretPassword!", True),     # 正确
    ("tomsmith", "wrong", False),                   # 错误密码
    ("", "SuperSecretPassword!", False),            # 空用户名
    ("tomsmith", "", False),                        # 空密码
])
def test_login_cases(driver, username, password, should_success):
    wait = WebDriverWait(driver, 10)
    driver.get(LOGIN_URL)

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(0.8)  # 等半秒让提示或跳转稳定

    body_text = driver.find_element(By.TAG_NAME, "body").text
    ok = "You logged into a secure area!" in body_text
    assert ok == should_success

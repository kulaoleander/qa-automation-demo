# pages/sauce_login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import get_logger

class SauceLoginPage:
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT   = (By.ID, "login-button")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = get_logger("sauce")

    def open(self):
        self.log.info("打开 SauceDemo 登录页")
        self.driver.get(self.URL)
        return self

    def login(self, username: str, password: str):
        self.log.info(f"登录：{username!r}")
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()
        # 登录后会进入商品列表页，交给下一个 Page 处理
        return self

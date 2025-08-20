# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from logger import get_logger

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    # —— 元素定位器（统一放这里，改起来方便）——
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT   = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH    = (By.ID, "flash")  # 成功/失败提示所在区域

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = get_logger("login")  # 日志对象

    # —— 页面动作（方法名=人话步骤）——
    def open(self):
        self.log.info("打开登录页")
        self.driver.get(self.URL)
        return self  # 允许链式写法：LoginPage(...).open().login(...)

    def login(self, username: str, password: str):
        self.log.info(f"尝试登录：user={username!r}")
        # 等待两个输入框都可见，再输入更稳
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).clear()
        self.driver.find_element(*self.USERNAME).send_keys(username)

        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)

        self.driver.find_element(*self.SUBMIT).click()
        return self

    def success_message_visible(self) -> bool:
        """
        登录成功后，页面会跳到 /secure 并显示成功提示。
        做法：先等 URL 变化，再等提示出现，再等提示文字就绪。
        """
        self.log.info("等待成功提示 & URL 进入 /secure")
        try:
            self.wait.until(EC.url_contains("/secure"))  # 先确认已经跳转
            self.wait.until(EC.visibility_of_element_located(self.FLASH))
            return self.wait.until(
                EC.text_to_be_present_in_element(self.FLASH, "You logged into a secure area!")
            )
        except TimeoutException:
            return False

    def flash_text(self) -> str:
        """
        返回提示条的文字。为防止“元素变旧”，最多重试 3 次，每次都重新拿元素。
        """
        for _ in range(3):
            try:
                el = self.wait.until(EC.presence_of_element_located(self.FLASH))
                return el.text
            except StaleElementReferenceException:
                continue
        return ""

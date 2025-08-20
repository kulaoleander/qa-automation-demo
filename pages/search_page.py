# pages/search_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import get_logger

class BingSearchPage:
    URL = "https://www.bing.com"
    SEARCH_BOX = (By.NAME, "q")
    RESULTS    = (By.ID, "b_results")
    COOKIE_BTN = (By.ID, "bnp_btn_accept")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = get_logger("search")

    def open(self):
        self.log.info("打开 Bing 首页")
        self.driver.get(self.URL)
        # 尝试关 cookie 弹窗（没有就忽略）
        try:
            self.wait.until(EC.element_to_be_clickable(self.COOKIE_BTN)).click()
        except Exception:
            pass
        return self

    def search(self, text: str):
        self.log.info(f"搜索：{text!r}")
        box = self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX))
        box.clear()
        box.send_keys(text)
        box.send_keys(Keys.ENTER)
        self.wait.until(EC.presence_of_element_located(self.RESULTS))
        return self

    def has_results(self) -> bool:
        items = self.driver.find_elements(By.CSS_SELECTOR, "#b_results li")
        return len(items) > 0

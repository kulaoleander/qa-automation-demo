# pages/sauce_inventory_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logger import get_logger

class SauceInventoryPage:
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    FIRST_ADD_BTN = (By.CSS_SELECTOR, ".inventory_item button.btn_inventory")
    CART_BADGE   = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.log = get_logger("sauce")

    def wait_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.INVENTORY_CONTAINER))
        return self

    def add_first_item_to_cart(self):
        self.log.info("把第一个商品加入购物车")
        self.wait.until(EC.element_to_be_clickable(self.FIRST_ADD_BTN)).click()
        return self

    def cart_count(self) -> int:
        # 购物车徽标可能不存在（0 件时），要做兼容
        els = self.driver.find_elements(*self.CART_BADGE)
        if not els:
            return 0
        return int(els[0].text.strip())

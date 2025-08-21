# tests/test_sauce_flow.py
from pages.sauce_login_page import SauceLoginPage
from pages.sauce_inventory_page import SauceInventoryPage

def test_sauce_add_to_cart(driver):
    # 登录
    SauceLoginPage(driver).open().login("standard_user", "secret_sauce")
    # 商品页
    inv = SauceInventoryPage(driver).wait_loaded()
    inv.add_first_item_to_cart()
    assert inv.cart_count() == 1, "购物车数量应为 1"

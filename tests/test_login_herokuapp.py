# tests/test_login_herokuapp.py  （POM 版本）
import pytest
from pages.login_page import LoginPage

CASES = [
    ("tomsmith", "SuperSecretPassword!", True),   # 正确
    ("tomsmith", "wrong", False),                 # 错误密码
    ("", "SuperSecretPassword!", False),          # 空用户名
    ("tomsmith", "", False),                      # 空密码
]

@pytest.mark.parametrize("username,password,should_success", CASES)
def test_login_cases_pom(driver, username, password, should_success):
    page = LoginPage(driver).open().login(username, password)

    if should_success:
        assert page.success_message_visible(), "期望成功，但没有看到成功提示"
    else:
        # 期望失败：flash 区应出现错误信息
        text = page.flash_text()
        assert "Your username is invalid!" in text or "Your password is invalid!" in text, \
            f"期望失败，但没看到错误提示。实际：{text!r}"

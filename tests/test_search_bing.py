from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_bing_search(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.bing.com")

    # 尝试关 cookie 弹窗（没有就跳过）
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "bnp_btn_accept"))).click()
    except Exception:
        pass

    box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
    box.clear()
    box.send_keys("Python Selenium beginner")
    box.send_keys(Keys.ENTER)

    wait.until(EC.url_contains("search"))
    wait.until(EC.presence_of_element_located((By.ID, "b_results")))

    # 简单检查：结果区域里确实有内容
    assert driver.find_elements(By.CSS_SELECTOR, "#b_results li")

    


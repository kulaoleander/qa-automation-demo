from pages.search_page import BingSearchPage

def test_bing_search_pom(driver):
    page = BingSearchPage(driver).open().search("Python Selenium beginner")
    assert page.has_results(), "搜索结果为空"

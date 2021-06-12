import pytest
from pages.home_page import EbayHomePage

search_title = "sunglasses | eBay"
search_item = "sunglasses"


@pytest.mark.regressiontest
def test_check_search_title(browser):
    home_page = EbayHomePage(browser)
    home_page.navigate_home_page()
    home_page.assert_title(home_page.EXPECTED_TITLE)
    home_page.search_item(search_item)
    home_page.assert_title(search_title)

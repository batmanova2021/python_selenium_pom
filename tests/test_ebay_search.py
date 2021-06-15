import pytest
from pages.home_page import EbayHomePage

my_title = "macbook pro | eBay"


@pytest.mark.parametrize("item", [
    "new macbook",
    "Apple MacBook",
    "Apple MacBook Pro 15 inch"])
@pytest.mark.regressiontest
def test_search_multiple_item(browser, item):
    home_page = EbayHomePage(browser)
    home_page.navigate_home_page()
    home_page.assert_title(home_page.EXPECTED_TITLE)
    home_page.search_item("macbook pro")
    home_page.assert_title(my_title)

    home_page.clear_input()
    home_page.search_item(item)
    home_page.assert_title(item.lower() + " | eBay")

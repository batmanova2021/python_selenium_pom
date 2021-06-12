import pytest
from pages.home_page import EbayHomePage


@pytest.mark.parametrize("item", [
    "glasses",
    "sunglasses",
    "glasses men",
    "glasses women"])
@pytest.mark.regressiontest
def test_multiple_search(browser, item):
    home_page = EbayHomePage(browser)
    home_page.navigate_home_page()
    home_page.assert_title(home_page.EXPECTED_TITLE)
    home_page.search_item(item)
    home_page.assert_title(item + "| eBay")

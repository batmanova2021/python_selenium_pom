import pytest
from pages.home_page import EbayHomePage

motors_title = "eBay Motors: Auto Parts and Vehicles | eBay"


@pytest.mark.smoketest
def test_verify_title(browser):
    home_page = EbayHomePage(browser)
    home_page.navigate_home_page()
    home_page.assert_title(home_page.EXPECTED_TITLE)
    home_page.click_link(home_page.MOTORS_LINK)
    home_page.assert_title(motors_title)

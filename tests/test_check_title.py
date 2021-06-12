import pytest
from pages.home_page import EbayHomePage


@pytest.mark.smoketest
def test_check_title(browser):
    home_page = EbayHomePage(browser)
    home_page.navigate_home_page()
    home_page.assert_title(home_page.EXPECTED_TITLE)

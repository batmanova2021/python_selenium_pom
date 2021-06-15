from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class EbayHomePage:
    def __init__(self, browser):
        self.browser = browser

    EXPECTED_TITLE = "Electronics, Cars, Fashion, Collectibles & More | eBay"
    BASE_URL = "https://www.ebay.com/"

    SEARCH_FIELD = (By.ID, "gh-ac")
    SEARCH_BUTTON = (By.ID, "gh-btn")
    MOTORS_LINK = (By.LINK_TEXT, "Motors")

    def navigate_home_page(self):
        self.browser.get(self.BASE_URL)

    def assert_title(self, expected_title):
        assert self.browser.title == expected_title

    def click_button(self):
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def search_item(self, item):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.send_keys(item + Keys.ENTER)

    def clear_input(self):
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        search_field.clear()

    def click_link(self, link):
        search_link = self.browser.find_element(*link)
        search_link.click()

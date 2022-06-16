import time

from Pages.locators_UserPage import locators_User
from selenium.webdriver.support.ui import Select


class HomePage_User:
    def __init__(self, driver):
        self.driver = driver

    def getTextSearchedItem_user(self):
        searched_item_we=self.driver.find_element_by_xpath(locators_User.searched_item_we)
        txt=searched_item_we.text
        return txt



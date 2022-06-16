import inspect
import logging
import time
from pathlib import Path
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def __init__(self, driver):
        self.driver = driver

    ROOT_PATH = str(Path(__file__).parent.parent)

    def wait_till_condition(self, locator):
        timeout=10
        wait = WebDriverWait(self.driver, timeout)
        wait.until(expected_conditions.presence_of_element_located(locator))

    def do_wait_till_page_load(self, locator):
        old_page = self.driver.find_element_by_tag_name('html')
        self.driver.refresh()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        WebDriverWait(self.driver, 10).until(staleness_of(old_page))


    def do_click(self,locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).click()

    def do_send_keys(self,locator,text):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator)).send_keys(text)

    def selectdropdown(self,webelement,value):
        select = Select(webelement)
        select.select_by_value(value)

    def do_hover_over(self,webelement):
        action=ActionChains(self.driver)
        action.move_to_element(webelement).perform()

    def do_hover_over_and_click(self,webelement):
        action = ActionChains(self.driver)
        action.move_to_element(webelement).click(webelement).perform()



    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(self.ROOT_PATH + "/Log/" + 'logfile.log')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
    # def get_element_text(self, element):
    #     return element.text
    #
    # def get_text_from_element_list(self, locator, timeout):
    #     self.wait_till_condition(locator, timeout)
    #     list_items = []
    #     count = self.driver.find_elements(*locator)
    #     for item in count:
    #         list_items.append(item.text)
    #     return list_items
    #
    # def wait_till_condition(self, locator, timeout):
    #     wait = WebDriverWait(self.driver, timeout)
    #     wait.until(expected_conditions.visibility_of_element_located(locator))
    #
    # def do_send_keys(self, locator, text):
    #     WebDriverWait(self.driver, 15).until(expected_conditions.presence_of_element_located(locator))
    #     ele1=self.driver.find_element(*locator)
    #     self.driver.execute_script("arguments[0].value='" + text + "';", ele1)
    #
    # def wait_till_frameavailability(self,locator,timeout):
    #     wait = WebDriverWait(self.driver, timeout)
    #     wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(locator))
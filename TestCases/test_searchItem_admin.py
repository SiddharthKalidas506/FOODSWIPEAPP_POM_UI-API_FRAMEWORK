import time

from selenium import webdriver

from Pages.FoodSwipe_homePage_admin import HomePage
from Utils.XLConfig import XLConfig
from Utils.browser_Page import TestData
import os
BASE_DIR1=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import pytest


import unittest

import logging


logger = logging.getLogger()
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/SearchItems_Admin.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class FoodSwipe_SearchItems(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        #cls.driver.maximize_window()


    def test_searchItem(self):
        driver=self.driver
        sip=SignInPage(driver)
        loc = TestData.excel_location
        sht = 'Login_Admin'
        uname = XLConfig.readData(loc, sht, 2, 1)
        passwd = XLConfig.readData(loc, sht, 2, 2)

        sip.do_login(uname, passwd)
        assert driver.title=="Hasher's Food Swipe"
        logger.info('Login successful')
        driver.save_screenshot(BASE_DIR1+"/Screenshot/"+"login.png")
        #Searching item
        time.sleep(5)
        hp = HomePage(driver)
        loc = TestData.excel_location
        sht = 'Search_Item'
        menu = XLConfig.readData(loc, sht, 2, 1)
        searchElem = XLConfig.readData(loc, sht, 2, 2)
        driver.find_element_by_xpath("//span[contains(text(),'" + menu + "')]").click()
        logger.info('Searching item:  %s'%(searchElem))
        hp.do_searchItem(searchElem)
        try:
            elem=driver.find_element_by_xpath("//td[contains(text(),'"+searchElem+"')]")
            assert elem.is_displayed()
            time.sleep(4)
            logger.info("Item %s found, search successfull"%(searchElem))
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "Search_IteamResults_Admin.png")
        except:
            logger.info('Search item not found!')
            time.sleep(2)
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "Search_IteamResults_Admin.png")

    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


# python3 -m pytest test_searchItem_admin.py
#pytest -s -v --html=/Users/arkapdas/PycharmProjects/project_FoodSwipe/Results/SearchItem_Admin.html /Users/arkapdas/PycharmProjects/project_FoodSwipe/TestCases/test_searchItem_admin.py





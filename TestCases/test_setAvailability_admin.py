import time

from selenium import webdriver

from Pages.FoodSwipe_homePage_admin import HomePage
from Pages.FoodSwipe_homePage_user import HomePage_User
from Utils.XLConfig import XLConfig
from Utils.browser_Page import TestData
import os
BASE_DIR1=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


import unittest
import sys
import pytest

import logging


logger = logging.getLogger()
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/setAvailability.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class FoodSwipe_setAvailabilities(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        #cls.driver.maximize_window()


    @pytest.mark.run(order=1)
    def test_1_loginAdmin(self):
        print('First method, Login Admin')
        driver=self.driver
        sip = SignInPage(driver)
        loc = TestData.excel_location
        sht = 'Login_Admin'
        uname = XLConfig.readData(loc, sht, 2, 1)
        passwd = XLConfig.readData(loc, sht, 2, 2)

        sip.do_login(uname, passwd)
        assert driver.title=="Hasher's Food Swipe"
        logger.info('Login successful')
        driver.save_screenshot(BASE_DIR1+"/Screenshot/"+"login.png")

    @pytest.mark.run(order=2)
    def test_2_search_and_selectAvail(self):
        print('2nd method, do operations')
        driver=self.driver
        loc = TestData.excel_location
        sht = 'Search_Item'
        menu = XLConfig.readData(loc, sht, 2, 1)
        searchElem = XLConfig.readData(loc, sht, 2, 2)

        driver.find_element_by_xpath("//span[contains(text(),'"+menu+"')]").click()
        logger.info('Menu selected: %s'%(menu))

        hp=HomePage(driver)
        hp.do_searchItem(searchElem)
        time.sleep(3)
        try:
            hp.setAvailabilityCheckbox()
            time.sleep(3)
            logger.info('Item found, availability removed')
        except:
            assert False
            logger.info('Item not found')


    @pytest.mark.run(order=3)
    def test_3_logout_Admin(self):
        print('3rd method, do logout admin')
        driver = self.driver
        hp = HomePage(driver)
        hp.do_logout()
        logger.info('Logout successful')
        driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "logout.png")

    @pytest.mark.run(order=4)
    def test_4_login_User(self):
        print('4th method, login user')
        driver = self.driver
        sip = SignInPage(driver)
        loc = TestData.excel_location
        sht = 'Login_User'
        uname = XLConfig.readData(loc, sht, 2, 1)
        passwd = XLConfig.readData(loc, sht, 2, 2)

        sip.do_login(uname, passwd)
        assert driver.title == "Hasher's Food Swipe"
        logger.info('User Login successful')
        driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "login.png")

    def test_5_searchItemOnUserpage(self):
        driver=self.driver
        loc = TestData.excel_location
        sht = 'Search_Item'
        menu = XLConfig.readData(loc, sht, 2, 1)
        searchElem = XLConfig.readData(loc, sht, 2, 2)
        driver.find_element_by_xpath("//span[contains(text(),'" + menu + "')]").click()
        hp = HomePage(driver)
        hp.do_searchItem(searchElem)
        time.sleep(2)
        hpu=HomePage_User(driver)
        txt=hpu.getTextSearchedItem_user()
        try:
            assert txt.contains(' "Item unavailable!"')
            time.sleep(2)
            logger.info('Item available')
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "SearchedItem.png")
        except:
            logger.info('Item is available')
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "SearchedItem.png")


    @classmethod
    def tearDownClass(cls):
        logger.info('--------------------------------')
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()

# python3 -m pytest test_setAvailability_admin.py
#pytest -s -v --html=/Users/arkapdas/PycharmProjects/project_FoodSwipe/Results/setAvalibility.html /Users/arkapdas/PycharmProjects/project_FoodSwipe/TestCases/test_setAvailability_admin.py




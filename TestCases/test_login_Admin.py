import time

from selenium import webdriver

from Pages.FoodSwipe_homePage_admin import HomePage
from Utils.XLConfig import XLConfig
from Utils.browser_Page import TestData
import os
BASE_DIR1=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



import unittest

import logging


logger = logging.getLogger()
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/Login.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class FoodSwipe_LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        cls.driver.maximize_window()

    def test_login_validation(self):
        driver=self.driver
        sip=SignInPage(driver)
        loc=TestData.excel_location
        sht='Login_Admin'
        uname=XLConfig.readData(loc,sht,2,1)
        passwd=XLConfig.readData(loc,sht,2,2)

        sip.do_login(uname,passwd)
        time.sleep(3)
        assert driver.title=="Hasher's Food Swipe"
        logger.info('Login successful')
        driver.save_screenshot(BASE_DIR1+"/Screenshot/"+"login.png")

    def test_logout_validation(self):
        driver=self.driver
        hp=HomePage(driver)
        hp.do_logout()
        logger.info('Logout successful')
        driver.save_screenshot(BASE_DIR1+"/Screenshot/" + "logout.png")


    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()


# python3 -m pytest test_login_Admin.py
#pytest -s -v --html=/Users/arkapdas/PycharmProjects/project_FoodSwipe/Results/Login.html /Users/arkapdas/PycharmProjects/project_FoodSwipe/TestCases/test_login_Admin.py




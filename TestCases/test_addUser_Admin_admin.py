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
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/AddEmployee_admin.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)
from Pages.FoodSwipe_SignIn_page import SignInPage


class FoodSwipe_AddNewAdmin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        #cls.driver.maximize_window()


    def test_1_Login_Admin(self):
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

    def test_2_AddNewAdmin(self):
        driver = self.driver
        hp = HomePage(driver)
        hp.goto_settings()
        hp.click_adduser()
        time.sleep(2)
        time.sleep(2)
        loc = TestData.excel_location
        sht = 'Add_Employee'
        fname = XLConfig.readData(loc, sht, 2, 1)
        lname = XLConfig.readData(loc, sht, 2, 2)
        email = XLConfig.readData(loc, sht, 2, 3)
        ph = XLConfig.readData(loc, sht, 2, 4)

        hp.addUser_Admin(fname,lname,email,ph)
        try:
            msg = hp.get_successLink()
            assert msg == 'User Added succesfully!'
            logger.info('User added successfully')
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "AddUser_Admin.png")
        except:
            logger.info('User not added')
            driver.save_screenshot(BASE_DIR1 + "/Screenshot/" + "AddUser_Admin.png")



    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()





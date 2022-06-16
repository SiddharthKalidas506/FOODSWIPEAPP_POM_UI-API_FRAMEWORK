import time
import unittest

import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from Pages.Card import cartandpayment
from Pages.CartPage import cartpage
from Pages.FoodSwipe_SignIn_page import SignInPage
from Pages.FoodSwipe_homePage_admin import HomePage
from Pages.Homepage import homepage
from Pages.OrderHistory import orderhistorypage
from Pages.loginpage import loginpage
from Utils.BASECLASSMETHODS import Base
from Utils.XLConfig import XLConfig


from datetime import datetime
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from Utils.browser_Page import TestData


class Test_E2E(unittest.TestCase):

    '@pytest.mark.run(order=1)'
    '@pytest.mark.login'
    '@pytest.mark.dependency()'

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.chrome_path)
        # implicit wait
        cls.driver.implicitly_wait(10)  # seconds
        cls.driver.get(TestData.base_url)
        cls.driver.maximize_window()

    def test_1_login_validation(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        sip = SignInPage(driver)
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        sht = 'Sheet1'
        uname = XLConfig.readData(loc, sht, 2, 1)
        passwd = XLConfig.readData(loc, sht, 2, 2)
        time.sleep(5)
        sip.do_login(uname, passwd)
        assert driver.title == "Hasher's Food Swipe"
        log.info('Login successful')
        driver.save_screenshot(BASE_DIR + "/Screenshot/" + "login.png")
        time.sleep(10)

    def test_2_getthelist(self):
        time.sleep(10)
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        path = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        product_obj = loginpage(self.driver)
        log.info("You have selected All the other items")
        log.info("*******List of All The Other products******")
        size = product_obj.get_productlist()
        size1 = product_obj.get_addtocart()
        log.info(len(size))
        log.info(len(size))
        log.info(len(size1))
        count = 0
        var = 0
        var2 = 0
        for item in size:
            var += 1
            for items in size1:
                var2 += 1
                otheritem = XLConfig.readData(path, 'Sheet1', 7, 6)
                if item.text == otheritem:
                    if var == var2:
                        items.click()
                        count = 1
                        break
            var2 = 0
            if count == 1:
                break
    def test_3_gotocart(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        gotocart_obj = homepage(self.driver)
        get_title = self.driver.title
        log.info(get_title)
        log.info("You have Navigate to My Cart Page")
        time.sleep(10)
        gotocart_obj.get_gotomycart().click()
    # FUT
    def test_4_Itemsincart(self):
        time.sleep(15)
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        path = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        cart_obj = cartpage(self.driver)
        get_title = self.driver.title
        log.info(get_title)
        log.info("Verifying Iteams in Cart")
        cartsize = cart_obj.get_iteamsincart()
        log.info(len(cartsize))
        count=0
        for item in cartsize:
            log.info(item.text)
            # after verifying from xl
            otheritem = XLConfig.readData(path, 'Sheet1', 7, 6)
            if item.text==otheritem:
                count=1
        if count ==1:
            log.info("All The Items Is Added")
        else:
            assert False
    def test_5_clicktopay(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        cart_obj = cartpage(self.driver)
        get_title = self.driver.title
        log.info(get_title)
        log.info("Proceding to payment")
        cart_obj.get_clicktopay().click()
    # FUT
    def test_6_payment(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        path = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        cardname = XLConfig.readData(path, 'Sheet1', 2, 3)
        cardnumber = 123456789123456000
        expmonth = XLConfig.readData(path, 'Sheet1', 2, 5)
        expyear = XLConfig.readData(path, 'Sheet1', 2, 6)
        cvv = XLConfig.readData(path, 'Sheet1', 2, 7)
        log.info(cardnumber)
        log.info(cardname)
        homepage_obj = homepage(self.driver)
        cartandpayment_obj = cartandpayment(self.driver)
        wait = WebDriverWait(self.driver, 10);
        b.do_send_keys(cartandpayment_obj.Paymentname, cardname)
        b.do_send_keys(cartandpayment_obj.Paymentnumber, cardnumber)
        cartandpayment_obj.get_Continue().click()
        wait.until(expected_conditions.alert_is_present())
        time.sleep(5)
        alert_text1 = self.driver.switch_to.alert.text
        log.info(alert_text1)
        Alert(self.driver).accept()
        cartandpayment_obj.get_Paymentnumber().clear()
        validcardnumber = '1234567891014321'
        invalexp=20234
        b.do_send_keys(cartandpayment_obj.Paymentnumber, validcardnumber)
        b.do_send_keys(cartandpayment_obj.Expmonth, expmonth)
        b.do_send_keys(cartandpayment_obj.Expyear, invalexp)
        cartandpayment_obj.get_Continue().click()
        wait.until(expected_conditions.alert_is_present())
        time.sleep(5)
        alert_text2 = self.driver.switch_to.alert.text
        log.info(alert_text2)
        Alert(self.driver).accept()
        cartandpayment_obj.get_Expyear().clear()
        b.do_send_keys(cartandpayment_obj.Expyear, expyear)
        invalcvv = 12343456
        b.do_send_keys(cartandpayment_obj.CVV, invalcvv)
        cartandpayment_obj.get_Continue().click()
        wait.until(expected_conditions.alert_is_present())
        time.sleep(5)
        alert_text3 = self.driver.switch_to.alert.text
        log.info(alert_text3)
        Alert(self.driver).accept()
        cartandpayment_obj.get_CVV().clear()
        b.do_send_keys(cartandpayment_obj.CVV, cvv)
        time.sleep(5)
        if (alert_text1 == "Enter a valid card number" and alert_text2 == "Enter a valid expry year" and alert_text3 == "enter a valid cvv"):
            assert True
            log.info("***** alert text boxes asserted successfully****")
        cartandpayment_obj.get_Continue().click()
        time.sleep(5)
        wait = WebDriverWait(self.driver, 10);
        wait.until(expected_conditions.alert_is_present())
        time.sleep(5)
        Alert(self.driver).accept()
        time.sleep(10)
    def test_7_logout_validation(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        hp = HomePage(driver)
        hp.do_logout()
        log.info('Logout successful')

    def test_8_login_validation(self):
        driver=self.driver
        b = Base(driver)
        log = b.getLogger()
        sip=SignInPage(driver)
        loc=TestData.excel_location
        sht='Login_Admin'
        uname=XLConfig.readData(loc,sht,2,1)
        passwd=XLConfig.readData(loc,sht,2,2)
        sip.do_login(uname,passwd)
        time.sleep(3)
        assert driver.title=="Hasher's Food Swipe"
        log.info('Login successful')


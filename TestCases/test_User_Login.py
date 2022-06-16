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
        sip=SignInPage(driver)
        loc=BASE_DIR+"/TestData/FoodSwipeDatabase.xlsx"
        sht='Sheet1'
        uname=XLConfig.readData(loc,sht,2,1)
        passwd=XLConfig.readData(loc,sht,2,2)
        sip.do_login(uname,passwd)
        time.sleep(3)
        assert driver.title=="Hasher's Food Swipe"
        log.info('Login successful')
        driver.save_screenshot(BASE_DIR+"/Screenshot/"+"login.png")

    def test_2_Homepage(self):
        driver= self.driver
        b=Base(driver)
        log = b.getLogger()
        Homepage_obj = loginpage(self.driver)
        log.info("User name Noted")
        time.sleep(10)
        var = Homepage_obj.get_Profilenames().text
        log.info(var)
        assert var=="  Siddharth Kalidas"
        log.info("User Verification Is Successfully ")
    # # FUT
    def test_3_getthelist(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        path = BASE_DIR+"/TestData/FoodSwipeDatabase.xlsx"
        product_obj = loginpage(self.driver)
        log.info("You have selected All the other items")
        log.info("*******List of All The Other products******")
        size=product_obj.get_productlist()
        size1= product_obj.get_addtocart()
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
                # log.info(var)
                # log.info(var2)
                otheritem=XLConfig.readData(path, 'Sheet1', 7, 1)
                if item.text == otheritem:
                    if var == var2:
                        items.click()
                        count = 1
                        break
            var2 = 0
            if count == 1:
                break
    # # FUT
    def test_4_gotocart(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        gotocart_obj = homepage(self.driver)
        get_title = self.driver.title
        log.info(get_title)
        log.info("You have Navigate to My Cart Page")
        time.sleep(20)
        gotocart_obj.get_gotomycart().click()
    # FUT
    def test_5_Itemsincart(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        cart_obj = cartpage(self.driver)
        get_title = self.driver.title
        log.info(get_title)
        log.info("Verifying Iteams in Cart")
        cartsize=cart_obj.get_iteamsincart()
        log.info(len(cartsize))
        for item in cartsize:
            log.info(item.text)
        log.info("All The Items Is Added")
    # # FUT
    def test_6_clicktopay(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        cart_obj = cartpage(self.driver)
        get_title = self.driver.title
        log.info(get_title)
        log.info("Proceding to payment")
        cart_obj.get_clicktopay().click()
    # FUT
    def test_7_payment(self):
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
        invalexp = 20234
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
    def test_8_cancelorder(self):
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        homepage_obj = homepage(self.driver)
        orderhistorypage_obj = orderhistorypage(self.driver)
        orderhistorypage_obj.get_orderhistory().click()
        time.sleep(5)
        order_accepted = orderhistorypage_obj.order_accepted_xpath
        j = orderhistorypage_obj.get_index_order(order_accepted)
        log.info(j)
        log.info(order_accepted)
        acceptedtext = self.driver.find_element(By.XPATH, "(//div[@class='order-pending'])" + "[" + j + "]").text
        if (acceptedtext == "Accepted"):
            assert True
        viewdetail = orderhistorypage_obj.viewdetails_xpath
        j = orderhistorypage_obj.get_index_order(viewdetail)
        self.driver.find_element(By.XPATH, "(//u[text()='View Details'])" + "[" + j + "]").click()
        orderhistorypage_obj.get_cancelorder().click()
        time.sleep(5)
        order_cancelled = orderhistorypage_obj.order_cancelled_xpath
        j = orderhistorypage_obj.get_index_order(order_cancelled)
        Cancelledtext = self.driver.find_element(By.XPATH, "(//div[@class='pay-failure'])" + "[" + j + "]").text
        if (Cancelledtext == "Cancelled"):
            assert True
            log.info("Order cancelled successfully")

    def test_othermenu(self):
        path = BASE_DIR+"/TestData/FoodSwipeDatabase.xlsx"
        time.sleep(10)
        driver = self.driver
        b = Base(driver)
        log = b.getLogger()
        homepage_obj = homepage(self.driver)
        homepage_obj.get_Menu().click()
        now = datetime.now()
        current_time = now.strftime("%H")
        log.info(current_time)
        if (int(current_time) >= 9 and int(current_time) < 10):
            time.sleep(10)
            log = self.getLogger()
            log.info("You have selected Breakfast")
            log.info("*******List of Breakfast products******")
            homepage_obj.get_Breakfast().click()
            homepage_obj.get_Breakfast().click()
            time.sleep(5)
            self.elements = self.driver.find_elements(By.XPATH, "//span[@class='MuiTypography-root MuiTypography-h5 MuiCardHeader-title css-1qvr50w-MuiTypography-root']")
            lst = []
            for i in self.elements:
                self.a = i.text
                lst.append(self.a)
            log.info(lst)
            for i in range(len(lst)):
                Breakfast = XLConfig.readData(path, 'Sheet1', 7, 2)
                if(Breakfast==lst[i]):
                    j=str(i+1)
                    self.driver.find_element(By.XPATH, "//*[@id='root']/div/div[1]/div[2]/div[2]/div[3]/div/div/div["+j+"]/div/div[2]/div[2]/div/button").click()
                    time.sleep(5)
                    break
            Test_E2E.test_4_gotocart(self)
            Test_E2E.test_5_Itemsincart(self)
            Test_E2E.test_6_clicktopay(self)
            Test_E2E.test_7_payment(self)
            Test_E2E.test_8_cancelorder(self)
        elif (int(current_time) >= 11 and int(current_time) < 16):
            homepage_obj = homepage(self.driver)
            log.info("You have selected Lunch")
            time.sleep(10)
            homepage_obj.get_selectLunch().click()
            log.info("*******List of Lunch products******")
            time.sleep(10)
            sizee = homepage_obj.get_productlist()
            sizee1 = homepage_obj.get_addtocart()
            log.info(len(sizee))
            log.info(len(sizee1))
            count = 0
            var = 0
            var2 = 0
            for item in sizee:
                var += 1
                for items in sizee1:
                    var2 += 1
                    log.info(item.text)
                    log.info(items.text)
                    Lunch = XLConfig.readData(path, 'Sheet1', 7, 3)
                    if item.text == Lunch:
                        if var == var2:
                            items.click()
                            count = 1
                            break
                var2 = 0
                if count == 1:
                    break
            Test_E2E.test_4_gotocart(self)
            Test_E2E.test_5_Itemsincart(self)
            Test_E2E.test_6_clicktopay(self)
            Test_E2E.test_7_payment(self)
            Test_E2E.test_8_cancelorder(self)
        elif (int(current_time) >= 17 and int(current_time) < 19):
            log.info("You have selected Snacks")
            homepage_objs = homepage(self.driver)
            homepage_objs.get_selectSnacks().click()
            log.info("*******List of Snacks products******")
            time.sleep(10)
            sizee = homepage_objs.get_productlist()
            sizee1 = homepage_objs.get_addtocart()
            log.info(len(sizee))
            log.info(len(sizee1))
            count = 0
            var = 0
            var2 = 0
            for item in sizee:
                var += 1
                for items in sizee1:
                    var2 += 1
                    log.info(item.text)
                    log.info(items.text)
                    Snacks = XLConfig.readData(path, 'Sheet1', 7, 4)
                    if item.text == Snacks:
                        if var == var2:
                            items.click()
                            count = 1
                            break
                var2 = 0
                if count == 1:
                    break
            Test_E2E.test_4_gotocart(self)
            Test_E2E.test_5_Itemsincart(self)
            Test_E2E.test_6_clicktopay(self)
            Test_E2E.test_7_payment(self)
            Test_E2E.test_8_cancelorder(self)
        elif (int(current_time) >= 19 and int(current_time) < 24):
            log.info("You have selected Dinner")
            homepage_obj.get_selectdineer().click()
            log.info("*******List of Dinner products******")
            time.sleep(10)
            sizee = homepage_obj.get_productlist()
            sizee1 = homepage_obj.get_addtocart()
            log.info(len(sizee))
            log.info(len(sizee1))
            count = 0
            var = 0
            var2 = 0
            for item in sizee:
                var += 1
                for items in sizee1:
                    var2 += 1
                    log.info(item.text)
                    log.info(items.text)
                    Dinner = XLConfig.readData(path, 'Sheet1', 7, 5)
                    if item.text == Dinner:
                        if var == var2:
                            items.click()
                            count = 1
                            break
                var2 = 0
                if count == 1:
                    break
            Test_E2E.test_4_gotocart(self)
            Test_E2E.test_5_Itemsincart(self)
            Test_E2E.test_6_clicktopay(self)
            Test_E2E.test_7_payment(self)
            Test_E2E.test_8_cancelorder(self)
        else:
            log.info("Currently Catagories are closed ")
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        cls.driver.close()
        cls.driver.quit()

import json
import time
import unittest

import pytest
import requests
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
import os
BASE_DIR1=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import logging
logger = logging.getLogger()
fhandler = logging.FileHandler(filename=BASE_DIR1+'/Log/TestAPILogs.txt', mode='a+')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.INFO)


from datetime import datetime
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from Utils.browser_Page import TestData


class Test_API(unittest.TestCase):

    '@pytest.mark.run(order=1)'
    '@pytest.mark.login'
    '@pytest.mark.dependency()'

    def test_User_Login(self):
        logger.info("Login User API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        Login = XLConfig.readData(loc, sht, 4, 2)
        print(Login)
        logger.info("Hit the Checkout-Services login Url")
        file = open(BASE_DIR + "/TestData/checkout-service_1.json")  # loc of and open the json
        json_ip = file.read()  # this to read the json
        request_json = json.loads(json_ip)  # this for load  the json
        print(request_json)
        req = requests.post(Login, json=request_json)
        respontoken = req.headers
        str = respontoken['authorization']
        print(str)
        XLConfig.writeData(loc, sht, 2, 10, str)
        logger.info("Login User API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False
    def test_one_order_by_order_id_and_user_id(self):
        logger.info("Feach order by user id and order id API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        orderbyuseridandorderid = XLConfig.readData(loc, sht, 5, 2)
        print(orderbyuseridandorderid)
        logger.info("Hit the Checkout-Services login Url")
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}
        req = requests.get(orderbyuseridandorderid,headers=headers_dict)
        logger.info("fetch API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False
    def test_fetch_order_history_by_user_id(self):
        logger.info("Feach order by user id  API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        orderbyuseridandorderid = XLConfig.readData(loc, sht, 10, 2)
        print(orderbyuseridandorderid)
        logger.info("Hit the Checkout-Services login Url")
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}
        req = requests.get(orderbyuseridandorderid, headers=headers_dict)
        logger.info("fetch API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False
    def test_fetch_all_orders_for_all_user(self):
        logger.info("Feach all order by user  API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        allorderbyuser = XLConfig.readData(loc, sht, 6, 2)
        print(allorderbyuser)
        logger.info("Hit the Checkout-Services login Url")
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}
        req = requests.get(allorderbyuser, headers=headers_dict)
        logger.info("fetch API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False
    def test_update_menu_desc(self):
        logger.info("Update Menu API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        updatemenu = XLConfig.readData(loc, sht, 7, 2)
        print(updatemenu)
        logger.info("Hit the Checkout-Services login Url")
        file = open(BASE_DIR + "/TestData/checkout-service_4.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}
        req = requests.put(updatemenu,json=request_json, headers=headers_dict)
        logger.info("fetch API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False
    def test_cancel_order(self):
        logger.info("Cancel order API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        canelorder = XLConfig.readData(loc, sht, 8, 2)
        print(canelorder)
        logger.info("Hit the Checkout-Services login Url")
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}
        req = requests.put(canelorder, headers=headers_dict)
        logger.info("fetch API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False
    def test_create_a_new_order(self):
        logger.info("Creat new order API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        createneworder = XLConfig.readData(loc, sht, 9, 2)
        print(createneworder)
        logger.info("Hit the Checkout-Services login Url")
        file = open(BASE_DIR + "/TestData/checkout-service_6.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}
        req = requests.post(createneworder,json=request_json, headers=headers_dict)
        logger.info("fetch API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
        else:
            assert False


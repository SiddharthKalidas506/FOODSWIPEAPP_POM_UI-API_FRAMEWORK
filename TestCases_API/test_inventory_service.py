import json
import time
import unittest

import pytest
import requests

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


    def test_adminLogin(self):
        logger.info("Login Admin API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        Login = XLConfig.readData(loc, sht, 1, 2)
        logger.info("Hit the inventory login Url")
        file = open(BASE_DIR + "/TestData/inventory-service_LoginAdmin.json") # loc of and open the json
        json_ip = file.read() # this to read the json
        request_json = json.loads(json_ip)  # this for load  the json
        req = requests.post(Login, json=request_json)
        respontoken=req.headers
        str=respontoken['authorization']
        print(str)
        XLConfig.writeData(loc, sht, 2, 10,str)
        logger.info("Login admin API response received ")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code==statuscode:
            assert True
        else:
            assert False
    def test_add_an_item(self):
        logger.info("Preceding To Add Item API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        additem = XLConfig.readData(loc, sht, 2, 2)
        logger.info("Hit the inventory Add Item Url")
        file = open(BASE_DIR + "/TestData/inventory-service_additem.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        token=XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token} # addtoken
        req = requests.post(additem, json=request_json,headers=headers_dict)
        logger.info("Hit Add Item API Done")
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(statuscode)
        if req.status_code==statuscode:
            assert True
        else:
            assert False

    def test_change_availability(self):
        logger.info("Preceding To Update Item API invoked")
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        updateitem = XLConfig.readData(loc, sht, 3, 2)
        logger.info("Hit the inventory Add Item Url")
        file = open(BASE_DIR + "/TestData/inventory-service_Updateavailability.json")

        json_ip = file.read()
        request_json = json.loads(json_ip)
        token = XLConfig.readData(loc, sht, 2, 10)
        headers_dict = {"Authorization": "Bearer " + token}  # addtoken
        req = requests.put(updateitem, json=request_json, headers=headers_dict)
        statuscode = XLConfig.readData(loc, sht, 2, 9)
        logger.info(req.status_code)
        logger.info(statuscode)
        if req.status_code == statuscode:
            assert True
            logger.info("Hit update Item API Done")
        else:
            assert False


import os

import  requests
import json
import jsonpath

from Utils.XLConfig import XLConfig

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



class Test_API_cartService:

    def test_1_loginUser(self):
        login_User_url = "https://may-hasherfoodswipe-backend-user-urtjok3rza-wl.a.run.app/v1/public/user/login-user"
        file = open(BASE_DIR + "/TestData/loginUser.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        response = requests.post(login_User_url, json=request_json)
        try:
            assert response.status_code == 200
            resp_json=response.headers.get('authorization')
            print(response.headers)
            sht = 'API_URL'
            loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
            XLConfig.writeData(loc,sht,2,10,resp_json)
        except:
            assert False


    def test_2_fetchUserCartDetails(self):
        userId='SiddharthKalidas@deloitte.com'
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        toc=XLConfig.readData(loc,sht,2,10)
        menu_url="https://may-hasherfoodswipe-backend-api-urtjok3rza-wl.a.run.app/cart-service/v1/auth/carts/"+userId
        headers_dict = {"Authorization": "Bearer " + toc}
        resp = requests.get(menu_url, headers=headers_dict)
        try:
            assert resp.status_code==200
            print(resp.text)
        except:
            print('cart is empty')
            assert False

    def test_3_UpdateCartDetails(self):
        userId = 'SiddharthKalidas@deloitte.com'
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        toc = XLConfig.readData(loc, sht, 2, 10)
        url = "https://may-hasherfoodswipe-backend-api-urtjok3rza-wl.a.run.app/cart-service/v1/auth/carts/" + userId
        headers_dict = {"Authorization": "Bearer " + toc}
        file = open(BASE_DIR + "/TestData/CartService_updateCart.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        resp = requests.put(url, json=request_json, headers=headers_dict)
        try:
            assert resp.status_code==202
            print(resp.text)
        except:
            print('cart not found')
            assert False








